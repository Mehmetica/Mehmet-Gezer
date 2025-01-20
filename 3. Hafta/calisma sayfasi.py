# konu anlatimi alistirmalari

# def yazdir(kelime):
#     print(kelime)


# yazdir(input("Bir kelime giriniz: "))
# #-------------------------------------

# def asal_bul(sayi1,sayi2):
#     asal_sayilar= [x for x in range(sayi1,sayi2+1) if x%2!=0]
#     for i in asal_sayilar:
#         print(i,end=(","))

# sayi1=int(input("Birinci sayiyi giriniz: "))
# sayi2=int(input("Ikinci sayiyi giriniz: "))
# asal_bul(sayi1,sayi2)
#-------------------------------------

# def saniye_bul(saat):
#     print(f"{saat} saat icinde {saat*3600} saniye vardir")

# saat=int(input("Kac saat icinde kac saniye oldugunu merak ediyorsunuz?: "))
# saniye_bul(saat)

#-------------------------------------
# def ders_notu_hesapla(vize, final):
#     ortalama = (vize * 0.40) + (final * 0.60)
    
#     if ortalama >= 85:
#         return "AA"
#     elif ortalama >= 70:
#         return "BB"
#     elif ortalama >= 55:
#         return "CC"
#     elif ortalama >= 45:
#         return "DD"
#     else:
#         return "FF"

# mat_vize = float(input("Matematik Vize Notu: "))
# mat_final = float(input("Matematik Final Notu: "))
# fizik_vize = float(input("Fizik Vize Notu: "))
# fizik_final = float(input("Fizik Final Notu: "))
# kimya_vize = float(input("Kimya Vize Notu: "))
# kimya_final = float(input("Kimya Final Notu: "))

# print(f"Matematik: {ders_notu_hesapla(mat_vize, mat_final)}")
# print(f"Fizik: {ders_notu_hesapla(fizik_vize, fizik_final)}")
# print(f"Kimya: {ders_notu_hesapla(kimya_vize, kimya_final)}")

#-------------------------------------
# def karesini_al(x):
    # return x**2


# sayilar=[*range(1,6)]
# print(sayilar)
# for index in range(len(sayilar)):
#     sayilar[index]=karesini_al(sayilar[index])

# print(sayilar)
#-------------------------------------

#map istenen fonsksiyonu listenini her elemanina uygulamak icin bir kisaayol gibi
# sonuc = [*map(karesini_al, sayilar)]  # map i listeye cevirdik ki yazdirabilelim, yoksa sadece olusturuluyor ve yazdiramiyoruz
# print(sonuc)
#-------------------------------------

#filtre de, map gibi hepsine degil de belirlenen ozellikteki elemanlara uygulanmasini istiyorsak kullanilir
# sayilar=[*range(1,6)]

# def cift_sayilari_filtrele(x):
#     if x&2==0:
#         return x
    
#ya da bu sekilde daha pro yazabiliriz
# def cift_sayilari_filtrele(x):
#     return x if x%2==0 else None
    
# result=cift_sayilari_filtrele(3)
# print(result)

# bu kodu filtre ile yazarsak:
# sonuc=[*filter(cift_sayilari_filtrele,sayilar)]
# print(sonuc)
#-------------------------------------
# lambda kullanarak:

# sayilar=[*range(1,6)]
# sonuc=list(map(lambda x: x**2, sayilar)) #veya [* ....] ile de liste cevirebilrdik
# print(sonuc)

#-------------------------------------
#lambda sadece map da degil filtre de de kullanilabilir

# sayilar=[*range(1,6)]
# sonuc=[*filter(lambda x : x if x%2==0 else None, sayilar)]
# print(sonuc)

#-------------------------------------

#youtube lambda ornek

#lambda yi hizli bir sekilde def yazmak yerine de kullanabiliriz, tek satirlik genel bir fonksiyondur.
# lambda x: x**2 demek : xi alir ve : sonrasindaki islemi yapar ve return eder
# tek kullanumlik fonksiyondur, def i tekrar cagirabiliriz ama lambda tek sefer

# nums=[3,4,5,6,7]

# def my_map(my_func, my_iter): # burda def bir fonsiyon ve iterable(liste,,sozluk vs) aliyor.
#     result=[]
#     for item in my_iter:
#         new_item= my_func(item)
#         result.append(new_item)
#     return(result)

# cubed=my_map(lambda x: x**3,nums) # burda my_map fonk cagirdik ve icinde kullancagi fonksiyonu ve dondurulebilir listeyi verdik. 
# #lambda ile basit bir fonksiyon yazmis olduk
# print(cubed)

