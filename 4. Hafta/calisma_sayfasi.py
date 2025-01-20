"""listem=[0,1,2,3]

try:
    listem[5]
except IndexError:
    print("Index eror verdi dikkat!")
else:
    print("Hata yok devamke!")
finally:
    print("Ben her turlu aga!")"""

#-----------------------------------
"""
try:
    bolunen = int(input("Bolunecek sayiyi girin: "))       
    bolen = int(input("Bolen sayiyi girin: "))       
    sonuc = bolunen / bolen
    print("1.sonuc ",sonuc)
except ValueError as e:#burda exception u e olarak tanimladik ve ilerde kullanabiliriz,yazdirabiliriz
    print(e)
    print("Lütfen geçerli bir sayı girin.")
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez.")
except Exception:
    print("Bir şeyler yanlış gitti.")
else:
    print(sonuc)
finally:
    print("Bu satir her zaman calisacaktir")
    """
#-----------------------------------

