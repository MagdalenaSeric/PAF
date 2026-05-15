import numpy as np
import math

malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()


def sigma_n(lista):
    n = len(lista)
    x_sr = sum(lista) / n
    suma = 0
    for x in lista:
        suma += (x - x_sr) ** 2
    return math.sqrt(suma / n)


def s(lista):
    n = len(lista)
    x_sr = sum(lista) / n
    suma = 0
    for x in lista:
        suma += (x - x_sr) ** 2
    return math.sqrt(suma / (n - 1))


def sigma_x(lista):
    n = len(lista)
    return s(lista) / math.sqrt(n)


sigma_n_mali = sigma_n(malo_n)
s_mali = s(malo_n)
sigma_x_mali = sigma_x(malo_n)

sigma_n_veliki = sigma_n(veliko_n)
s_veliki = s(veliko_n)
sigma_x_veliki = sigma_x(veliko_n)


print("MALI SKUP PODATAKA")
print("σn =", sigma_n_mali)
print("s =", s_mali)
print("σx =", sigma_x_mali)

print("-----------------------")

print("VELIKI SKUP PODATAKA")
print("σn =", sigma_n_veliki)
print("s =", s_veliki)
print("σx =", sigma_x_veliki)

print("-----------------------")

rel_mali = abs(sigma_n_mali - s_mali) / s_mali * 100
rel_veliki = abs(sigma_n_veliki - s_veliki) / s_veliki * 100

print("RELATIVNA RAZLIKA")
print("Mali skup =", rel_mali, "%")
print("Veliki skup =", rel_veliki, "%")