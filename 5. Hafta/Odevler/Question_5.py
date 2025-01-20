class Customer():
    def __init__(self,name,surname,tc_identification,phone):
        self.name=name
        self.surname=surname
        self.tc=tc_identification
        self.phone=phone

    def display_information(self):
            print( f"""
            Customer Info:
            Name: {self.name}
            Surname: {self.surname}
            ID: {self.tc}
            Phone: {self.phone}
            """)

    
class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone,account_number,balance):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        new_balance=self.balance + amount
        self.balance=new_balance
        print( f"{amount} USD is added to your account,\nYour new balance is: {self.balance}")

    def money_check(self, amount):
         if amount>self.balance:
              print("The amount that you want to withdraw is greater than your current balance! You can not do that!")
         else:
              new_balance=self.balance-amount
              self.balance=new_balance
              print(f"You have withdrawed {amount} USD from your account. Current balance is: {self.balance}")
    
    def display_balance(self):
         print (f"Your current balance is: {self.balance}")

    



        


account1=Account("Mehmet","Gezer","1234356657",123345,100,1000)
print("-----------------------------------------")
account1.deposit(250)
print("-----------------------------------------")
account1.display_information()
print("-----------------------------------------")
account1.money_check(1500)
account1.money_check(350)
print("-----------------------------------------")
account1.display_balance()