import random

zarlar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(100000):
    zar=random.randint(1, 6)
    zarlar[zar]+=1

for zar in zarlar:
    print(f"{zar}: {zarlar[zar]/100000000 }")

