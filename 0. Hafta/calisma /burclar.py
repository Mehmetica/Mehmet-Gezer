while True:
    while True:
        gun = int(input("Dogdugunuz gunu girin (1-31): "))
        if 1 <= gun <= 31:
            break
        print("Hata: Gun 1 ile 31 arasinda olmalidir. Lutfen tekrar deneyin.")

    while True:
        ay = int(input("Dogdugunuz ayi girin (1-12): "))
        if 1 <= ay <= 12:
            break
        print("Hata: Ay 1 ile 12 arasinda olmalidir. Lutfen tekrar deneyin.")

    while True:
        yil = int(input("Dogdugunuz yili girin (YYYY): "))
        if 1 <= yil <= 2024:
            break
        print("Hata: Yil 1 ile 2024 arasinda bir sayi olmalidir. Lutfen tekrar deneyin.")

    print("\nDegerler basariyla alindi!")
    print("Dogum tarihiniz: " + str(gun) + "." + str(ay) + "." + str(yil))

    if (ay == 1 and gun >= 20) or (ay == 2 and gun <= 18):
        burc = "Kova"
        ozellikler = ["ozgur ruhlu", "Yenilikci", "insancil"]
    elif (ay == 2 and gun >= 19) or (ay == 3 and gun <= 20):
        burc = "Balik"
        ozellikler = ["Hayalperest", "Duygusal", "sefkatli"]
    elif (ay == 3 and gun >= 21) or (ay == 4 and gun <= 19):
        burc = "Koc"
        ozellikler = ["Cesur", "Enerjik", "Lider ruhlu"]
    elif (ay == 4 and gun >= 20) or (ay == 5 and gun <= 20):
        burc = "Boga"
        ozellikler = ["Sabirli", "Guvenilir", "Pratik"]
    elif (ay == 5 and gun >= 21) or (ay == 6 and gun <= 20):
        burc = "ikizler"
        ozellikler = ["Zeki", "Konuskan", "Esnek"]
    elif (ay == 6 and gun >= 21) or (ay == 7 and gun <= 22):
        burc = "Yengec"
        ozellikler = ["Duygusal", "Sadik", "Sevecen"]
    elif (ay == 7 and gun >= 23) or (ay == 8 and gun <= 22):
        burc = "Aslan"
        ozellikler = ["Kendine guvenen", "Comert", "Yaratici"]
    elif (ay == 8 and gun >= 23) or (ay == 9 and gun <= 22):
        burc = "Basak"
        ozellikler = ["Detayci", "Analitik", "caliskan"]
    elif (ay == 9 and gun >= 23) or (ay == 10 and gun <= 22):
        burc = "Terazi"
        ozellikler = ["Adil", "Zarif", "Sosyal"]
    elif (ay == 10 and gun >= 23) or (ay == 11 and gun <= 21):
        burc = "Akrep"
        ozellikler = ["Tutkulu", "Gizemli", "Kararli"]
    elif (ay == 11 and gun >= 22) or (ay == 12 and gun <= 21):
        burc = "Yay"
        ozellikler = ["Maceraci", "ozgur ruhlu", "iyimser"]
    elif (ay == 12 and gun >= 22) or (ay == 1 and gun <= 19):
        burc = "Oglak"
        ozellikler = ["Sorumlu", "Disiplinli", "Pratik"]
    #else:
        #print("Gecersiz bir giris yaptiniz, lutfen tekrar deneyin.")
        #continue

    print(f"\nBurcunuz: {burc}")
    print("Ozellikleriniz:")
    for ozellik in ozellikler:
        print(f"- {ozellik}")

    print("Programdan cikmak ister misiniz? E/H")
    cevap = input()
    if cevap == "E":
        break
    else:
        continue
