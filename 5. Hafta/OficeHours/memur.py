class Memur:
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def bilgileri_goster(self):
        print(f"Benim adim {self.ad}, soyadim {self.soyad} ve maasim {self.maas} USD'dir")

class Yonetici(Memur):
    def __init__(self, ad, soyad, maas, departman):
        super().__init__(ad, soyad, maas)
        self.departman = departman

class Stajer(Memur):
    def __init__(self, ad, soyad, egitim):
        super().__init__(ad, soyad, 1000)
        self.egitim = egitim

s1 = Stajer("ali", "kemal", "egitim")
print(s1.egitim)  