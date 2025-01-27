class Kitap:
    kitap_sayisi=0
    sayfa_sayisi=0

   

    def __init__(self,baslik,yazar,sayfa_sayisi,tur):
        self.baslik=baslik
        self.yazar=yazar
        self.sayfa_sayisi=sayfa_sayisi
        self.tur=tur
        Kitap.kitap_sayisi+=1
        Kitap.sayfa_sayisi+=self.sayfa_sayisi

    def kitap_sayfa_sayisi_guncelle(self,sayfa):
        Kitap.sayfa_sayisi=Kitap.sayfa_sayisi-self.sayfa_sayisi+sayfa
        self.sayfa_sayisi=sayfa
        print(f"{self.baslik} kitabinin sayfa sayisi guncellendi, yeni sayfa sayisi: {self.sayfa_sayisi}\ntoplam sayfa sayisi: {Kitap.sayfa_sayisi}, toplam kitap sayisi: {Kitap.kitap_sayisi}")

kitap1=Kitap("ahmet","kemal",100,"Korku")
kitap2=Kitap("mehmet","osman",200,"macera")
kitap1=Kitap("oguz","kursat",550,"ask")

print(f"toplam kitap sayisi: {Kitap.kitap_sayisi}")
print(f"toplam sayfa sayisi: {Kitap.sayfa_sayisi}")
kitap1.kitap_sayfa_sayisi_guncelle(500)