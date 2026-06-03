import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653, 0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460])
T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720, 1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573])

g = 9.81
theta = np.radians(kut_deg)

#teorijska funkcija
def T_model(theta, l):
    return 2 * np.pi * np.sqrt(l / (g * np.cos(theta)))

#fit (efektivne duljine niti)
l120, _ = curve_fit(T_model, theta, T_120, p0 = [0.12])
l240, _ = curve_fit(T_model, theta, T_240, p0 = [0.24])

l120 = l120[0]
l240 = l240[0]

print("l_120 =", l120, "m")
print("l_240 =", l240, "m")

#relativne pogreške
err120 = abs(l120 - 0.120) / 0.120 * 100
err240 = abs(l240 - 0.240)/ 0.240 * 100

print("Relativna pogreška 120 mm =", err120, "%")
print("Relativna pogreška 240 mm =", err240, "%")

#graf
theta_plot = np.linspace(0, np.deg2rad(85), 500)

plt.figure(figsize=(8,5))

plt.scatter(kut_deg, T_120, label='Mjerenja L = 120 mm')
plt.plot(np.rad2deg(theta_plot), T_model(theta_plot, l120), label=f'Fit, l={l120:.3f} m')

plt.scatter(kut_deg, T_240, label='Mjerenja L=240 mm')
plt.plot(np.rad2deg(theta_plot), T_model(theta_plot, l240), label=f'Fit, l={l240:.3f} m')

plt.xlabel('Kut θ (°)')
plt.ylabel('Period T (s)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()