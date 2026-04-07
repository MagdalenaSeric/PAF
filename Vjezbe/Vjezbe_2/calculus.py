import numpy as np


def derivacija(f, x, h, metoda="three-step"):
    if metoda == "two-step":
        return (f(x + h) - f(x)) / h

    return (f(x + h) - f(x - h)) / (2 * h)


def derivacija_na_intervalu(f, a, b, h, metoda="three-step"):
    x_evi = np.arange(a + h, b - h, h)

    derivacije = []

    for x in x_evi:
        d = derivacija(f, x, h, metoda)
        derivacije.append(d)

    return [x_evi, np.array(derivacije)]


def pravokutna_metoda(f, a, b, n):
    dx = (b - a) / n
    gornja_suma = 0
    donja_suma = 0
    for i in range(n):
        donja_suma += f(a + i * dx) * dx
        gornja_suma += f(a + (i + 1) * dx) * dx

    return [round(gornja_suma, 4), round(donja_suma, 4)]


def trapezna_metoda(f, a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + dx * i) + f(a + dx * (i + 1))

    return round((suma * dx) / 2, 4)
