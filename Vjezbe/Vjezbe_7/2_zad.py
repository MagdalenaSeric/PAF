import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

mase_ciste = np.random.normal(loc = 2.06, scale = 0.05, size = 57).tolist()

sredina = np.mean(mase_ciste)
medijan = np.median(mase_ciste)

plt.hist(mase_ciste, bins = 10, edgecolor = "black")

plt.axvline(sredina, linestyle = '--', label = f'Sredina = {sredina:.3f}', color = "red")

plt.axvline(medijan, linestyle = ':', label = f'Medijan = {medijan:.3f}', color = "magenta")

plt.xlabel("Masa zvijezde")
plt.ylabel("Frekvencija")
plt.title("Histogram mase Sirius A")

plt.legend()
plt.show()