sayi=int(input("sayi giriniz: "))
us=int(input("kacinci derecesini almak istiyorsunuz? : "))

sonuc=1

for i in range(us):
    sonuc *= sayi
    i+=1

print(f"{sayi} uzeri {us} = {sonuc} ")

