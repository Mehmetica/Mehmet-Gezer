"""veri_listesi = [56, 'rmzoe', 86, 97, 'icwxm', 'mpcsn', 'lbgoa', 48, 'qdvch', 'sgzbd', 'ukedp', 32, 41, 'yhkji', 68, 'vnmwt', 52, 'knawt', 53, 74]

# Sayıları filtrele
sayi_listesi = [eleman for eleman in veri_listesi if isinstance(eleman, int)]

# En büyük ve en küçük sayıları bul
en_buyuk = max(sayi_listesi)
en_kucuk = min(sayi_listesi)

print("En büyük sayı:", en_buyuk)
print("En küçük sayı:", en_kucuk)

"""



veri_listesi=["dfasdfsd",232,45,3,67,"fsf",'dfss',56]
yeni_liste=[]
for a in veri_listesi:
    if type(a)==int:
        yeni_liste.append(a)
print(yeni_liste)

max=yeni_liste[0]
min=yeni_liste[0]

for b in yeni_liste:
    if b>max:
        max=b
    if b<min:
        min=b

print("\nmax sayi= ", max, "\nmin sayi= ", min)


"""veri_listesi = [56, 'rmzoe', 86, 97, 'icwxm', 'mpcsn', 'lbgoa', 48, 'qdvch', 'sgzbd', 'ukedp', 32, 41, 'yhkji', 68, 'vnmwt', 52, 'knawt', 53, 74]

# Sayıları filtrelemek için boş bir liste oluştur
sayi_listesi = []

# Listedeki her elemanı kontrol et
for eleman in veri_listesi:
    if isinstance(eleman, int):  # Eğer eleman bir tamsayıysa
        sayi_listesi.append(eleman)

# En büyük ve en küçük sayıları bul
en_buyuk = sayi_listesi[0]
en_kucuk = sayi_listesi[0]

# Listedeki her sayıyı kontrol et
for sayi in sayi_listesi:
    if sayi > en_buyuk:
        en_buyuk = sayi
    if sayi < en_kucuk:
        en_kucuk = sayi

print("En büyük sayı:", en_buyuk)
print("En küçük sayı:", en_kucuk)

"""
