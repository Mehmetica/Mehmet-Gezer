girdi= input("Bir dizi sayi giriniz ve aralrinda bosluk birakiniz: ").split()

toplam=0


for i in girdi:
    toplam+=float(i)
ortalama= toplam/len(girdi)

print("ortalama: ", ortalama)