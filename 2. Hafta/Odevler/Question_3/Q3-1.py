musteriler={}
musteri_id = input("Müşteri ID'sini giriniz: ")

if musteri_id in musteriler:
    print("Bu müşteri zaten mevcut!")
else:
    isim = input("Müşterinin adını giriniz: ")
    soyad = input("Müşterinin soyadını giriniz: ")
    email = input("Müşterinin e-posta adresini giriniz: ")
    telefon = input("Müşterinin telefon numarasını giriniz: ")

    musteriler[musteri_id] = {
        "isim": isim,
        "soyad": soyad,
        "email": email,
        "telefon": telefon
    }
    print(f"{isim} {soyad} başarıyla eklendi!")