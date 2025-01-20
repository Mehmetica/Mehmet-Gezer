# sozluk={
#     "isim":"Ahmet",
#     "soyisim":"Yılmaz",
#     "yas":25,
#     "meslek":"Mühendis",
#     "telefonlar":[5555555555,6666666666,7777777],
    
    
# }

# # print(sozluk)
# sozluk["cinsiyet"]="erkek"
# # print(sozluk)

# # print(sozluk["telefonlar"][0])
# y=sozluk.get("yas")
# print(y)
# print(sozluk.keys())
# print(sozluk.values())

# x=sozluk.items()
# print(x)

# if "yas" in sozluk:
#     print("var")

# sozluk.update({"mesklek":"pilot"})
# print(sozluk)

# sozluk.pop("yas")
# print(sozluk)

# sozluk.popitem()
# print(sozluk)

# sozluk.popitem()
# print(sozluk)

# del sozluk["isim"]
# print(sozluk)

# del sozluk
# sozluk.clear()

# for x in sozluk:
#     print(x,"-",sozluk[x])

# for x in sozluk.values():
#     print(x)

# for z in sozluk.keys():
#     print(z)

# for x,y in sozluk.items():
#     print(x,"-",y)

# print("😄! You're too  😎 🆒.")
#------------------------------------------------
# X if condition else Y
# x=3
# print("postivie" if x>0 else "negative")

# x=4
# result = "even" if x%2==0 else "odd"
# print(result)

# kelima=list("Ali")
# kelima.reverse()
# print(kelima)

### 1

# Soru-1:

# listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]

# Yukarida verilen liste ile ilgili asagidaki sorulari yanitlayiniz.

# 1-a: Kullanicidan bir sayi girmesini isteyiniz,  

# 1-b: Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekleyiniz.

# 1-c: Olusan yeni listenin icindeki tek sayilar ile tek_sayilar adinda yeni bir liste olusturunuz.

# 1-d: tek_sayilar isimli listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriniz.
#-------------------------------------------------------------------------------------------
# listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]

# sayi=int(input("Bir sayi giriniz: "))
# listem.insert(0,sayi)
# print(listem)

# # teksayilar=[]
# # for i in listem:
# #     if i%2!=0:
# #         teksayilar.append(i)


# tek_sayilar_listesi=[i for i in listem if i%2!=0]

# print(tek_sayilar_listesi.sort(reverse=True))
# tek_sayilar_listesi.sort(reverse=True)
# # print(tek_sayilar_listesi)

#-------------------------------------------------------------------------------------------

# listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]

# print(listem2[2][1])

# listem3=[x for x in range(0,10)]
# print(listem3)


# a={1,4,6,8,4,2,23,56}
# print(*a, sep=",")
#----------------------------------------------------------------------------------------
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# my_dict = {}

# for i in range(len(keys)):
#     my_dict.update({keys[i]: values[i]})

# print(my_dict) 