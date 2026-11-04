import random

tajne_cislo = random.randint(1, 20)
pokusy = 0
tip = 0

print("Myslím si číslo od 1 do 20.")

while tip != tajne_cislo:
    vstup = input("Zadej svůj tip: ")
    tip = int(vstup)

    pokusy += 1

    if tip < tajne_cislo:
        print("Moje číslo je VĚTŠÍ!\n")
    elif tip > tajne_cislo:
        print("Moje číslo je MENŠÍ!\n")
    else:
        print(f" Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")