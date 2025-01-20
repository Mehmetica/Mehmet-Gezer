 elif secim == "3":
        musteri_id = input("Silmek istediğiniz müşterinin ID'sini giriniz: ")
        if musteri_id in musteriler:
            del musteriler[musteri_id]
            print("Müşteri başarıyla silindi!")
        else:
            print("Geçersiz müşteri ID!")