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

    #second instance, testing transfer and interest
    checking2 = CheckingAccount(20,"John Doe", 500, "Checking", 18)
    savings2 = SavingsAccount(20, "John Doe", 500 , "Savings", .07, 10)

    savings2.generate_interest()
    savings2.print_customer_information()

    checking2.transfer_money(100,savings2)
    savings2.generate_interest()
    checking2.print_customer_information()
    savings2.print_customer_information()

main()