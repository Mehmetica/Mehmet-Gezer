import random

# Önceden belirlenmiş kelime listesi
kelimeler = ["elma", "python", "araba", "bilgisayar", "programlama"]
rastgele_kelime = random.choice(kelimeler)

# Oyuncunun göreceği boşluklar (örn: "_ _ _ _ _ _")
kelime_tahmin = ["_"] * len(rastgele_kelime)
yanlis_tahmin_hakki = 6
tahmin_edilen_harfler = []

print("Kelime Tahmin Oyunu - Adam Asmaca'ya Hoş Geldiniz!")
print(f"Kelime {len(rastgele_kelime)} harften oluşuyor.")
print(" ".join(kelime_tahmin))
print(f"{yanlis_tahmin_hakki} yanlış tahmin hakkınız var.\n")

while yanlis_tahmin_hakki > 0:
    harf = input("Bir harf tahmin edin: ").lower()

    # Eğer harf zaten tahmin edildiyse uyarı ver
    if harf in tahmin_edilen_harfler:
        print("Bu harfi zaten tahmin ettiniz! Başka bir harf deneyin.")
        continue

    tahmin_edilen_harfler.append(harf)

    # Doğru harf tahmin edildiğinde
    if harf in rastgele_kelime:
        for i in range(len(rastgele_kelime)):
            if rastgele_kelime[i] == harf:
                kelime_tahmin[i] = harf
        print("\nDoğru tahmin!")
    else:
        # Yanlış harf tahmini olduğunda hakları azalt
        yanlis_tahmin_hakki -= 1
        print("\nYanlış tahmin!")

    # Kelimenin şu anki durumu ve kalan haklar
    print(" ".join(kelime_tahmin))
    print(f"Kalan tahmin hakkınız: {yanlis_tahmin_hakki}\n")

    # Tüm harfler doğru tahmin edilmişse oyun biter
    if "_" not in kelime_tahmin:
        print("Tebrikler! Kelimeyi doğru tahmin ettiniz.")
        break

# Oyuncunun tüm tahmin hakları bittiyse
if yanlis_tahmin_hakki == 0:
    print(f"Üzgünüm, kaybettiniz. Doğru kelime: {rastgele_kelime}")
