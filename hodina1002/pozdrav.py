
hodina = int(input("Zadej hodinu (0-23): "))

if hodina<0:
    print("Hodina nemůže být záporná.")
elif hodina > 23:
    print("Zadávejte hodiny v rozmezí 0 až 23.")

if   hodina<=5:
    print("Dobrou noc")
elif hodina<=9:
    print("Dobré ráno")
elif hodina<12:
     print("Dobré dopoledne")
elif hodina==12:
    print("Dobré poledne")
elif hodina<=16:
    print("Dobré odpoledne")
elif hodina<22:
    print("Dobrý večer")
else: hodina>=22:
    print("Dobrou noc")