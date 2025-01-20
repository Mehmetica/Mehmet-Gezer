birinci=input("1.metni giriniz: ")
ikinci= input("2.metni giriniz: ")

birlesik_metin= (birinci+" "+ikinci).split()



dizi=[]

for eleman in birlesik_metin:
    dizi.append(eleman[:-1]+eleman[-1].upper())



print(" ".join(dizi))

"""
girdi1 = input("1yaz")
girdi2 = input("2yaz")

yeni= girdi1[:-1]+girdi1[-1].upper()+" "+ girdi2[:-1]+girdi2[-1].upper()

print(yeni)"""