#-------------------------------------

# youtube 2

# add_1= lambda x: x+1
# result=add_1(4)
# print(result)

#-------------------------------------

# def add_1_def_ile(x,y):# bunu lambda ile tek satirda yapabiliyoruz. tekrar tekrar kullancaksak def daha mantikli
#     return x+y

# add_1= lambda x,y: x+y
# result=add_1(4,5)
# print(result)
#-------------------------------------
#def ile tekrar kullanilabilen bir def yazabiliriz
# my_numbers=[1,2,3,4,5,6,7,8,9,10]

"""
my_numbers=[1,2,3,4,5,6,7,8,9,10]

def square(x):
    return x**2

squares= list(map(square,my_numbers)) # bir listeye ayni fonksiyonu uygulamak icin map kullandik ve yazdirabilmek icin list e cevirdik
print(squares)

"""

#ya da bunu lambda ile yazariz tek kullnimlik olur:

"""
my_numbers=[1,2,3,4,5,6,7,8,9,10]
print(squares)
squares= list(map(lambda z : z**2, my_numbers))
"""
# bunu filter ile de yazabiliriz
"""
my_numbers=[1,2,3,4,5,6,7,8,9,10]
evens= list(filter(lambda x : x%2==0, my_numbers)) # my_numbers icindeki elemanlardan cift olanlari dondurur, list e cevirerek de yazdirilabilir olur
print("evens: ",evens)

"""
#-------------------------------------
# YOUTUBE 3 LAMBDA

"""
denklem = lambda x: x**2 # denklem kendi basina tek satirlik bir def oldu brda

sonuc= denklem(3)
print(sonuc)
 """

"""
isim_soyisim=['Mehmet Gezer','Muhammet Alkan','Eren Ergin','Fatih Gozubek']
isim_soyisim.sort(key= lambda x: x.split(' ')[-1].lower()) #burdaki x, her bir elemani temsil eder), split() ile isim soyisim ayirdik, 
#[-1] ile soyismi aldik ve kucuk harfe cevirdik, sort() ile de soyisime gore siraladik. sort() metodu key e gore siralar, 
#biz kendimiz soyisme gore siralamak icin ve listedeki her elemana uygulamak icin lambda kullanarak souismi ayirma fonksiyonu yazmis olduk
print(isim_soyisim)
"""

#-------------------------------------
#lambda alistirmalari
# Alıştırma 1: Verilen bir listedeki sayıların ortalamasını hesaplayan bir lambda ifadesi yazınız.

"""
listem=[2,3,6,7,1,2,32,5]
ortalama=lambda x: sum(x)/len(x)

sonuc= ortalama(listem)
print(sonuc)
"""
#Alıştırma 2: Verilen bir liste içindeki tek sayıları filtreleyen bir lambda ifadesi yazın.

"""listem=[2,3,6,7,1,2,32,5]
tekleri_bul= lambda x: x%2!=0
tekler= list(filter(tekleri_bul,listem))
print(tekler)
"""

#Alıştırma 3: Verilen bir liste içindeki negatif sayıları filtreleyen bir lambda ifadesi yazın.

"""
listem=[-2,3,6,7,-1,2,32,-5]
 
negatifler= list(filter(lambda x : x<0,listem))
print(negatifler)
"""

#Alıştırma 4: Verilen listenin elemanlari olan tuple lari sayilara gore buyukten kucuge siralayiniz.

"""
unsorted_list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

unsorted_list.sort(key= lambda x : x[1])
print(unsorted_list)
"""
#map alistirmalari
#Alıştırma 1: math modülünü kullanarak verilen listenin karekökünü hesaplayan fonksiyon yazınız.

"""
numbers=[9, 16, 25, 36, 144]

karekokler=list( map(lambda x : x**(1/2), numbers))
print(karekokler)
"""
#Alıştırma 2: Verilen listedeki elemanların tek mi çift mi olduklarını liste olarak yazdırınız.(map ve lambda kullaniniz.

"""
numbers = [1, 2, 3, 4, 5]

sonuc=list(map(lambda x : 'cift' if x%2==0 else 'tek',numbers))
print(sonuc)
"""

#-------------------------------------
#REDUCE iterable veriyi tek bir veriye donusturene kadar bir islem tekrarlar
#reduce(function,iterabla)

from functools import reduce

letters=['h','e','l','l','o']

kelime= reduce(lambda x,y : x+y, letters)
print(kelime)

sayilar=[1,2,3,4,5,6,7,8,9]

carpim= reduce(lambda x,y : x*y, sayilar)
print(carpim)