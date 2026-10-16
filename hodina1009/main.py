# vyhodnocení kolize

# kolizní doména (obdelník)
x1 = 2
y1 = 1.5
x2 = 6
y2 = 7

# bod (panáček)
xb = float(input("Zadej x souřadnici panáčka: "))
yb = float(input("Zadej y souřadnici panáčka: "))

# test kolize
if xb > x1 and xb < x2 and yb > y1 and yb < y2:
    print("Jsi v zone")
elif xb >= x1 and xb <= x2 and yb >= y1 and yb <= y2:
     print("Jsi na kraji zony")
else: print("Nejsi v zone")
