class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount, acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f"\nAccount '{self.name}' created.\nBalence =${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = $'{self.balance:.2f}'")
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"\nDeposit completed!")
        self.get_balance()

    def viableTransaction(self,amount):
        if self.balance>= amount:
            return
        else:
            raise BalanceException(f"\n Sorry, account '{self.name}' has only $'{self.balance:.2f}'")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance-=amount
            print("\nWithdraw completed!")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWitdraw interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print('\n**************\n\nBeginning Transfer...🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer completed ✅")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewarsdAcct(BankAccount):
    def deposit(self,amount):
        self.balance=self.balance+ (amount*1.05)
        print("\nDeposit complete ✅")
        self.get_balance()

class SavingsAcct(InterestRewarsdAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance-=(amount+self.fee)
            print("Withraw complete")
            self.get_balance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: '{error}'")
    








