import json
from datetime import datetime, timedelta
import Zaman


file_name="/Users/mehmetgezer/PycharmProjects/Mehmet Gezer/json_dosyalari/kitap.json"

def read_json_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_json_file(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def add_book(file_name, book):
    books = read_json_file(file_name)
    books.append(book)
    write_json_file(file_name, books)
    print("Kitap başarıyla eklendi.")

def get_book_info():
    Barkod = int(input("Barkod numarasını giriniz: "))
    Dil = input("Kitabın dilini giriniz: ")
    Fiyat = float(input("Kitabın fiyatını giriniz: "))
    Kitap_Adi = input("Kitabın adını giriniz: ")
    Yayinevi = input("Kitabın yayınevini giriniz: ")
    Yazar = input("Kitabın yazarını giriniz: ")
    
    

    new_book = {
        "Barkod": Barkod,
        "Dil": Dil,
        "Fiyat": Fiyat,
        "Kitap_Adi": Kitap_Adi,
        "Yayinevi": Yayinevi,
        "Yazar": Yazar,
        
    }
    return new_book

def delete_book(file_name,barkod):
    while True:
        try:
            books = read_json_file(file_name)
            books = [book for book in books if book["Barkod"] != barkod]
            write_json_file(file_name, books)
            print("Kitap başarıyla silindi.")
            break
        except Exception:
            print("Hatali giris yaptiniz, tekrar deneyiniz.")


def list_books(file_name):
    books = read_json_file(file_name)
    for book in books:
        print(book)


def search_book(file_name, keyword):
    books = read_json_file(file_name)
    found_books = [book for book in books if keyword.lower() in book["Kitap_Adi"].lower()]
    if found_books:
        for book in found_books:
            print(f"{book} isimli kitap kutuphanemizde mevcuttur.")
    else:
        print("Kitap bulunamadı.")



