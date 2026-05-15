import math


def volumen_valjka(R, L):
    return math.pi * R**2 * L

def sigma_volumena(R, sigma_R, L, sigma_L):

    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * R**2

    return math.sqrt((dV_dR * sigma_R)**2 +
                     (dV_dL * sigma_L)**2)

def gustoća(m, V):
    return m / V

def sigma_gustoće(m, sigma_m, V, sigma_V):

    dRho_dm = 1 / V
    dRho_dV = -m / V**2

    return math.sqrt((dRho_dm * sigma_m)**2 +
                     (dRho_dV * sigma_V)**2)


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

m1 = 138.98
m2 = 128.55
m3 = 71.77

sigma_m1 = 0.056
sigma_m2 = 0.058
sigma_m3 = 0.057


V1 = volumen_valjka(R1, L1)
V2 = volumen_valjka(R2, L2)
V3 = volumen_valjka(R3, L3)

sigma_V1 = sigma_volumena(R1, sigma_R1, L1, sigma_L1)
sigma_V2 = sigma_volumena(R2, sigma_R2, L2, sigma_L2)
sigma_V3 = sigma_volumena(R3, sigma_R3, L3, sigma_L3)


rho1 = gustoća(m1, V1)
rho2 = gustoća(m2, V2)
rho3 = gustoća(m3, V3)

sigma_rho1 = sigma_gustoće(m1, sigma_m1, V1, sigma_V1)
sigma_rho2 = sigma_gustoće(m2, sigma_m2, V2, sigma_V2)
sigma_rho3 = sigma_gustoće(m3, sigma_m3, V3, sigma_V3)


print("Valjak 1")
print("ρ = %.3e g/cm^3" % rho1)
print("σρ = %.3e g/cm^3" % sigma_rho1)

print("-----------------------")

print("Valjak 2")
print("ρ = %.3e g/cm^3" % rho2)
print("σρ = %.3e g/cm^3" % sigma_rho2)

print("-----------------------")

print("Valjak 3")
print("ρ = %.3e g/cm^3" % rho3)
print("σρ = %.3e g/cm^3" % sigma_rho3)