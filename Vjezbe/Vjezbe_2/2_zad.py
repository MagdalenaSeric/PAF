import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
kut = np.radians(60)

domet_anal = (v0**2 * np.sin(2 * kut)) / g


def simulacija(dt):
    x = 0
    y = 0
    vx = v0 * np.cos(kut)
    vy = v0 * np.sin(kut)

    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy -= g * dt

    return x


vrijednosti_dt = []
for i in range(1, 101):
    vrijednosti_dt.append(i * 0.001)

odstupanja = []

for dt in vrijednosti_dt:
    domet_num = simulacija(dt)
    odstupanja.append(abs(domet_num - domet_anal) / domet_anal)

plt.plot(vrijednosti_dt, odstupanja)
plt.xlabel("dt/s")
plt.ylabel("Relativna pogreška / %")
plt.grid()
plt.title("Ovisnost relativne pogreške o vrijednosti dt")
plt.show()
