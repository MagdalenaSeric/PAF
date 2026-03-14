x1 = float(input("Unesi koordinatu: "))
y1 = float(input("Unesi koordinatu: "))
x2 = float(input("Unesi koordinatu: "))
y2 = float(input("Unesi koordinatu: "))


def jednadzba(x1, y1, x2, y2):
    if x1 == x2:
        print(f"Pravac je vertikalan. Jednadžba: x = {x1}.")
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f"Jednadžba pravca: y = {round(k, 2)}x + {round(l, 2)}.")


jednadzba(x1, y1, x2, y2)
