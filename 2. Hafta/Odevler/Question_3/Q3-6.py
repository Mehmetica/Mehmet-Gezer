elif secim == "4":
        if musteriler:
            print("Tüm Müşteriler:")
            for musteri_id, bilgiler in musteriler.items():
                print(f"ID: {musteri_id} - İsim: {bilgiler['isim']} {bilgiler['soyad']} - E-posta: {bilgiler['email']} - Telefon: {bilgiler['telefon']}")
        else:
            print("Hiç müşteri bulunmamaktadır.")