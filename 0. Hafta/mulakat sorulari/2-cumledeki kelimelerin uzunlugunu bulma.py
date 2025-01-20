cumle=input("Lutfen bir cumle giriniz: ")

kelimeler=cumle.split()

uzunluk=[]
for i in kelimeler:
    uzunluk.append(len(i))

print("kelimelerin uzunluklari: ", uzunluk)