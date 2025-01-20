cumle= input(" Bir cumle giriniz: ")
harf= input("Bir harf giriniz: ")

tekrar_sayisi=0

for i in cumle:
    if i==harf:
        tekrar_sayisi+=1

print("Cumlenizde",harf,"tekrar eden sayi:",tekrar_sayisi)