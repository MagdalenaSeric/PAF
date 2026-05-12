import math

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

n = len(M)

suma_xy = 0
suma_x2 = 0

for i in range(n):
    suma_xy += fi[i] * M[i]
    suma_x2 += fi[i] ** 2

a = suma_xy / suma_x2

suma_y2 = 0

for y in M:
    suma_y2 += y ** 2

sigma_a = math.sqrt((1/n) * ((suma_y2 / suma_x2) - a**2))

print("Modul torzije (Dt) aluminijske šipke:", a)
print("Standardna pogreška:", sigma_a)