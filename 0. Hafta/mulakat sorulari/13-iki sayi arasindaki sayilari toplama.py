from pickle import PROTO

sayi1=input("1. sayiyi giriniz: ")
sayi2= input("2. sayiyi giriniz: ")
toplam=0
ara_sayilar=[]

for i in range(int(sayi1)+1,int(sayi2)):
    ara_sayilar.append(i)
    toplam+=i

print("ara sayilar: ", ara_sayilar)
print(sayi1, " ile", sayi2, " arasindaki sayilarin toplami: ", toplam)
