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