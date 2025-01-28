class Employee:
    num_of_emps=0
    raise_amt= 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email= first + '.' + last + '@email.com'

        Employee.num_of_emps+=1
    
    def fullname(self):
        return '{} {} '.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt= amount

    @classmethod # bunu artik alternative constructor olarak kullanabiliriz
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        # return Employee(first, last, pay) #alttaki ile ayni manaya geliyor
        return cls(first, last, pay)
    
    @staticmethod #std metodlar ilk arg olarak self alir, class methodlari ise cls alir, 
    #ancak static metodlar sadee gireegimiz arg lari alir, instance ile veya class ile calismaz, bagimsiz bir method olarak dusunebiliriz.class dan object uretmeden de, sadece sinif ismi kullanarak  kullanabiliriz
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True



    
# emp_1 = Employee("mehmet","Gezer", 190000)
# emp_2 = Employee("ahmet","ASLAN", 200000)
#---------------------------------

# Employee.set_raise_amt(1.05)#class metodu oldugu icin direk class ismiyle ile cagirabiliriz
# emp_1.set_raise_amt(1.07)#ayni zamanda o klasin nesnesi ile de cagirilabilir

#---------------------------------

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
#---------------------------------


        
emp_str_1 = "Ali-Gezer-130000"
emp_str_2 = "Kemal-Aslan-90000"
emp_str_3 = "Mahmut-Bucak-20000"

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)

# print(new_emp_1.pay)
#---------------------------------
# #class metodu kullanimi
# new_emp_1= Employee.from_string(emp_str_1)
# print(new_emp_1.pay)
#---------------------------------
#static metod kullanimi
import datetime
my_date = datetime.date(2016,6,30)

print(Employee.is_workday(my_date))