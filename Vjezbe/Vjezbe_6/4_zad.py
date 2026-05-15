import gustoce as g

rho_lit1 = 8.5
rho_lit2 = 7.85
rho_lit3 = 2.70

rel1 = (abs(g.rho1 - rho_lit1) / rho_lit1) * 100
rel2 = (abs(g.rho2 - rho_lit2) / rho_lit2) * 100
rel3 = (abs(g.rho3 - rho_lit3) / rho_lit3) * 100


print("Valjak 1")
print("Materijal: mjed")
print("Relativna pogreška =", round(rel1, 3), "%")

print("-----------------------")

print("Valjak 2")
print("Materijal: željezo / čelik")
print("Relativna pogreška =", round(rel2, 3), "%")

print("-----------------------")

print("Valjak 3")
print("Materijal: aluminij")
print("Relativna pogreška =", round(rel3, 3), "%")