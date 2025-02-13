import BankAccount from BankAccount

class SavingsAccount(BankAccount):
    minimum_balance = 500
    def __init__(self, account_number, customer_name, current_balance, interest_rate):
        super().__init__(account_number, customer_name, current_balance)
        self.interest_rate = interest_rate

    def generate_interest(self):
        if self.current_balance >= self.minimum_balance:
            self.current_balance *= (1 + self.interest_rate)
            print(f"Account balance was increased to {self.current_balance}")