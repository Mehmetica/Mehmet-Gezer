# dosya=open("yeni_dosya.txt",mode='r+', encoding="utf-8")
# icerik=dosya.read()
# dosya.close()

# print("Dosya adi: ", dosya.name)
# print("kapali mi: ", dosya.closed)
# print("Erisim modu: ", dosya.mode)
#----------------------------------------------------------------

text="""Programlama dillerinde sabit diske veri yazmak ve veriyi okumak verilerimizin kalıcı açısından önemlidir. 
    Her ne kadar günümüzde veritabanına yazma/okuma ve hatta bulut üzerinde yazma/okuma popüler olsa da standart dosya işlemleri de en temel veri saklama yöntemidir. 
    Python, dosyaları değiştirmek için gerekli temel fonksiyonları ve yöntemleri sağlar. 
    Bir dosya nesnesini kullanarak dosya işlemlerin çoğunu yapabilirsiniz. 
    C programlama dilindeki dosya işlemlerine çok benzer metotlar içerir."""

with open ("dosya.txt",'w+',encoding='utf-8') as dosya:
    dosya.write(text)
    dosya.seek(0)
    satirlar=dosya.readlines()

    for i in satirlar:
        print(i)

