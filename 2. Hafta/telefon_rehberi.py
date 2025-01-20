import os

rehber={
    "mehmet":"234243242",
    "ali":"3432454252523",
} 

def ekle():
    ad=input("Isim:").lower()
    tel=input("Telefon:")
    rehber.update({ad:tel})
    print("Kisi eklendi")
def ara():
    ad=input("Isim: ").lower()
    if ad in rehber:
        print(rehber.get(ad))
    else:
        print("Bu kisi rehberinizde bulunmuyor...")


def sil():
    ad=input("Isim:").lower()
    if ad in rehber:    
        rehber.pop(ad)
        print(ad," kisisi silindi")
    else:
        print("Rehberde bu kisi mevcut degil!")


def liste():
    for x,y in rehber.items():
        print(f"isim: {x} telefon: {y}")

while True:
    os.system("clear")#ekrani temizleme 
    print("""
    Telefon Rehberi
    Ekle - 1
    Ara - 2
    Sil - 3
    Liste - 4
    """)
    sec=input("Lutfen Seciniz: ")

    if sec=="1":
        ekle()
    elif sec=="2":
        ara()
    elif sec=="3":
        sil()
    elif sec=="4":
        liste()
    else:
        print("Hatalı Seçim")
    print(input("Devam etmek icin enter'a basin")) 




