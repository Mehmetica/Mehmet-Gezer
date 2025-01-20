gorevler = []
sonraki_sira_no = 1
bos_sira_nolari = []

def gorev_ekle(gorev_adi):
    global sonraki_sira_no
    if bos_sira_nolari:
        sira_no = bos_sira_nolari.pop(0)
    else: 
        sira_no = sonraki_sira_no
        sonraki_sira_no += 1
    
    gorev = {
        "Sira Numarasi": sira_no,
        "Gorev Adi": gorev_adi,
        "Durum": "Beklemede"
    }
    gorevler.append(gorev)
    print(f"Gorev '{gorev_adi}' basariyla eklendi.")

def gorev_tamamla(sira_no):
    for gorev in gorevler:
        if gorev["Sira Numarasi"] == sira_no and gorev["Durum"] == "Beklemede":
            gorev["Durum"] = "Tamamlandi"
            print(f"Gorev {sira_no} tamamlandi olarak isaretlendi.")
            return
    print(f"Gorev {sira_no} bulunamadi veya zaten tamamlanmis.")

def gorev_sil(sira_no):
    global bos_sira_nolari
    for gorev in gorevler:
        if gorev["Sira Numarasi"] == sira_no:
            gorevler.remove(gorev)
            bos_sira_nolari.append(sira_no)
            bos_sira_nolari.sort()
            print(f"Gorev {sira_no} basariyla silindi.")
            return
    print(f"Gorev {sira_no} bulunamadi.")

def tamamlanmis_gorevleri_listele():
    tamamlanmis_gorevler = [gorev for gorev in gorevler if gorev["Durum"] == "Tamamlandi"]
    if tamamlanmis_gorevler:
        print("\nTamamlanmis Gorevler:")
        for gorev in tamamlanmis_gorevler:
            print(f"{gorev['Sira Numarasi']}: {gorev['Gorev Adi']} (Tamamlandi)")
    else:
        print("Tamamlanmis gorev bulunamadi.")

def tum_gorevleri_listele():
    if gorevler:
        print("\nTum Gorevler:")
        for gorev in sorted(gorevler, key=lambda g: g["Sira Numarasi"]):
            print(f"{gorev['Sira Numarasi']}: {gorev['Gorev Adi']} ({gorev['Durum']})")
    else:
        print("Gorev bulunamadi.")

def ana_menu():
    while True:
        print("\nGorev Yonetici Menusu:")
        print("1. Yeni bir gorev ekle")
        print("2. Gorev tamamla")
        print("3. Gorev sil")
        print("4. Tamamlanmis gorevleri listele")
        print("5. Tum gorevleri listele")
        print("6. Cikis")

        secim = input("Bir secenek secin (1-6): ")

        if secim == "1":
            gorev_adi = input("Gorev adini girin: ")
            gorev_ekle(gorev_adi)
        elif secim == "2":
            sira_no = int(input("Tamamlanacak gorevin sira numarasini girin: "))
            gorev_tamamla(sira_no)
        elif secim == "3":
            sira_no = int(input("Silinecek gorevin sira numarasini girin: "))
            gorev_sil(sira_no)
        elif secim == "4":
            tamamlanmis_gorevleri_listele()
        elif secim == "5":
            tum_gorevleri_listele()
        elif secim == "6":
            print("Gorev Yonetici kapatiliyor. Hosca kalin!")
            break
        else:
            print("Gecersiz secenek. Lutfen 1 ile 6 arasinda bir secim yapin.")

if __name__ == "__main__":
    ana_menu()

def tum_gorevleri_listele():
    if gorevler:
        print("\nTum Gorevler:")
        for gorev in sorted(gorevler, key=lambda g: g["Sira Numarasi"]):
            print(f"{gorev['Sira Numarasi']}: {gorev['Gorev Adi']} ({gorev['Durum']})")
    else:
        print("Gorev bulunamadi.")

def ana_menu():
    while True:
        print("\nGorev Yonetici Menusu:")
        print("1. Yeni bir gorev ekle")
        print("2. Gorev tamamla")
        print("3. Gorev sil")
        print("4. Tamamlanmis gorevleri listele")
        print("5. Tum gorevleri listele")
        print("6. Cikis")

        secim = input("Bir secenek secin (1-6): ")

        if secim == "1":
            gorev_adi = input("Gorev adini girin: ")
            gorev_ekle(gorev_adi)
        elif secim == "2":
            sira_no = int(input("Tamamlanacak gorevin sira numarasini girin: "))
            gorev_tamamla(sira_no)
        elif secim == "3":
            sira_no = int(input("Silinecek gorevin sira numarasini girin: "))
            gorev_sil(sira_no)
        elif secim == "4":
            tamamlanmis_gorevleri_listele()
        elif secim == "5":
            tum_gorevleri_listele()
        elif secim == "6":
            print("Gorev Yonetici kapatiliyor. Hosca kalin!")
            break
        else:
            print("Gecersiz secenek. Lutfen 1 ile 6 arasinda bir secim yapin.")

