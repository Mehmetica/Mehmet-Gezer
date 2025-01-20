musteriler = {}

while True:
    print("\nMüşteri Yönetim Sistemi")
    print("1. Müşteri Ekle")
    print("2. Müşteri Güncelle")
    print("3. Müşteri Sil")
    print("4. Müşteri Listele")
    print("5. Çıkış")

    secim = input("Bir işlem seçiniz (1-5): ")

    if secim == "1":
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

    elif secim == "2":
        musteri_id = input("Güncellemek istediğiniz müşterinin ID'sini giriniz: ")
        if musteri_id in musteriler:
            print("Mevcut Müşteri Bilgileri:", musteriler[musteri_id])
            isim = input(f"Yeni isim (eski: {musteriler[musteri_id]['isim']}): ")
            soyad = input(f"Yeni soyad (eski: {musteriler[musteri_id]['soyad']}): ")
            email = input(f"Yeni e-posta (eski: {musteriler[musteri_id]['email']}): ")
            telefon = input(f"Yeni telefon (eski: {musteriler[musteri_id]['telefon']}): ")

            if isim:
                musteriler[musteri_id]["isim"] = isim
            if soyad:
                musteriler[musteri_id]["soyad"] = soyad
            if email:
                musteriler[musteri_id]["email"] = email
            if telefon:
                musteriler[musteri_id]["telefon"] = telefon

            print("Müşteri bilgileri başarıyla güncellendi!")
        else:
            print("Geçersiz müşteri ID!")

    elif secim == "3":
        musteri_id = input("Silmek istediğiniz müşterinin ID'sini giriniz: ")
        if musteri_id in musteriler:
            del musteriler[musteri_id]
            print("Müşteri başarıyla silindi!")
        else:
            print("Geçersiz müşteri ID!")

    elif secim == "4":
        if musteriler:
            print("Tüm Müşteriler:")
            for musteri_id, bilgiler in musteriler.items():
                print(f"ID: {musteri_id} - İsim: {bilgiler['isim']} {bilgiler['soyad']} - E-posta: {bilgiler['email']} - Telefon: {bilgiler['telefon']}")
        else:
            print("Hiç müşteri bulunmamaktadır.")

    elif secim == "5":
        
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin!")
