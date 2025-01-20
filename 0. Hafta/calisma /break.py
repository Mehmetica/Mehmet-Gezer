defkullanici="ali"
defparola="1234"
i=0
while True:

    kullanici=input("Kullanici adi: ")
    parola=input("Parola: ")

    if kullanici==defkullanici and parola==defparola:
        print("hosgeldiniz sayin", kullanici)
        break
    elif kullanici!=defkullanici and parola==defparola:
        print("kullanici adi yanlis")
    elif kullanici==defkullanici and parola!=defparola:
        print("parola yanlis")
        i+=1
        if i==2:
            print("sifrenizi mi unuttunuz?"," E/H")
            cevap=input()
            if cevap=="E":
                mail= input("mail adresinizi giriniz:")
                print(mail+" adresine dogrulama kodu gonderiliyor..."," 6789 dogrulama kodunu giriniz...")
                dogrulamakodu=input("Dogrulama kodu:")
                if dogrulamakodu=="6789":
                    print("Yeni sifrenizi giriniz: ")
                    defparola=input()
                    print("yeni parolaniz: "+ defparola)
                else:
                    print("dogrulama kodu yanlis, tekrar deneyin")
                    break

    else:
        print("kullanici adi ve parola yanlis")
