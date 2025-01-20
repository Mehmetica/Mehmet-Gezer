
cumle = input("Bir metin giriniz: ")
yeni_cumle = ""

for i in cumle:
    if i != " ":
        yeni_cumle += i

print("cumlenin bosluklarini kaldirdim: ", yeni_cumle)
