# collections:
# -list=[] ordered and changable, duplicates ok
# -tuple=() ordered and unchangable , duplicates ok, FASTER index ve count metodu var
# -set={} random,unordered and immutable, no dublicates but add/remove ok
# -dictionary= collection of keys and values {key:value}, ordered and changable, no duplicates


# fruits=("apple","banana","tomato")
# print(dir(fruits))
# print(help(fruits))
# for i in fruits:
    # print(i)  

# baskentler={"turkiye":"Ankara",
#             "amerika":"washington",
#             "hindistan":"new delhi",
#             }

# print(baskentler.get("turkiye"))

# if baskentler.get("urfa"):
#     print("mevcut")
# else:
#     print("yok")

# baskentler.update({"rusya":"moskova"})
# baskentler.update({"amerika":"detroit"})

# baskentler.pop("turkiye")
# baskentler.popitem()#son cifti siler
#print(baskentler)

# anahtarlar= baskentler.keys()

# print("\n",anahtarlar)

# for i in baskentler.keys():
#     print(i)


# degerler= baskentler.values()

# for i in baskentler.values():
#     print(i)

# items= baskentler.items()
# print(items)

# for key, value in baskentler.items():
#     print(f"{key}-{value} baskentler icinde bir cifttir")