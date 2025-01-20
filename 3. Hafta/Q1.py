"""
Soru 1: Görev Yöneticisi Uygulaması
Proje Açıklaması: Bu ödevde, Python programlama dilini kullanarak bir görev yöneticisi uygulaması oluşturacaksınız. 
Bu uygulama kullanıcıların görevlerini eklemelerine, tamamlamalarına, silmelerine ve listelemelerine izin verecektir.

Gereksinimler:
1- Görevler bir Python listesinde saklanacak ve her görev bir sözlük olarak temsil edilecektir. Her görev aşağıdaki özelliklere sahip olmalıdır:

Sıra Numarası (Otomatik olarak atanır)

Görev Adı

Durum (Tamamlandı, Beklemede veya Silindi)

2- Kullanıcının gerçekleştirebileceği işlemler:

Yeni bir görev ekleyin

Bir görevi tamamlayın

Görev silme

Tamamlanan görevleri listeleyin

Tüm görevleri durumlarıyla birlikte listeleyin

Çıkış

3- Görevler eklendikleri sıraya göre otomatik olarak sıra numarası almalıdır.

4- Silinen görevlerin numaraları yerine yeni görevler kaydedilmelidir.

5- Görevler listelenirken sıra numaralarına göre sıralanmalıdır.

6- Her işlemden sonra kullanıcıya uygun geri bildirim verilmelidir. Örneğin, yeni bir görev eklendiğinde, görevin eklendiğini belirten bir mesaj görmelidir.


"""
import os
gorevler_listesi=[{}]
sira_no=1


def ekle():
    global sira_no
    gorev_adi=input("Gorev adi giriniz: ")
    gorevler_listesi.append({
        "Sira No": sira_no, 
        "Gorev Adi": gorev_adi, 
        "Durum":"Beklemede"
        })
    sira_no+=1
    print(gorevler_listesi)
    print(f"{gorev_adi} isimli gorev listeye basarili bir sekilde eklendi!")

def tamamla():
    pass

def sil():
    pass

def tamamlananlari_listele():
    pass

def tumunu_listele():
    pass





while True:
    #os.system("clear")
    print("""
    Gorev yoneticisine hosgeldiniz!
        
        1-Yeni bir görev ekleyin
        2-Bir görevi tamamlayın
        3-Görev silme
        4-Tamamlanan görevleri listeleyin
        5-Tüm görevleri durumlarıyla birlikte listeleyin
        6-Çıkış       
    """)
    secim=int(input("Lutfen yapmak istediginiz islemi seciniz: "))

    if secim==1:
        ekle()
    elif secim==2:
        tamamla()
    elif secim==3:
        sil()
    elif secim==4:
        tamamlananlari_listele()
    elif secim==5:
        tumunu_listele()
    elif secim==6:
        print("Basari ile cikis yapildi!")
        break
    else:
        print("Yanlis giris yaptiniz!")
    print("Devam etmek icin enter'a basiniz...")







 
