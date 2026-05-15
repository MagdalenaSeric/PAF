import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]


def histogram(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)
    h = (xmax - xmin) / k
    rubovi = []
    frekvencije = [0] * k

    for i in range(k + 1):
        rubovi.append(xmin + i * h)

    for x in podaci:
        if x == xmax:
            frekvencije[k - 1] += 1
            continue

        for i in range(k):
            if rubovi[i] <= x < rubovi[i + 1]:
                frekvencije[i] += 1
                break

    print("Histogram:\n")

    for i in range(k):
        lijevi = rubovi[i]
        desni = rubovi[i + 1]

        if i == k - 1:
            print(f"[{lijevi:.2f},{desni:.2f}]: {frekvencije[i]}")
        else:
            print(f"[{lijevi:.2f},{desni:.2f}): {frekvencije[i]}")

    return rubovi, frekvencije

k = 10
rubovi, frekvencije = histogram(mase_ciste, k)

sirina = rubovi[1] - rubovi[0]

plt.bar(rubovi[:-1], frekvencije, width=sirina, align='edge', edgecolor = "black")

plt.xlabel("Masa zvijezde")
plt.ylabel("Frekvencija")
plt.title("Histogram mjerenja mase Sirius A")

plt.show()