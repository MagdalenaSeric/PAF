import math

R1 = [19.98, 20.18, 20.10, 20.08, 19.74]
R2 = [19.92, 19.82, 19.96, 19.98, 19.88]
R3 = [24.96, 24.98, 24.98, 24.92, 24.94]

L1 = [49.80, 49.00, 50.48, 49.80, 49.96]
L2 = [52.56, 52.50, 52.62, 52.58, 52.54]
L3 = [55.34, 55.40, 55.30, 55.44, 55.48]

m1 = [138.92, 138.98, 139.20, 138.90, 138.92]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
m3 = [71.59, 71.90, 71.79, 71.85, 71.70]


def srednja_vrijednost(lista):
    return sum(lista) / len(lista)

def standardno_odstupanje(lista):
    n = len(lista)
    x_sr = srednja_vrijednost(lista)

    suma = 0

    for x in lista:
        suma += (x - x_sr) ** 2

    return math.sqrt(suma / (n * (n - 1)))


# Valjak 1
R_sr1 = srednja_vrijednost(R1)
sigma_R1 = standardno_odstupanje(R1)

L_sr1 = srednja_vrijednost(L1)
sigma_L1 = standardno_odstupanje(L1)

m_sr1 = srednja_vrijednost(m1)
sigma_m1 = standardno_odstupanje(m1)

print("Valjak 1:")
print("R̄ =", round(R_sr1, 3), "mm")
print("σR =", round(sigma_R1, 3), "mm")

print("L̄ =", round(L_sr1, 3), "mm")
print("σL =", round(sigma_L1, 3), "mm")

print("m̄ =", round(m_sr1, 3), "g")
print("σm =", round(sigma_m1, 3), "g")

print("-----------------------")

# Valjak 2
R_sr2 = srednja_vrijednost(R2)
sigma_R2 = standardno_odstupanje(R2)

L_sr2 = srednja_vrijednost(L2)
sigma_L2 = standardno_odstupanje(L2)

m_sr2 = srednja_vrijednost(m2)
sigma_m2 = standardno_odstupanje(m2)

print("Valjak 2:")
print("R̄ =", round(R_sr2, 3), "mm")
print("σR =", round(sigma_R2, 3), "mm")

print("L̄ =", round(L_sr2, 3), "mm")
print("σL =", round(sigma_L2, 3), "mm")

print("m̄ =", round(m_sr2, 3), "g")
print("σm =", round(sigma_m2, 3), "g")

print("-----------------------")

# Valjak 3
R_sr3 = srednja_vrijednost(R3)
sigma_R3 = standardno_odstupanje(R3)

L_sr3 = srednja_vrijednost(L3)
sigma_L3 = standardno_odstupanje(L3)

m_sr3 = srednja_vrijednost(m3)
sigma_m3 = standardno_odstupanje(m3)

print("Valjak 3:")
print("R̄ =", round(R_sr3, 3), "mm")
print("σR =", round(sigma_R3, 3), "mm")

print("L̄ =", round(L_sr3, 3), "mm")
print("σL =", round(sigma_L3, 3), "mm")

print("m̄ =", round(m_sr3, 3), "g")
print("σm =", round(sigma_m3, 3), "g")