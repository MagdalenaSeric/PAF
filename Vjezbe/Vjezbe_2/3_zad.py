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

x = np.linspace(-2, 2, 100)

lista_kub1 = calc.derivacija_na_intervalu(f1, -2, 2, 0.5)
lista_kub2 = calc.derivacija_na_intervalu(f1, -2, 2, 0.01)
lista_kub3 = calc.derivacija_na_intervalu(f1, -2, 2, 0.0001)

# iznos derivacija od -2 do 2, a iznos h se mijenja

lista_sin1 = calc.derivacija_na_intervalu(f2, -2, 2, 0.5)
lista_sin2 = calc.derivacija_na_intervalu(f2, -2, 2, 0.01)
lista_sin3 = calc.derivacija_na_intervalu(f2, -2, 2, 0.0001)

plt.subplot(1, 2, 1)
plt.plot(x, df1(x), label="Analitička", linewidth=2, color="pink")
plt.scatter(lista_kub1[0], lista_kub1[1], color="red", s=5, label="h = 0.5")
plt.scatter(lista_kub2[0], lista_kub2[1], color="green", s=5, label="h = 0.01")
plt.scatter(lista_kub3[0], lista_kub3[1], color="blue", s=5, label="h = 0.0001")
plt.title("Kubna funkcija")
plt.xlabel("x")
plt.ylabel("df(x)/dx")
plt.grid()
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(x, df2(x), label="Analitička", linewidth=2, color="pink")
plt.scatter(lista_sin1[0], lista_sin1[1], color="red", s=5, label="h = 0.5")
plt.scatter(lista_sin2[0], lista_sin2[1], color="green", s=5, label="h = 0.01")
plt.scatter(lista_sin3[0], lista_sin3[1], color="blue", s=5, label="h = 0.0001")
plt.title("Trigonometrijska funkcija")
plt.xlabel("x")
plt.ylabel("df/dx")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
