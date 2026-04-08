import calculus as calc
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2 * x**2 + 3


print("Gornja i donja integralna suma su: ", calc.pravokutna_metoda(f, 0, 1, 100))
print("Integral pomoću trapeza: ", calc.trapezna_metoda(f, 0, 1, 100))

n = np.arange(50, 501, 20)
y = [11 / 3] * len(n)

trapezni = []
prav_gornji = []
prav_donji = []

for i in n:
    trapezni.append(calc.trapezna_metoda(f, 0, 1, i))
    g, d = calc.pravokutna_metoda(f, 0, 1, i)
    prav_gornji.append(g)
    prav_donji.append(d)

plt.plot(n, y, label="Analitičko rješenje", linewidth=2)
plt.title("Numerička integracija funkcije 2x^2 + 3")
plt.xlabel("n (broj podintervala)")
plt.ylabel("Vrijednost integrala")
plt.scatter(n, trapezni, s=10, label="Trapezna metoda")
plt.scatter(n, prav_gornji, s=10, label="Gornja suma")
plt.scatter(n, prav_donji, s=10, label="Donja suma")
plt.legend()
plt.grid()
plt.show()
