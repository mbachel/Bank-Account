#Worked with Devdan
class BankAccount:
    bank_title = "Bank of America"
    def __init__(self,customer_name,current_balance,minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self,amount):
        if (amount >= 0):
            self.current_balance += amount
            print(f"Deposit Successful\n"
                  f"New Balance: {self.current_balance}\n")
        return

    def withdraw(self,amount):
        if ((self.current_balance - amount) < self.minimum_balance):
            print("Error: Amount would exceed minimum balance")
            return
        self.current_balance -= amount

    def print_customer_information(self):
        print(f"Bank Title: {self.bank_title}\n"
               f"Name: {self.customer_name}\n"
               f"Current Balance: {self.current_balance}\n")

#Test instances:
cust1 = BankAccount("Matthew B",20000,10000)
cust1.deposit(100)
cust1.print_customer_information()
cust1.withdraw(100000)
cust1.print_customer_information()

cust2 = BankAccount("Matt C",50000,6000)
cust2.deposit(1000000)
cust2.print_customer_information()
cust2.withdraw(50000)