import numpy as np

def medijan(podaci):
    sortirani = sorted(podaci)
    n = len(sortirani)

    # neparan broj elemenata
    if n % 2 != 0:
        return sortirani[n // 2]

    # paran broj elemenata
    else:
        srednji1 = sortirani[n // 2 - 1]
        srednji2 = sortirani[n // 2]

        return (srednji1 + srednji2) / 2


a = [3, 1, 4, 1, 5, 9, 2, 6]
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("Medijan liste a =", medijan(a))
print("Medijan liste b =", medijan(b))

print("-----------------------")

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

moj_medijan = medijan(mase)

numpy_medijan = np.median(mase)

print("Medijan masa (funkcija) =", moj_medijan)
print("Medijan masa (numpy) =", numpy_medijan)