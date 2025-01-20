koleksiyon = [
    {"isim": "adana", "yonetmen": "mehmet", "yil": "1988", "tur": "aksiyon"},
    {"isim": "urfa", "yonetmen": "ahmet", "yil": "1986", "tur": "gerilim"},
    {"isim": "sivas", "yonetmen": "ayse", "yil": "2001", "tur": "suc"}
]

while True:
    
    print("\nFilm koleksiyonu:")
    for i, film in enumerate(koleksiyon):
        print(f"{i}: {film['isim']} ({film['yil']}) - {film['tur']} - {film['yonetmen']}")
    
    cevap = input("\nFilmleri silmek için 'S'; düzenlemek için 'D'; çıkmak için 'Q' tuşlayın: ").lower()

    if cevap == "d":
        indeks = int(input("Düzenlemek istediğiniz filmin numarasını girin: "))

        if 0 <= indeks < len(koleksiyon):
            secilen_film = koleksiyon[indeks]
            print(f"Seçilen film: {secilen_film}")

            yeni_isim = input(f"Yeni film adı (eski: {secilen_film['isim']}): ")
            yeni_yonetmen = input(f"Yeni yönetmen adı (eski: {secilen_film['yonetmen']}): ")
            yeni_yil = input(f"Yeni yayın yılı (eski: {secilen_film['yil']}): ")
            yeni_tur = input(f"Yeni tür (eski: {secilen_film['tur']}): ")

            if yeni_isim:
                secilen_film["isim"] = yeni_isim
            if yeni_yonetmen:
                secilen_film["yonetmen"] = yeni_yonetmen
            if yeni_yil:
                secilen_film["yil"] = yeni_yil
            if yeni_tur:
                secilen_film["tur"] = yeni_tur

            print("Film başarıyla güncellendi!")
        else:
            print("Geçersiz numara!")

    elif cevap == "s":
        indeks = int(input("Silmek istediğiniz filmin numarasını girin: "))
        if 0 <= indeks < len(koleksiyon):
            silinen = koleksiyon.pop(indeks)
            print(f"Film silindi: {silinen['isim']}")
        else:
            print("Geçersiz numara!")

    elif cevap == "q":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen 'S', 'D' veya 'Q' girin.")
