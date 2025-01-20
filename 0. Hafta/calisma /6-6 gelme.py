import random

alti=0
deneme=0

while True:
    deneme+=1
    zar1= random.randint(1,6)
    zar2= random.randint(1,6)
    if zar1==6 and zar2==6:
        alti+=1
    if alti==10:
        print(f"10 defa 6-6 gelmesi icin {deneme} defa denendi")
        break