sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tek ve çift sayı toplamları için değişkenler
tek_toplam = 0
cift_toplam = 0

# Listedeki sayıları kontrol et
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_toplam += sayi
    else:
        tek_toplam += sayi

# Sonuçları ekrana yazdır
print("Tek sayıların toplamı:", tek_toplam)
print("Çift sayıların toplamı:", cift_toplam)
