import json

# Başlangıçta film koleksiyonunu yüklemeye çalışıyoruz.
try:
    with open("filmler.json", "r") as dosya:
        koleksiyon = json.load(dosya)
        print("Kayıtlı film koleksiyonu yüklendi.")
except FileNotFoundError:
    koleksiyon = []
    print("Kaydedilmiş bir koleksiyon bulunamadı. Yeni bir koleksiyon oluşturuldu.")

while True:
    # Menü
    print("\nFilm Kütüphanesi")
    print("1. Film Ekle")
    print("2. Film Düzenle")
    print("3. Film Sil")
    print("4. Filmleri Listele")
    print("5. Çık ve Kaydet")

    secim = input("Bir seçenek girin: ")

    # Film Ekleme
    if secim == "1":
        isim = input("Film adı: ")
        yonetmen = input("Yönetmen: ")
        yil = input("Yayın yılı: ")
        tur = input("Tür: ")
        film = {"isim": isim, "yonetmen": yonetmen, "yil": yil, "tur": tur}
        koleksiyon.append(film)
        print("Film başarıyla eklendi!")

    # Film Düzenleme
    elif secim == "2":
        if not koleksiyon:
            print("Koleksiyon boş! Düzenlenecek film yok.")
            continue
        for i, film in enumerate(koleksiyon):
            print(f"{i}: {film['isim']} ({film['yil']}) - {film['tur']} - {film['yonetmen']}")
        indeks = int(input("Düzenlemek istediğiniz filmin numarasını girin: "))
        if 0 <= indeks < len(koleksiyon):
            print(f"Şu an düzenliyorsunuz: {koleksiyon[indeks]['isim']}")
            yeni_isim = input("Yeni film adı (boş bırakabilirsiniz): ")
            yeni_yonetmen = input("Yeni yönetmen adı (boş bırakabilirsiniz): ")
            yeni_yil = input("Yeni yayın yılı (boş bırakabilirsiniz): ")
            yeni_tur = input("Yeni tür (boş bırakabilirsiniz): ")
            if yeni_isim:
                koleksiyon[indeks]["isim"] = yeni_isim
            if yeni_yonetmen:
                koleksiyon[indeks]["yonetmen"] = yeni_yonetmen
            if yeni_yil:
                koleksiyon[indeks]["yil"] = yeni_yil
            if yeni_tur:
                koleksiyon[indeks]["tur"] = yeni_tur
            print("Film başarıyla güncellendi!")
        else:
            print("Geçersiz numara!")

    # Film Silme
    elif secim == "3":
        if not koleksiyon:
            print("Koleksiyon boş! Silinecek film yok.")
            continue
        for i, film in enumerate(koleksiyon):
            print(f"{i}: {film['isim']} ({film['yil']}) - {film['tur']} - {film['yonetmen']}")
        indeks = int(input("Silmek istediğiniz filmin numarasını girin: "))
        if 0 <= indeks < len(koleksiyon):
            silinen = koleksiyon.pop(indeks)
            print(f"Film silindi: {silinen['isim']}")
        else:
            print("Geçersiz numara!")

    # Film Listeleme
    elif secim == "4":
        if not koleksiyon:
            print("Koleksiyon boş!")
        else:
            for i, film in enumerate(koleksiyon):
                print(f"{i}: {film['isim']} ({film['yil']}) - {film['tur']} - {film['yonetmen']}")

    # Çık ve Kaydet
    elif secim == "5":
        with open("filmler.json", "w") as dosya:
            json.dump(koleksiyon, dosya)
        print("Veriler kaydedildi. Çıkış yapılıyor...")
        break

    # Geçersiz Seçim
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
