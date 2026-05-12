import statistics

brojevi = []

for i in range(10):
    x = float(input("Unesi broj: "))
    brojevi.append(x)

aritmetička_sredina = statistics.mean(brojevi)
standardna_devijacija = statistics.stdev(brojevi)

print("Aritmetička sredina: ", aritmetička_sredina)
print("Standardna devijacija: ", standardna_devijacija)