dizi1= input("birinci diziyi girin aralarinda bozluk olsun: ").split()
dizi2= input("ikinci diziyi girin aralarinda bozluk olsun: ").split()

ortak_elemanlar=[]

for eleman in dizi1:
    if eleman in dizi2 and eleman not in ortak_elemanlar:
        ortak_elemanlar.append(eleman)

print(ortak_elemanlar)