import random

# Bilgisayar rastgele bir sayı seçer (1 ile 100 arasında)
rastgele_sayi = random.randint(1, 100)
tahmin_hakki = 5

print("Sayı Tahmin Oyununa Hoş Geldiniz!")
print("1 ile 100 arasında bir sayı tahmin edin.")
print(f"{tahmin_hakki} tahmin hakkınız var.\n")

while tahmin_hakki > 0:
    # Kullanıcıdan tahmin al
    tahmin = int(input("Tahmininiz: "))

    # Tahmin doğruysa oyunu bitir
    if tahmin == rastgele_sayi:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    # Yanlış tahmin durumunda ipucu ver
    elif tahmin < rastgele_sayi:
        print("Daha büyük bir sayı girin.")
    else:
        print("Daha küçük bir sayı girin.")

    # Tahmin hakkını azalt
    tahmin_hakki -= 1
    print(f"Kalan tahmin hakkınız: {tahmin_hakki}\n")

    # Tahmin hakkı biterse
