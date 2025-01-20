ad = "ali"
soyad = "gezer"

while True:
    girilenad = input("Adınızı giriniz: ")
    girilensoyad = input("Soyadınızı giriniz: ")

    # Eğer hem ad hem soyad doğru ise, hoş geldiniz mesajını göster ve döngüyü bitir
    if girilenad == ad and girilensoyad == soyad:
        print("Hoş geldiniz")
        break

    # Eğer ad yanlış, soyad doğru ise:
    elif girilenad != ad and girilensoyad == soyad:
        print("Adınız yanlış. Lütfen tekrar deneyin.")

    # Eğer soyad yanlış, ad doğru ise:
    elif girilenad == ad and girilensoyad != soyad:
        print("Soyadınız yanlış. Lütfen tekrar deneyin.")

    # Her ikisi de yanlışsa:
    else:
        print("Adınız ve soyadınız yanlış. Lütfen tekrar deneyin.")
