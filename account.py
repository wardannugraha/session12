class Account:
    def __init__(self, name, address, acc_type, balance=0.0):
        self.name = name
        self.address = address
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"Deposit Successful. Available Balance: {self.balance}"
        else:
            return False, "Invalid deposit amount. Please try again."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True, f"Withdrawal Successful. Available Balance: {self.balance}"
        else:
            return False, "Invalid withdrawal amount. Please try again."

    def check_balance(self):
        return True, f"Available Balance: {self.balance}"