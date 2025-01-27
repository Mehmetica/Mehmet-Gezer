class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f" I am {self.name} and I am {self.age} years old ")

    def speak(self):
        print("Pet sinifi ne desin?")


class Cat(Pet): 
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def show(self):
        print(f" I am {self.name} and I am {self.age} years old and I  am {self.color}")

    def speak(self):
        print("meow")
    
class Dog(Pet):  
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p1=Pet("mahmut",3)
p1.show()
c=Cat("ali",45,"blue")#Cat sinifi Pet ten inherit yaptigi icin init fonk ve show fonk otomatik olarak kullanabilir. tekrar yazmaya gerek yok
c.show()
d=Dog("Murat",33)
d.show()
f=Fish("bubbles",1)
f.show()

p1.speak()#pet sinifinin speak fonk calisir
c.speak()#Cat sinifinin speak fonk calisir
d.speak()#ayni isimde alt siniflarda da fonk varsa, alt sinifinki override eder ve ustune baskin cikar, daha spesifik bir fonk oldugu icin
f.speak()#