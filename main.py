from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

def main():
    #initiating and checking both a checking and savings account
    checking1 = CheckingAccount(15,"Matthew", 1000, "Checking",15)
    savings1 = SavingsAccount(15,"Matthew",1500, "Savings", .07,37)
    checking1.print_customer_information()
    savings1.print_customer_information()

    #scenario: withdraw 800 from the checking to put it under the 250 min balance (transfer limit)
    checking1.withdraw(800)
    checking1.transfer_money(50,savings1)
    #throws an "error" because there aren't enough funds, so add some
    checking1.deposit(500)
    checking1.print_customer_information()
    checking1.transfer_money(50,savings1)
    checking1.print_customer_information()
    savings1.print_customer_information()



main()