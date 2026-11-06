dole = 1
nahore = 100
tip = (dole+nahore) //2
pokusy = 0

while True:
    print(f"Můj tip je {tip}")

    pokusy +=1

    odpoved = input("Je číslo větší,menší nebo rovno? (v,m,s): ").lower()

    if odpoved == "s":
        print(f"Uhádl jsem číslo {tip} na {pokusy} pokus")
        break
    elif odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    else:
        print("Neplatná odpověď. Zadej 'v', 'm' nebo 's'.")
        pokusy -= 1

    if dole > nahore:
        print(" Lhát se nemá! takže takové číslo není v našem rozmezí .")