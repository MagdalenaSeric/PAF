import matplotlib.pyplot as plt
import numpy as np


class Particle:
    g = 9.81

    def __init__(self, v0, kut, x0, y0):
        self.v0 = v0
        self.kut = np.radians(kut)
        self.x0 = x0
        self.y0 = y0

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.t = 0
        self.lista_x = [self.x]
        self.lista_y = [self.y]

    def __move(self, dt):
        self.vy -= Particle.g * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.t += dt
        self.lista_x.append(self.x)
        self.lista_y.append(self.y)

    def range(self, dt=0.005):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt=0.005):
        self.range(dt)

        plt.plot(self.lista_x, self.lista_y, label="Numerička putanja")
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.title("Putanja čestice")
        plt.grid()
        plt.legend()
        plt.show()
