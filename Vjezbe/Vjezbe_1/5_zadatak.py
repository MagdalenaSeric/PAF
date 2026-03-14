import matplotlib.pyplot as plt
import numpy as np

x1 = float(input("Unesi koordinatu x: "))
y1 = float(input("Unesi koordinatu y: "))
x2 = float(input("Unesi koordinatu x: "))
y2 = float(input("Unesi koordinatu y: "))


def graf_jednadzbe(x1, y1, x2, y2):
    unos = (
        input("Unesi 'p' za prikaz grafa ili 's' za spremanje grafa: ").strip().lower()
    )

    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
        x = [x1, x2]
        y = [y1, y2]
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f"Jednadžba pravca: y = {round(k, 2)}x + {round(l, 2)}.")
        x = np.linspace(x1 - 2, x2 + 2, 200)
        y = k * x + l

    plt.plot(x, y)
    plt.scatter([x1, x2], [y1, y2])
    plt.title("Pravac kroz dvije zadane točke.")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()

    if unos == "s":
        naziv_datoteke = input("Upiši naziv datoteke (sa .pdf): ")
        plt.savefig(naziv_datoteke)
    else:
        plt.show()


graf_jednadzbe(x1, y1, x2, y2)
