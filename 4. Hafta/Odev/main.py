import Member_Transactions
import Kitap_transactions
import modul_hata_yakala
import Member_Transactions
import json
import os






while True:
    print("""
    ------------------------------------------------------------
    -      Halk Kutuphanesine Hosgeldiniz!                     -
    -                                                          -
    -   1- Uyelik Islemleri                                    -                    
    -   2- Kitap Islemleri                                     -                     
    -   0- Cikis                                               -                       
    -                                                          -
    ------------------------------------------------------------
    """)

    secim = modul_hata_yakala.hata_yakala(2)
    
    if secim == 1:
        while True:
            print("""
        ------------------------------------------------------------
        -                     Uyelik Islemleri                     -
        -                                                          -
        -   1- Uyeleri Listele                                     -                    
        -   2- Uye Ekle                                            -                     
        -   3- Uye Ara                                             -                       
        -   4- Uye Sil                                             -                       
        -   5- Kitap Odunc Ver                                     -                       
        -   6- Kitap Iade Et                                       -                       
        -   7- Kitap Takip Et                                      -                       
        -   0- Cikis                                               -                       
        -                                                          -
        ------------------------------------------------------------    
        """)
            print("Uyelik islemlerine giris yaptiniz!")
            uyelik_secimi = modul_hata_yakala.hata_yakala(7)

            if uyelik_secimi == 0:
                break  

            elif uyelik_secimi == 1:
                Member_Transactions.list_member()
            
            elif uyelik_secimi == 2:
                kullanici=Member_Transactions.kayit_bilgiler_al()
                Member_Transactions.add_member(kullanici)

            elif uyelik_secimi == 3:
                Member_Transactions.check_member()

            elif uyelik_secimi == 4:
                Member_Transactions.delete_member()

            elif uyelik_secimi == 5:
                uye=Member_Transactions.get_member_info()
                Member_Transactions.search_book(uye)
                Member_Transactions.give_book(uye)

            elif uyelik_secimi == 6:
                Member_Transactions.receive_book()
            
            elif uyelik_secimi == 7:
                Member_Transactions.members_book()

    elif secim == 2:
        file_name="/Users/mehmetgezer/PycharmProjects/Mehmet Gezer/json_dosyalari/kitap.json"

        while True:
            print("""
        ------------------------------------------------------------
        -                     Kitap Islemleri                      -
        -                                                          -
        -   1- Kitaplari Listele                                   -                    
        -   2- Kitap Ekle                                          -                     
        -   3- Kitap Ara                                           -                       
        -   4- Kitap Sil                                           -                                             
        -   0- Cikis                                               -                       
        -                                                          -
        ------------------------------------------------------------    
        """)
            print("Kitap islemlerine giris yaptiniz!")
            kitap_secimi = modul_hata_yakala.hata_yakala(4)
            
            if kitap_secimi == 0:
                break  

            elif kitap_secimi == 1:
                Kitap_transactions.list_books(file_name)

            elif kitap_secimi == 2:
                new_book = Kitap_transactions.get_book_info()
                Kitap_transactions.add_book(file_name, new_book)

            elif kitap_secimi == 3:
                kitap_adi=input("Aradiginiz kitap adini giriniz: ").lower()
                Kitap_transactions.search_book(file_name, kitap_adi)

            elif kitap_secimi == 4:
                barkod=int(input("Silinecek kitabin barkod numarasini giriniz: "))
                Kitap_transactions.delete_book(file_name,barkod)

    elif secim == 0:
        print("Sistemden guvenle cikis yaptiniz!")
        break  
