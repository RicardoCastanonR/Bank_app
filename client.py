class Client:
    def __init__(self, name, age, account_number, pin, balance = 0):
        self.name = name
        self.age = age
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def print_user_info(self):
        print(f"""
                {self.name} account information

                Account: ****{self.account_number[-4:]}
                Balance: {self.balance}
              """)