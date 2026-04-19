import numpy as np
import matplotlib.pyplot as plt


class Projectile:
    g = 9.81

    def __init__(self, m, k):
        self.m = m
        self.k = k

    def akceleracija(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        ax = -(self.k / self.m) * v * vx
        ay = -self.g - (self.k / self.m) * v * vy
        return ax, ay

    def simulacija_euler(self, v0, kut, dt):
        kut = np.radians(kut)
        vx = v0 * np.cos(kut)
        vy = v0 * np.sin(kut)

        x = 0
        y = 0

        lista_x = [x]
        lista_y = [y]

        while y >= 0:
            ax, ay = self.akceleracija(vx, vy)

            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt

            lista_x.append(x)
            lista_y.append(y)

        return np.array(lista_x), np.array(lista_y)

    def simulacija_run_kut(self, v0, kut, dt):
        kut = np.radians(kut)
        vx = v0 * np.cos(kut)
        vy = v0 * np.sin(kut)

        x = 0
        y = 0

        lista_x = [x]
        lista_y = [y]

        while y >= 0:
            ax1, ay1 = self.akceleracija(vx, vy)

            vx2 = vx + 0.5 * dt * ax1
            vy2 = vy + 0.5 * dt * ay1
            ax2, ay2 = self.akceleracija(vx2, vy2)

            vx3 = vx + 0.5 * dt * ax2
            vy3 = vy + 0.5 * dt * ay2
            ax3, ay3 = self.akceleracija(vx3, vy3)

            vx4 = vx + dt * ax3
            vy4 = vy + dt * ay3
            ax4, ay4 = self.akceleracija(vx4, vy4)

            x += (dt * (vx + 2 * (vx + 0.5 * dt * ax1) + 2 * (vx + 0.5 * dt * ax2) + (vx + dt * ax3)) / 6)
            y += (dt * (vy + 2 * (vy + 0.5 * dt * ay1) + 2 * (vy + 0.5 * dt * ay2) + (vy + dt * ay3)) / 6)

            vx += dt * (ax1 + 2 * ax2 + 2 * ax3 + ax4) / 6
            vy += dt * (ay1 + 2 * ay2 + 2 * ay3 + ay4) / 6

            lista_x.append(x)
            lista_y.append(y)

        return np.array(lista_x), np.array(lista_y)


gibanje = Projectile(10, 0.1)

dt = 0.01

x_e, y_e = gibanje.simulacija_euler(25, 45, dt)
x_rk, y_rk = gibanje.simulacija_run_kut(25, 45, dt)

plt.plot(x_e, y_e, label="Eulerova metoda")
plt.plot(x_rk, y_rk, label="Runge-Kutta metoda")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Gibanje projektila opisano dvjema metodama.")
plt.grid()
plt.show()
