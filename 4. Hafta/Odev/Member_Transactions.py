import json
import uuid  
import Zaman
import Kitap_transactions


dosya_adi = "uye.json"

def sira_numarasi_ver():
        kullanici_id = int(uuid.uuid4())
        data=dosyayi_yukle_veya_olustur()
        while True:
            if kullanici_id in data["ID"]:
                kullanici_id = int(uuid.uuid4())
            else:
                return kullanici_id
            
                




def dosyayi_yukle_veya_olustur(file_name):
    try:
        with open(file_name, "r") as dosya:
            return json.load(dosya)  
    except FileNotFoundError:
        return []  


def kayit_bilgiler_al():
    print("Kayıt İçin Gerekli Bilgiler:")
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    dogum_tarihi = input("Doğum Tarihi (gun/ay/yil): ")
    kullanici_id = int(uuid.uuid4())

   
    kullanici = {
        "ID": kullanici_id,
        "isim": isim,
        "soyisim": soyisim,
        "dogum_tarihi": dogum_tarihi,
        "uyelik_tarihi": Zaman.eklenme_tarihi()
    }

    return kullanici

def add_member(kullanici):
    kayitlar = dosyayi_yukle_veya_olustur("uye.json")  # Mevcut kayıtları yükle
    kayitlar.append(kullanici)  # Yeni kullanıcıyı ekle

    # Güncellenmiş kayıtları dosyaya yaz
    with open(dosya_adi, "w") as dosya:
        json.dump(kayitlar, dosya, indent=4)

    print(f"{kullanici['isim']} {kullanici['soyisim']} başarıyla kaydedildi.")
    print(f"Kullanıcı ID'si: {kullanici['ID']}")


def list_member():
    kayitlar = dosyayi_yukle_veya_olustur("uye.json")
    if not kayitlar:
        print("Henüz kayıtlı bir kullanıcı yok.")
    else:
        print("Kayıtlı Kullanıcılar:")
        for kullanici in kayitlar:
            print(f"ID: {kullanici['ID']}, İsim: {kullanici['isim']}, Soyisim: {kullanici['soyisim']}, Doğum Tarihi: {kullanici['dogum_tarihi']}, Uyelik Tarihi: {kullanici["uyelik_tarihi"]}")




def delete_member():
    silinecek_uye_id = int(input("Silmek istediğiniz üyenin ID'sini girin: "))
    


    with open("uye.json", 'r+') as file:
        try:
            uyeler = json.load(file)
        except json.JSONDecodeError:
            uyeler = []

        

        # Filtreleme işlemi: ID eşleşen üyeyi kaldır
        yeni_uyeler = [uye for uye in uyeler if uye["ID"] != silinecek_uye_id]

        if len(uyeler) == len(yeni_uyeler):
            print(f"Üye bulunamadı: Ad:  ID : {silinecek_uye_id}")
            return

        # Üye bulunduysa, yeni veriyi dosyaya kaydet
        file.seek(0)  # Dosya başına git
        file.truncate()  # Eski veriyi sil
        json.dump(yeni_uyeler, file, indent=4)
        print(f"Üye başarıyla silindi: ID: {silinecek_uye_id}")
    


def check_member():
    pass


def get_member_info():
    Barkod = int(input("Ödünç verilecek kitabın barkod numarasını giriniz: "))
    ID = input("Üye numarasını giriniz: ")
    Isim_Soyisim = input("İsim-Soyisim giriniz: ")

    odunc_verilen = {
        "Barkod": Barkod,
        "ID": ID,
        "Isim-Soyisim": Isim_Soyisim,
        "Kitabin odunc verildigi tarih": Zaman.eklenme_tarihi(),
        "Kitabin geri alinacagi tarih": Zaman.iade_tarihi()
    }
    
    return odunc_verilen

def search_book(uye):
    Barkod = uye["Barkod"]
    try:
        with open("taksi.json", 'r') as file:
            taksi = json.load(file)
            if not isinstance(taksi, list):
                raise ValueError("taksi.json bir liste içermelidir.")
            for i in taksi:
                if i["Barkod"] == Barkod:
                    print("Bu kitap daha önce ödünç verildiği için kütüphanemizde mevcut değil!")
                    return True  # Kayıt bulunduğunda döngüden çık
    except json.JSONDecodeError:
        print("taksi.json dosyası düzgün bir JSON formatında değil.")
    except FileNotFoundError:
        print("taksi.json dosyası bulunamadı.")
    return False


def give_book(uye):
    Barkod = uye["Barkod"]

    # Kitap kütüphanede mevcut mu kontrol et
    if search_book(uye):
        return

    try:
        # Kitap.json dosyasını yükle ve barkod numarası ile kitabı sil
        kitaplar = dosyayi_yukle_veya_olustur("kitap.json")
        kitaplar = list(filter(lambda kitap: kitap["Barkod"] != Barkod, kitaplar))
        
        # Güncellenmiş kitaplar listesini kitap.json'a yaz
        with open("kitap.json", "w") as dosya:
            json.dump(kitaplar, dosya, indent=4)
        
        print("Kitap kütüphaneden başarıyla silindi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return

    # Taksi.json dosyasına yeni kayıt ekle
    taksi = dosyayi_yukle_veya_olustur("taksi.json")
    taksi.append(uye)
    with open("taksi.json", "w") as dosya:
        json.dump(taksi, dosya, indent=4)
    
    print("Kitap başarı ile ödünç verildi!")

    
   
    

def receive_book():
    pass

def members_book():
    pass





