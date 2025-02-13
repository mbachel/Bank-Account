import BankAccount from BankAccount

class CheckingAccount(BankAccount):
    minimum_balance = 0

    def __init__(self, account_number, customer_name, current_balance):
        super().__init__(account_number, customer_name, current_balance)