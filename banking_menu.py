from account import Account
def create_account():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    acc_type = input("Do you want to open a saving(S) or Current(C) account: ")
    acc = Account(name, address, acc_type)
    print("Account Created Successfully")
    return acc

def deposit_money(acc):
    amount = float(input("Enter the amount to deposit: "))
    success, message = acc.deposit(amount)
    print(message)

def withdraw_money(acc):
    amount = float(input("Enter the amount to withdraw: "))
    success, message = acc.withdraw(amount)
    print(message)

def check_balance(acc):
    success, message = acc.check_balance()
    print(message)