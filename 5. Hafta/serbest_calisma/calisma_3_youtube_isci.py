class Person:
    number_of_people=0#bu attribute tum sinifa aittir, direk class ismiyle de cagirabiliriz ya da object ile de cagirabiliriz
    def __init__(self, name):
        self.name=name

    @classmethod
    def add_people(cls):#cls yazinca sadece class a ozel bir fonk oluyor. alt siniflardan, instance ile cagirilamiyor.
        Person.number_of_people +=1

p1=Person("ali")
p2=Person("mehmet")

print(Person.number_of_people)
print(p1.number_of_people)

Person.number_of_people=9
print(Person.number_of_people)
