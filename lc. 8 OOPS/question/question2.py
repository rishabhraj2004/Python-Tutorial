class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Method for debit
    def debit(self, amount):
        self.balance -= amount
        print(f"Amount debited: {amount}")
        print(f"Current balance: {self.get_balance()}")

    # Method for credit
    def credit(self, amount):
        self.balance += amount       
        print(f"Amount credited: {amount}")
        print(f"Current balance: {self.get_balance()}")

    # Method to get balance
    def get_balance(self):
        return self.balance


# Test
acc1 = Account(10000, "1234567890")
acc1.debit(2000)
acc1.credit(5000)
acc1.debit(3000)
acc1.credit(2000)
acc1.debit(1000)