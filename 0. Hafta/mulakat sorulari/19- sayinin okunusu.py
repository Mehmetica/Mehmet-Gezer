sayi = int(input("iki basamakli bir sayi giriniz: "))

onlar_dizisi = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
birler_dizisi = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]

basamak_sayisi = len(str(sayi))

while True:
    if sayi >= 10 and sayi < 100:
        onlar_basamagi = int(sayi / 10)
        birler_basamagi = sayi % 10
        okunus = onlar_dizisi[onlar_basamagi - 1] + " " + birler_dizisi[birler_basamagi]
        print("Sayının okunusu:", okunus)

        print("Programdan cikmak ister misiniz?: E/H")
        cevap = input().upper()
        if cevap == "E":
            break
        elif cevap == "H":
            sayi = int(input("Iki basamakli bir sayi giriniz: "))
        else:
            print("Yanlis giris yaptiniz, E/H giriniz")
    else:
        sayi = int(input("Iki basamakli bir sayi giriniz: "))
