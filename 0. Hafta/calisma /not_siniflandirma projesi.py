import random

def not_siniflandirma():
    print("Rastgele Not Sınıflandırma Sistemine Hoşgeldiniz!")

    # Öğrenciler için rastgele 10 adet not üretiyoruz
    ogrenciler = []
    for i in range(10):
        not_ = random.randint(0, 100)  # 0 ile 100 arasında rastgele bir not
        ogrenciler.append(not_)

    print("\nÜretilen Notlar:")
    print(ogrenciler)

    # Her notu sınıflandırıyoruz
    for i, not_ in enumerate(ogrenciler):
        print(f"\nÖğrenci {i+1} Notu: {not_} - ", end="")

        if not_ >= 90:
            print("A (Mükemmel)")
        elif not_ >= 80:
            print("B (İyi)")
        elif not_ >= 70:
            print("C (Ortalama)")
        elif not_ >= 60:
            print("D (Geçer)")
        else:
            print("F (Başarısız)")

    # Geçen öğrenci sayısını hesaplayalım
    gecenler = 0
    for not_ in ogrenciler:
        if not_ >= 60:
            gecenler += 1

    print(f"\nToplam Geçen Öğrenci Sayısı: {gecenler}")
    print(f"Toplam Başarısız Öğrenci Sayısı: {len(ogrenciler) - gecenler}")

# Programı çalıştırıyoruz
not_siniflandirma()
