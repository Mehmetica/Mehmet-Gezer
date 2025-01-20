import random

# Bir liste üzerinden rastgele seçim yap
liste = ['elma', 'armut', 'muz', 'kiraz']
rastgele_secilen = random.choice(liste)
print(rastgele_secilen)


print(random.random())#0-1 arasi rastgele sayi uretme
print(random.uniform(1,5))#1-5 arasi sayi uretme
print(random.randint(1,7),"(random.randint(1,7)")# 1-7 arasi tam sayi uretme
print(random.randrange(1,10,2),"random.randrange(1,10,2)")# 1-10 arasi 2 ser artan sayilardan (1,3,5,7,9) rastgele secmek
print(random.choice(liste))#verilen listeden rastgele secer
print(random.sample(liste,2))#listeden 2 adet rastgele eleman secer
print(random.shuffle(liste))#karistirir listeyi
print(random.getrandbits(1))
print(random.getstate())
print(random.setstate(random.getstate() ))
print(random.getstate())
print(random.seed(1))
print("---------------------------------")

