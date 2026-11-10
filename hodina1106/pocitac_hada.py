dole = 1
nahore = 100
pokusy = 0

while dole<= nahore:
    tip = (dole+nahore) //2
    pokusy +=1


    print(f"Můj tip je {tip}")
    odpoved = input("Je číslo větší,menší nebo rovno? (v,m,s): ").lower()

    if odpoved == "s":
        print(f"Uhádl jsem číslo {tip} na {pokusy} pokusů")
        break
    elif odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    else:
        print("Neplatná odpověď. Zadej 'v' (větší), 'm' (menší) nebo 's' (správně).")
        pokusy -= 1

    if dole > nahore:
        print(" Lhát se nemá! takže takové číslo není v našem rozmezí .")