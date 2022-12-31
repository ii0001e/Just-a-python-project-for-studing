def massiind():
    print("Tere! Olen sinu uus sõber - Python!")
    nimi = str(input("Mis sinu nimi on? "))
    print(f"{nimi}, oi kui ilus nimi!")
    choose = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if choose == 1:
        try:
            pikkus = int(input("Sisesta oma pikkus CM-s. => "))
            while pikkus < 0 or pikkus > 273:
                print("Pikkus peab olema rohkem kui null ja vähem kui 273. Ja kirjutatud numbritega!")
                pikkus = input("Sesesta oma pikkus CM-s. => ")
        except:
            pikkus = 170
            print("Siis pikkus on 170 cm.")
        try:
            mass = float(input("Siseta oma keha kaal KG-s. => "))
            while mass < 0:
                print("Mass peab olema rohkem kui null!")
                mass = float(input("Sesesta oma pikkus KG-s. => "))
            else:
                pass
        except:
            mass = 69
            print("Siis teie mass on 69 kg.")
        index = round((mass / (0.01 * pikkus)**2), 1)
        print(f"{nimi}! Sinu keha indeks on: {index}")
        if index <= 16:
            answer = "Tervisele ohtlik alakaal"
        elif 16 < index <= 19:
            answer = "Alakaal"
        elif 19 < index <= 25:
            answer = "Normaalkaal"
        elif 25 < index <= 30:
            answer = "Ülekaal"
        elif 30 < index <= 35:
            answer = "Rasvumine"
        elif 35 < index <= 40:
            answer = "Tugev rasvumine"
        else:
            answer = "Tervisele ohtlik rasvumine"     
    else:
        answer = "Kahju! See on väga kasulik info!" + "\n"
    print (answer)
    print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
#massiind()