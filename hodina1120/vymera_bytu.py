# Výpočet celkové výměry bytu v m2

def obsah_obdelnika(a,b):       # funcke pro výpočet výměry pokoje 
    if a<= 0 or b <=0:
        return None
    obsah = a * b
    return obsah                # return a * b

print("Program pro celkovou výměru bytu")
pocet_pokoju = int(input("Zadej počet pokojů: "))

pokoj = 1                       #  první pokoj 
celkova_vymera = 0
while pokoj <= pocet_pokoju:
    print(f"Zadej rozměry {pokoj}. místnosti")
    strana_a = float(input("Zadej rozměr a: "))
    strana_b = float(input("Zadej rozměr b: "))
    rozloha_pokoje = obsah_obdelnika(strana_a, strana_b)
    if rozloha_pokoje != None:
        celkova_vymera += rozloha_pokoje
        pokoj +=1
    else:
        print("Neplatný rozměr,zadej platné rozměry")
if (pocet_pokoju > 0) :
    print(f"Celková výměra bytu je: {celkova_vymera} m2.")
else:
    print("Zadej kladný rozměr")
