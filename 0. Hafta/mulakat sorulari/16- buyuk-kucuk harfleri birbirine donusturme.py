"""cumle= input("Bir cumle giriniz: ")

son_hali=""

for harf in cumle:
    if harf.isupper():
        son_hali+=harf.lower()
    else :
        son_hali+=harf.upper()

print(son_hali)"""

cumle = input("Bir cumle giriniz: ")
print(cumle.swapcase())
