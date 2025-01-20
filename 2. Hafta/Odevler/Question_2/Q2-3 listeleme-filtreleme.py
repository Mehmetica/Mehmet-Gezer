koleksiyon = [
    {"isim": "adana", "yonetmen": "mehmet", "yil": "1988", "tur": "aksiyon"},
    {"isim": "urfa", "yonetmen": "ahmet", "yil": "1986", "tur": "gerilim"},
    {"isim": "sivas", "yonetmen": "ayse", "yil": "2001", "tur": "suc"}
]

for i, movie in enumerate(koleksiyon):
    print(f"{i}: {movie['isim']} ({movie['yil']}) - {movie['tur']} by {movie['yonetmen']}")

print("--------------------------------------")

criteria = input("Yıla göre mi Tür'e göre mi filtrelemek istersiniz? : Y - T").lower()

if criteria == "t":
    genre = input("İstediğiniz türü giriniz: ")
    filtered = [movie for movie in koleksiyon if movie["tur"].lower() == genre.lower()]

elif criteria == "y":
    year = input("İstediğiniz yılı giriniz: ")
    filtered = [movie for movie in koleksiyon if movie["yil"] == year]

else:
    print("Geçersiz giriş!")
    filtered = []

if filtered:
    print("\nFiltrelenmiş Filmler:")
    for movie in filtered:
        print(f"{movie['isim']} ({movie['yil']}) - {movie['tur']} by {movie['yonetmen']}")
else:
    print("Hiçbir film bulunamadı.")
