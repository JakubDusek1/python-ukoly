# Zadání 3 čísel
a = int(input("Zadej 1. číslo: "))
b = int(input("Zadej 2. číslo: "))
c = int(input("Zadej 3. číslo: "))

# např. 7, 10, 2
if a > b:
    p = a
    a = b
    b = p
    # (1): 7,10,2
if b > c:
    p = b
    b = c
    c = p
    # (2): 7,2,10
if a > b:
    p = a
    a = b
    b = p
    # (3): 2,7,10

print(f"{a}<{b}<{c}")