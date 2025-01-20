"""cumle="  ali ve veli   "

print(cumle.count("a"))

print(cumle.find("i"))

print(cumle.replace("ali","mehmet"))

print(cumle.strip(" "))

a="5"
if a.isdigit():
    print("True")"""
#-----------------------------------------------------------------------
"""elma=3
muz=5

if muz>elma:
    print("Muz,elma dan pahalidir")
elif muz==elma:
    print("Muz ve elma ayni fiyattir")
else:
    print("Muz, elma dan ucuzdur")"""

#-----------------------------------------------------------------------

"""sayi= int(input("Cektiginiz sayiyi giriniz: "))
if sayi==1:
    print("Kazandiniz!!!")
else:
    print("Kumar haramdir:(")"""
#-----------------------------------------------------------------------

"""sayi1=int(input("1. sayiyi giriniz: "))
sayi2=int(input("2. sayiyi giriniz: "))

if sayi1%sayi2==0 or sayi2%sayi1==0:
    print("tam bolunuyor")
else:
    print("Tam bolunmez!")"""
    
#-----------------------------------------------------------------------

"""sayi=int(input("Bir sayi giriniz: "))

if sayi<0:
    print("Sayi negatiftir")
elif sayi>0:
    print(" Sayi pozitiftir")
else :
    print(" Sayi sifirdir")"""

#-----------------------------------------------------------------------
"""dizi=[]
for i in range(3):
    sayi=int(input(f" {i+1}. sayi giriniz: "))
    dizi.append(sayi)

dizi.sort
print(dizi[1])

"""

"""a=int(input("1. sayiyi giriniz: "))
b=int(input("2. sayiyi giriniz: "))
c=int(input("3. sayiyi giriniz: "))

if b>a>c or c>a>b:
    print(f"Medyan: {a} ")
elif a>b>c or c>b>a:
    print(f"Medyan: {b} ")
else:
    print(f"Medyan: {c} ")"""


#-----------------------------------------------------------------------

"""for i in range(10):
    pass #hata vermemesi icin kullanilir
else:
    print("asfdafdasf")"""
#----------------------------------------------------------------------- 

"""liste=[19,34,62,93]

sayi =int(input("Bir sayi giriniz: "))

for i in liste:
    if sayi>i:
        print(f" {sayi} > {i}")
    elif sayi<i:
        print(f" {sayi} < {i}")
    else:
        print(f" {sayi} = {i}")"""

#-----------------------------------------------------------------------

"""sayi= int ( input("Bir sayi giriniz: "))

for i in range (1,11):
    print(f" {i} x {sayi} = {i*sayi}")"""
#-----------------------------------------------------------------------

#kelime = input(" Bir kelime giriniz: ")

"""uzunluk=len(kelime)
i=0

while i<uzunluk:
    print(kelime[i])
    i+=1"""

""""""
#-----------------------------------------------------------------------

"""i=1
sayi=5

while True:
    tahmin=int(input("1-10 arasinda bir sayi giriniz: "))
    if tahmin< sayi:
        print("Daha buyuk bir sayi giriniz: ")
    elif tahmin>5:
        print("Daha kucuk bir sayi giriniz: ")
    else:
        print("Dogru tahmin!")
        break
    i+=1
print(f"{i} . seferde buldunuz!")"""
#-----------------------------------------------------------------------

"""for i in range(1,101):
    if i%3==0 and i%4==0:
        print(i)
"""

#-----------------------------------------------------------------------

'''sayi = int(input("Bir sayi giriniz: "))

bolenler=[]

for i in range(sayi,0,-1):
    if sayi%i==0:
        bolenler.append(i)

print(bolenler)'''

#-----------------------------------------------------------------------

"""sayi1=int(input("1. sayiyi giriniz: "))
sayi2=int(input("2. sayiyi giriniz: "))

tekler,ciftler=0,0


if sayi1==sayi2:
    print('Farkli iki sayi giriniz: ')
    sayi1=int(input("1. sayiyi giriniz: "))
    sayi2=int(input("2. sayiyi giriniz: "))

if sayi1>sayi2:
    for i in range(sayi2,sayi1+1):
        if i%2==0:
            ciftler+=i
        else:
            tekler+=i

if sayi1<sayi2:
    for i in range(sayi1,sayi2+1):
        if i%2==0:
            ciftler+=i
        else:
            tekler+=i

print(f"Tek sayilar toplami: {tekler}\nCift sayilar toplami: {ciftler}")"""

#-----------------------------------------------------------------------




