faktoriyel=1

while True:
     sayi=int(input("pozitif bir sayi giriniz: "))
     if (sayi <= 0):
         print("pozitif bir sayi giriniz")
     else:
         for i in range(1, sayi+1):# sayi 3 girildi ancak for dongusu son sayiyi dahil etmedigi icin sayi+1 seklinde yazarak 3 sayisini da carptik boylece
             faktoriyel= faktoriyel*i

         print(sayi,"faktoryel degeri:",faktoriyel)
         break


