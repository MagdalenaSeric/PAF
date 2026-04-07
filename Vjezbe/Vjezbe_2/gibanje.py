import particle as prt

import numpy as np
import matplotlib.pyplot as plt

v0 = 10
kut = 45
g = 9.81

gibanje = prt.Particle(v0, kut, 0, 0)

domet_num = gibanje.range()
domet_anal = (v0**2 * np.sin(2 * np.radians(kut))) / g

odstupanje = abs(domet_num - domet_anal)

print(f"Numerički domet: {round(domet_num, 2)}")
print(f"Analitički domet: {round(domet_anal, 2)}")
print(f"Odstupanje: {round(odstupanje, 2)}")

gibanje.plot_trajectory()
