class Kitap:
    dil = "Turkce"

    def __init__(self, yazar, baslik, sayfa_sayisi):
        self.yazar = yazar
        self.baslik = baslik
        self.sayfa_sayisi = sayfa_sayisi

    def bilgileri_goster(self):
        print(f"\n'Kitabin yazari'= {self.yazar}\n'Kitabin Basligi'={self.baslik}\n'Kitabin sayfa sayisi'= {self.sayfa_sayisi}")
        

# kitap1.bilgileri_goster()

    def sayfa_ekle(self, eklenecek_sayfa):
        self.sayfa_sayisi=+eklenecek_sayfa
        print(f"{self.yazar} kitabina {eklenecek_sayfa} kadar sayfa eklendi, yeni sayfa sayisi= {self.sayfa_sayisi}")

    def sayfa_cikar(self,cikarilacak_sayi):
        try:
            if(self.sayfa_sayisi>=cikarilacak_sayi):
                self.sayfa_sayisi-=cikarilacak_sayi
                print(f" {cikarilacak_sayi} kadar sayfa silindi, sayfa sayisi= {self.sayfa_sayisi}")
            
            else:
                print("Bu kadar sayfa yok!")
        except Exception as error:
            print(error)
    


kitap1= Kitap("ali", "ataman", 345)
kitap2= Kitap("kemal", "george", 445)
kitap3= Kitap("mehmet", "faruk", 566)

kitap1.sayfa_cikar(30)
kitap2.bilgileri_goster()
kitap3.sayfa_ekle(44)


