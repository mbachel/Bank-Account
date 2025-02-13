from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    minimum_balance = 500
    def __init__(self, account_number, customer_name, current_balance, type, interest_rate, routing_number):
        super().__init__(account_number, customer_name, current_balance, type)
        self.interest_rate = interest_rate
        self.routing_number = routing_number

    def generate_interest(self):
        if self.current_balance >= self.minimum_balance:
            self.current_balance *= (1 + self.interest_rate)
            print(f"Account balance was increased to {self.current_balance}")
        else:
            print("Account balance below minimum balance. Please deposit to earn interest.")
