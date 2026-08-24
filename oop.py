from bank_account import BankAccount
from bank_account import InterestRewardsAccount

account_1 = BankAccount("Paddy", 1234, 10000)
print("")
account_2 = BankAccount("Debs", 1235, 10000)
print("")
account_1.deposit(30000)
account_1.transfer(4000,account_2)

print("")
print(account_2._account_balance)

account_3 = InterestRewardsAccount("Eman", 1111, 300000)
account_3.deposit(300000)
print(account_3._account_balance)

account_3.transfer(20000, account_2)
account_3.transfer(20000, account_1)

account_2.account_balance
account_1.account_balance