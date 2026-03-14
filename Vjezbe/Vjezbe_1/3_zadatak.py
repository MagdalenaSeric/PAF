def string_je_broj(broj):
    broj = broj.replace("-", "", 1)
    broj = broj.replace(".", "", 1)
    return broj.isdigit()


while True:
    x1 = input("Upiši koordinatu x1: ")
    y1 = input("Upiši koordinatu y1: ")
    if string_je_broj(x1) and string_je_broj(y1):
        x1 = int(x1)
        y1 = int(y1)
        break
    else:
        print("Pogrešno definirane koordinate. Upišite ponovno!")

while True:
    x2 = input("Upiši koordinatu x2: ")
    y2 = input("Upiši koordinatu y2: ")
    if string_je_broj(x2) and string_je_broj(y2):
        x2 = int(x2)
        y2 = int(y2)
        break
    else:
        print("Pogrešno definirane koordinate. Upišite ponovno!")

if x1 == x2:
    print(f"Pravac je vertikalan. Jednadžba: x = {x1}.")
else:
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    print(f"Jednadžba pravca: y = {round(k, 2)}x + {round(l, 2)}")
