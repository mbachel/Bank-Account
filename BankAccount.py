class BankAccount:
    bank_title = "Bank of America"
    def __init__(self, account_number, customer_name, current_balance):
        self._account_number = account_number
        self.customer_name = customer_name
        self.current_balance = current_balance

    def deposit(self,amount):
        if amount >= 0:
            self.current_balance += amount
            print(f"Deposit Successful\n"
                  f"New Balance: {self.current_balance}\n")
        return

    def withdraw(self,amount):
        if self.current_balance <= 0 && self.current_balance > amount:
            print("Withdraw Failed\n")
            return
        self.current_balance -= amount

    def print_customer_information(self):
        print(f"Bank Title: {self.bank_title}\n"
               f"Account Number: {self._account_number}\n"
               f"Name: {self.customer_name}\n"
               f"Current Balance: {self.current_balance}\n")

def testing():
    #Test instances:
    cust1 = BankAccount(1,"Matthew B",20000)
    cust1.deposit(100)
    cust1.print_customer_information()
    cust1.withdraw(100000)
    cust1.print_customer_information()

    cust2 = BankAccount(2,"Matt C",50000)
    cust2.deposit(1000000)
    cust2.print_customer_information()
    cust2.withdraw(50000)