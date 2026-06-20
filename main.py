from operations import *

while True:

    print("\n------ BANK MENU ------")
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.View Accounts")
    print("6.Delete Account")
    print("7.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        check_balance()

    elif choice == 5:
        view_accounts()

    elif choice == 6:
        delete_account()

    elif choice == 7:
        exit_program()
        break

    else:
        print("Invalid Choice")