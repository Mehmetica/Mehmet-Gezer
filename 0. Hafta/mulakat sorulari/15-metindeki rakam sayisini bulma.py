cumle= input("Bir cumle giriniz: ")
rakam_sayisi=0

for eleman in cumle:
    if eleman.isdigit():
        rakam_sayisi+=1

print(f"cumledeki rakam sayisi: {rakam_sayisi} dir")