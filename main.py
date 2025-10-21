print("Welcome to Practice Bank!")
print("No account exists yet")

while(True):
    create_account = input("Want to create a new account? [y/n] or close the application? [q]")

    if create_account.lower() == "y":
        print("Creating account")
        print("Please enter the following fields")
        name_input = input("NAME: ")
        age_input = input("Age: ")
        if not age_input.isdigit():
            print("Invalid age")
            continue
        age = int(age_input)
        if age < 18 :
            print("You must be at least 18 years old to register...")
            continue
        account_number = input("Account number (8 digits): ")
        if not len(account_number) == 8 and not account_number.isdigit():
            print("invalid account number...")
            continue
        
        pin = input("Introduce you PIN (4 digits): ")
        if not len(pin) == 8 and not pin.isdigit():
            print("Invalid pin")
            continue

        initial_amount = input("Introduce your initial ammount of money: ")

        print("The user has been created successfully")


    elif create_account.lower() == "q":
        break
    elif create_account.lower() != "n":
        break

        
        