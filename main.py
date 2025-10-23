from client import Client

def age_input():
    age_input = input("Age: ")
    if not age_input.isdigit():
        print("Invalid age")
        return
    age = int(age_input)
    if age < 18 :
        print("You must be at least 18 years old to register...")
        return
    return age

# TODO: Generates the number automatically
def create_account_number():
    account_number = input("Account number (8 digits): ")
    if not len(account_number) == 8 and not account_number.isdigit():
        print("invalid account number...")
        return
    return account_number

def pin_input():
    pin = input("Introduce you PIN (4 digits): ")
    if not len(pin) == 8 and not pin.isdigit():
        print("Invalid pin")
        return
    return pin

def create_accout():
    print("Creating account")
    print("Please enter the following fields")
    
    name_input = input("NAME: ")

    age = age_input()
    account_number = create_account_number()
    pin = pin_input
    initial_amount = input("Introduce your initial ammount of money: ")
    
    new_client = Client(name_input, age, account_number, pin, initial_amount)
    print("The user has been created successfully")
    return new_client


print("Welcome to Practice Bank!")
print("No account exists yet")
while(True):
    create_account_i = input("Want to create a new account? [y/n] or close the application? [q]")
    if create_account_i.lower() == "y":
        client = create_accout()
        if client:
            client.print_user_info()
        else:
            print("Something wrong happened! D:")
        
    elif create_account_i.lower() == "q":
        break
    elif create_account_i.lower() != "n":
        break

        
        