class BankAccount:
    def __init__(self, account_name, account_number, initial_deposit):
        self.account_name = account_name
        self.account_number = account_number
        self._account_balance = initial_deposit

        print(f"Account Name: {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: ${self.account_balance:.2f}")

    @property
    def account_balance(self):
        return self._account_balance
    

    def deposit(self, amount):
        self._account_balance += amount
        print(f"Account Name: {self.account_name}")
        print(f" Deposited ${amount:.2f}. New balance: ${self._account_balance:.2f}")

    def withdrawal(self, amount):
        if amount > self._account_balance:
            raise ValueError("Insufficient funds")
        
        self._account_balance -= amount
        print(f"Account Name: {self.account_name} Withdrew ${amount:.2f}. New balance: ${self._account_balance:.2f}")

    def transfer(self, amount, receipient_account):

        if amount > self._account_balance:
            raise ValueError("Insufficient funds for transfer")

        self._account_balance -= amount
        receipient_account.deposit(amount)
        print(f"Transferred ${amount:.2f} to {receipient_account.account_name}. New balance: ${self._account_balance:.2f}")


    # def deposit(self, amount):
    #     self._account_balance += amount

class InterestRewardsAccount(BankAccount):
    def __init__(self, account_name, account_number, initial_deposit, interest_rate):
        super().__init__(account_name, account_number, initial_deposit)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._account_balance * (self.interest_rate / 100)

    def apply_interest(self):
        interest = self.calculate_interest()
        self._account_balance += interest


account_1 = BankAccount("Paddy", "123456", 100000)
account_2 = BankAccount("Debs", "123457", 100000)

# print(f"Account Name: {account_1.account_name}")
# print(f"Account Number: {account_1.account_number}")
# print(f"Account Balance: {account_1.account_balance}")

account_1.deposit(8000)
# print(f"Account Balance after deposit: ${account_1.account_balance}")

account_1.withdrawal(5000)
# print(f"Account Balance after withdrawal: ${account_1.account_balance}")

account_1.transfer(20000, account_2)
interest_account = InterestRewardsAccount("Paddy", "123456", account_1.account_balance, 30)
interest_account.apply_interest()
print(f"Account Balance after applying interest: ${interest_account.account_balance}")
# print(f"Account Balance after transfer: ${account_1.account_balance}")

account_2.account_balance
# print(f"Account Balance after receiving transfer: ${account_2.account_balance}")
# account_1.account_balance = 300000

# print(f"Account Balance after manual update: ${account_1.account_balance}")
# account_1.withdrawal(200000)  # This will raise a ValueError for insufficient funds
