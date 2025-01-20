
def hata_yakala(max_islem):
    while True:
        try:
            secim = int(input(f"Lütfen yapmak istediginiz islemi seciniz ve 0 ile {max_islem } arasında bir değer giriniz: "))
            if 0 <= secim <= max_islem:
                return secim  
            else:
                print(f"Yanlış değer girdiniz, 0 ile {max_islem } arasında bir değer giriniz.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı giriniz.")
