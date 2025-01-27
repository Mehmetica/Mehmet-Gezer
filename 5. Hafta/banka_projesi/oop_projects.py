from bank_accounts import *

Dave= BankAccount(1000,"Dave")
Sarah= BankAccount(2000,"Sara")

# Dave.get_balance()
# Sarah.get_balance()

# Sarah.deposit(500)
# Dave.withdraw(3000)
# Dave.withdraw(10)

# print("--------------------------")

# Dave.transfer(500,Sarah)
# Sarah.transfer(1000,Dave)

# print("--------------------------")

# Jim=InterestRewarsdAcct(1000,"Jim")
# Jim.get_balance()
# Jim.deposit(100)
# Jim.transfer(100,Dave)

print("--------------------------")

Blaze= SavingsAcct(1000, "Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(1000,Sarah)

