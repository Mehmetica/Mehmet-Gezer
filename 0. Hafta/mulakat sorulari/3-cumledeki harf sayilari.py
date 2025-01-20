cumle=input("Bir cumle giriniz: ")

harfler_dizisi=[]
adet_dizisi=[]

for harf in cumle:
    if harf not in harfler_dizisi:
        harfler_dizisi.append(harf)
        adet_dizisi.append(1)
    else:
        yer=harfler_dizisi.index(harf)
        adet_dizisi[yer]+=1

for i in range(len(harfler_dizisi)):
    print(f"{harfler_dizisi[i]} : {adet_dizisi[i]}")

