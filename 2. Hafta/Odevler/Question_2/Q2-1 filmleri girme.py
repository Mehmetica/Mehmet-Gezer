koleksiyon=[]
cevap=""
while cevap!="h":
    isim = input("Film adı: ")
    yonetmen = input("Yönetmen: ")
    yil = input("Yayın yılı: ")
    tur = input("Tür: ")
    film = {"isim": isim, "yonetmen": yonetmen, "yil": yil, "tur": tur}
    koleksiyon.append(film)
    print("Film başarıyla eklendi!")
    
    cevap=input("Tum giris isleminiz bittiyse 'H' basiniz: ")
    
    

