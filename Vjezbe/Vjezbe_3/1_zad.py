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

    def simulacija(self, v0, kut, dt):
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


gibanje = Projectile(10, 0.1)

lista_dt = [0.5, 0.1, 0.05, 0.01]

for dt in lista_dt:
    x, y = gibanje.simulacija(20, 45, dt)
    plt.plot(x, y, label=f"dt = {dt}")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Prikaz kosog hitca uzimajući u obzir otpor zraka.")
plt.grid()
plt.show()
