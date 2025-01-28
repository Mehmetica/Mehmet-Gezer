class Employee: 
    def __init__(self, first, last):
        self.first = first
        self.last=last
        self.email= first+'.'+last+'@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter#yukaridaki metodun setter'i. 
    def fullname(self,name):
        first, last = name.split( )
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first=None
        self.last=None


    @property 
    def mail(self):
        return '{}{}@email.com'.format(self.first, self.last)
    

emp_1= Employee ('john', "smith")
emp_1.first="mehmet"
emp_1.fullname= 'Mehmet Gezer'


#print(emp_1.fullname())
print(emp_1.fullname)#prorety ekledikten sonra diren bir attribute gibi cagirabiliriz
print(emp_1.first)
print(emp_1.mail)

#eger sinifin methodlarina bir nesne gibi ulasmak istiyorsak ve degistirmek istiyorsak onlari property yapariz @property




del emp_1.fullname
print(emp_1.first)