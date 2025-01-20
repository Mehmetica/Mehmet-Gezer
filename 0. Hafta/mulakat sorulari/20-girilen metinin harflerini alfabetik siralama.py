
# Kullanıcıdan metin al
girdi = input("Bir metin giriniz: ")

# Metni kelimelere ayır
kelimeler = girdi.split()

# Her kelimenin harflerini elle sırala
siralanmis_kelimeler = []

for kelime in kelimeler:
    harfler = list(kelime)
    n = len(harfler)

    # Basit bir seçim sıralaması implementasyonu
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if harfler[j] < harfler[min_index]:
                min_index = j
        # Harf değişimi
        harfler[i], harfler[min_index] = harfler[min_index], harfler[i]

    siralanmis_kelimeler.append(''.join(harfler))

# Yeni metin oluştur
yeni_metin = ' '.join(siralanmis_kelimeler)

# Sonucu yazdır
print("Harfleri sıralanmış metin:", yeni_metin)

