import numpy as np
import matplotlib.pyplot as plt

#PODATCI
h0 = 0.54        #ukupna visina
m = 0.5257       #masa diska
r = 4.025e-3     #polumjer osovine
g = 9.81

#prosječni padovi
h = np.array([0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40])

t_mean = np.array([1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813])

s = h       #pad od početne pozicije

def linearna_regresija(x, y):
    n = len(x)

    #sume
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxx = np.sum(x**2)
    Sxy = np.sum(x*y)

    #nagib i odsječak
    a = (n * Sxy - Sx * Sy) / (n * Sxx - Sx**2)
    b = (Sy - a * Sx) / n

    y_fit = a * x + b
    odstupanja = y - y_fit

    #ukupna udaljenost točaka od regresijskog pravca
    sigma2 = np.sum(odstupanja**2) / (n - 2)

    #pogreška nagiba pravca
    sa = np.sqrt(n * sigma2 / (n * Sxx - Sx**2))
    #pogreška odjsečka pravca
    sb = np.sqrt(sigma2 * Sxx / (n * Sxx - Sx**2))

    return a, b, sa, sb, y_fit

#--------------------------------------------------------------------------------

print("a) log(s) - log(t)")

x_log = np.log(t_mean)
y_log = np.log(s)

a_log, b_log, sa_log, sb_log, y_fit_log = linearna_regresija(x_log, y_log)

#ispisivanje a i b + njihove pogreške
print(f"Nagib (a) = {a_log} ± {sa_log}")
print(f"Odsječak (b) = {b_log} ± {sb_log}")

#graf
plt.subplot(1, 2, 1)
plt.plot(x_log, y_fit_log, color = "magenta", label = "Pravac regresije")
plt.scatter(x_log, y_log, color = "green", label = "Mjerenja")
plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.title("log(s) - log(t)")
plt.legend()
plt.tight_layout()
plt.grid()

#--------------------------------------------------------------------------------

print("b) s - t^2")

x_lin = t_mean**2
y_lin = s

a_lin, b_lin, sa_lin, sb_lin, y_fit_lin = linearna_regresija(x_lin, y_lin)

print(f"Nagib (a) = {a_lin} ± {sa_lin}")
print(f"Odsječak (b) = {b_lin} ± {sb_lin}")

#graf
plt.subplot(1, 2, 2)
plt.plot(x_lin, y_fit_lin, color = "magenta", label = "Pravac regresije")
plt.scatter(x_lin, y_lin, color = "blue", label = "Mjerenja")
plt.xlabel("t^2 [s^2]")
plt.ylabel("s [m]")
plt.title("s - t^2")
plt.legend()
plt.tight_layout()
plt.grid()

#--------------------------------------------------------------------------------

print("c) Moment tromosti")

#iz relacije: s = 1/2 * a_ef * t^2 => nagib = a_ef / 2

a_ef = 2 * a_lin        #ubrzanje
sa_ef = 2 * sa_lin      #pogreška ubrzanja

#formula: a_eff = (m * g * r^2) / (m * r^2 + Iz)
Iz = (m * g * r**2) / (a_ef) - m * r**2

#propagacija pogreške --> kako pogreška jedne veličine utječe na drugu veličinu
dIz_da_ef = -(m * g * r**2) / (a_ef ** 2)

sIz = abs(dIz_da_ef) * sa_ef

print(f"a_ef = {a_ef} ± {sa_ef} m/s^2")
print(f"Iz = ({Iz} ± {sIz}) kg m^2")

plt.show()






