import numpy as np
import matplotlib.pyplot as plt
import calculus as calc


def f1(x):
    return x**3


def df1(x):
    return 3 * x**2


def f2(x):
    return np.sin(x)


def df2(x):
    return np.cos(x)


# analitička derivacija (prefiks d)

print("Derivacija u točki x = 2: ", calc.derivacija(f2, 2, 0.0001))
print("Pravokutna metoda: ", calc.pravokutna_metoda(f2, 1, 4, 100))
print("Trapezna metoda: ", calc.trapezna_metoda(f2, 1, 4, 100))

x = np.linspace(-2, 2, 100)

lista_1 = calc.derivacija_na_intervalu(f1, -2, 2, 0.5)
lista_2 = calc.derivacija_na_intervalu(f1, -2, 2, 0.01)
lista_3 = calc.derivacija_na_intervalu(f1, -2, 2, 0.0001)

# iznos derivacija od -2 do 2, a iznos h se mijenja

plt.plot(x, df1(x), label="Analitička", linewidth=2, color="pink")
plt.scatter(lista_1[0], lista_1[1], color="red", s=5, label="h = 0.5")
plt.scatter(lista_2[0], lista_2[1], color="green", s=5, label="h = 0.01")
plt.scatter(lista_3[0], lista_3[1], color="blue", s=5, label="h = 0.0001")
plt.title("Derivacija kubne funkcije")
plt.xlabel("x")
plt.ylabel("df(x)/dx")
plt.grid()
plt.legend()
plt.show()
