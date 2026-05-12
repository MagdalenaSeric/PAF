import math

brojevi = []

for i in range(10):
    x = float(input("Unesi broj:"))
    brojevi.append(x)

n = len(brojevi)

#aritmetička sredina
suma = 0

for x in brojevi:
    suma += x

x_sr = suma / n

#standardna devijacija
suma_kvadrata = 0

for x in brojevi:
    suma_kvadrata += (x - x_sr)**2

sigma = math.sqrt(suma_kvadrata / (n * (n-1)))


print("Aritmetička sredina: ", x_sr)
print("Standardna devijacija: ", sigma)