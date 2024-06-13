from account import Account
from banking_menu import create_account, deposit_money, withdraw_money, check_balance

def main():
    acc = None
    while True:
        print("Banking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        if choice == 1:
            acc = create_account()
        elif choice == 2:
            if acc is None:
                print("Please create an account first.")
                continue
            deposit_money(acc)
        elif choice == 3:
            if acc is None:
                print("Please create an account first.")
                continue
            withdraw_money(acc)
        elif choice == 4:
            if acc is None:
                print("Please create an account first.")
                continue
            check_balance(acc)
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()