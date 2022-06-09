class bank_account:
    def details(self, firstname, lastname, NIN, age, phone_number, LGA, state_of_origin, country):
        self.firstname = str(input("Enter your firstname: "))
        self.lastname = str(input("Enter your lastname: "))
        self.NIN = int(input("Enter your NIN: "))
        self.age = int(input("Enter your age: "))
        self.phone_number = int(input("Enter your phone_number: "))
        self.LGA = str(input("Enter your LGA: "))
        self.state_of_origin = str(input("Enter your state_of_origin: "))
        self.country = str(input("Enter your country name: "))


        # if phone_number <= 11:
        #     print("invalid")



        import random
        accountNumber = random.randint(10000000000, 99999999999)



        if self.details == "":
            print("you have not completed the form")
        else:
            print("congratulations!!", self.firstname, self.lastname, "you have successfully opened an account, your account number is: ", accountNumber)


    def __init__(self):
        self.balance = 0
        print("hello, welcome to your deposit and withdrawal machine")
    def deposit(self):
        amount = float(input("enter amount to be deposited: "))
        self.balance += amount
        print("\n amount deposited: ", amount)
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n you withdrew: ",amount)
        else:
            print("\n sorry insufficient balance")
    def display(self):
        print("\n net available balance =", self.balance)
s = bank_account()


s.details("self", "firstname", "lastname", "NIN", "age", "phone_number", "LGA" "state_of_origin", "country")
s.deposit()
s.withdraw()
s.display()
