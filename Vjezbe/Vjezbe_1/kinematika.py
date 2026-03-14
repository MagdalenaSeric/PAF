import matplotlib.pyplot as plt
import numpy as np


def jednoliko_gibanje(F, m):
    dt = 0.05
    t = 0

    vrijeme = [0]
    a = [F / m]

    x0 = float(input("Unesi početni pomak (u m): "))
    v0 = float(input("Unesi početni iznos brzine (u m/s): "))

    x = []
    v = []
    x.append(x0)
    v.append(v0)

    while t < 10:
        v.append(v[-1] + a[0] * dt)
        x.append(x[-1] + v[-2] * dt)

        t += dt
        vrijeme.append(t)
        a.append(F / m)

    plt.subplot(1, 3, 1)
    plt.plot(vrijeme, x)
    plt.title("Ovisnost puta o vremenu.")
    plt.xlabel("t/s")
    plt.ylabel("s/m")
    plt.grid()

    plt.subplot(1, 3, 2)
    plt.plot(vrijeme, v)
    plt.title("Ovisnost brzine o vremenu.")
    plt.xlabel("t/s")
    plt.ylabel("v/ms^{-1}")
    plt.grid()

    plt.subplot(1, 3, 3)
    plt.plot(vrijeme, a)
    plt.title("Ovisnost akceleracije o vremenu.")
    plt.xlabel("t/s")
    plt.ylabel("a/ms^{-2}")
    plt.grid()

    plt.tight_layout()
    plt.show()
