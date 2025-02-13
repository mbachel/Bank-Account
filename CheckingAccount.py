from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    minimum_balance = 250

    def __init__(self, account_number, customer_name, current_balance, type, routing_number):
        super().__init__(account_number, customer_name, current_balance, type)
        self.routing_number = routing_number

    def transfer_money(self, amount, other_account):
        #transfer limitation:
        #if balance less than amount OR the transfer would be less than the min balance, break
        if self.current_balance < amount or self.current_balance - amount < self.minimum_balance:
            print("Error. Not enough funds to transfer.")
            return
        self.current_balance -= amount
        other_account.deposit(amount)
        print(f"Transfer from routing #{self.routing_number} to routing #{other_account.routing_number} successful.")
        print()