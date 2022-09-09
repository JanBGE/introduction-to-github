# -------------------------------------------------------

#matkakulu

#versio 1.0

#(C) Janne Bragge, Sastamala, Suomi

#janne.bragge@edu.sasky.fi

# 11.5.2022

# -------------------------------------------------------





def bensanhinta ():
    bhinta = float(input("\nKuinka paljon bensa tai diesel maksaa litralta: "))
    print("")
    matka = float(input("Kuinka pitkä matka on kilometreissä?: "))
    print("")
    auton_kulutus_100 = float(input("Kuinka paljon autosi kuluttaa 100km kohden?: "))
    print("")
    hinta_km = bhinta / 100  
    kulutus_raha_km = hinta_km * auton_kulutus_100
    rahakulu_matkalle = kulutus_raha_km * matka
    #return rahakulu_matkalle
    print("*****************************************")
    print("Rahaa kuluu polttoaineeseen matkalla", round(rahakulu_matkalle), "euroa\n")
    print("Haluatko laskea vielä seuraavan matkan polttoainekulun?\n")
    print("*****************************************")


def main():
    while True:
        print("")
        selection = input("Paina (1) laskeaksi matkakulu haluamallesi matkalle tai paina (2) lopettaaksesi ohjelman\nAnna valintasi: ")
        if selection == "1":
            bensanhinta()
            continue
        elif selection == "2":
            print(f"\nKiitos ohjelman käytöstä")
            break
        else:
            print("Syöte ei kelpaa, valitse uudelleen")
            continue


if __name__ == '__main__':
    main()