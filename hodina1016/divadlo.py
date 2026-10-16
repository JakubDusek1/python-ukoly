
pocet = int(input("Zadej počet lidí: "))

# default hodnoty
cena = 500
typ_vstupenky = "Bez slevy"

if pocet>=4:
    cena *= 0.75
    typ_vstupenky = "Skupinová sleva"
else:
    vek = float(input("Zadej věk: "))
    if vek>=65:
        cena *= 0.8
        typ_vstupenky = "Senioři"
    elif vek<26:
        student = input("Student [ano/ne] ")
        if student=="ano":
            cena *= 0.7
            typ_vstupenky = "Studenti"

#tady to bude po dodělání bloků laždé z větví
print("Cena vstupenky:", cena)
print("Cena celková:", cena * pocet)
        