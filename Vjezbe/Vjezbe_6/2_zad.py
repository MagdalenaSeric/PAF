import math


def volumen_valjka(R, L):
    return (R**2) * math.pi * L


def sigma_volumena(R, sigma_R, L, sigma_L):

    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * R**2

    sigma_V = math.sqrt((dV_dR * sigma_R)**2 +
                        (dV_dL * sigma_L)**2)

    return sigma_V


R1 = 19.98 / 20
R2 = 19.91 / 20
R3 = 24.96 / 20

sigma_R1 = 0.074 / 20
sigma_R2 = 0.028 / 20
sigma_R3 = 0.012 / 20

L1 = 49.81 / 10
L2 = 52.56 / 10
L3 = 55.39 / 10

sigma_L1 = 0.241 / 10
sigma_L2 = 0.021 / 10
sigma_L3 = 0.031 / 10


V1 = volumen_valjka(R1, L1)
V2 = volumen_valjka(R2, L2)
V3 = volumen_valjka(R3, L3)

sigma_V1 = sigma_volumena(R1, sigma_R1, L1, sigma_L1)
sigma_V2 = sigma_volumena(R2, sigma_R2, L2, sigma_L2)
sigma_V3 = sigma_volumena(R3, sigma_R3, L3, sigma_L3)


print("Valjak 1")
print(f"V = {V1:.3e} cm^3")
print(f"σV = {sigma_V1:.3e} cm^3")

print("-----------------------")

print("Valjak 2")
print(f"V = {V2:.3e} cm^3")
print(f"σV = {sigma_V2:.3e} cm^3")

print("-----------------------")

print("Valjak 3")
print(f"V = {V3:.3e} cm^3")
print(f"σV = {sigma_V3:.3e} cm^3")