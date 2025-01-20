cumle = input("Bir cumle giriniz:")

uzunluk = len(cumle.split())

print(cumle.split())

print(f"bu cumlede {uzunluk} kelime var")
tersdizi=[]
cumle_dizisi=cumle.split()
for kelime in cumle_dizisi:
    ters_kelime=""
    for harf in kelime:
        ters_kelime=harf+ters_kelime

    tersdizi.append(ters_kelime)

print(" ".join(tersdizi))
