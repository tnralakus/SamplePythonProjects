__author__ = 'alakus'

from classes.CheckingAccount import CheckingAccount
from classes.SavingsAccount import SavingsAccount
from classes.BusinessAccount import BusinessAccount
from classes.AccountType import AccountType

def initialize_objects():
    global sally_checking, paolo_business, paolo_savings, master_list

    sally_checking = CheckingAccount(1, 2567.50)
    paolo_savings = SavingsAccount(2, 12890.01)
    paolo_business = BusinessAccount(2, 14500.40)

    master_list = [sally_checking, paolo_savings, paolo_business]

def get_selected_account(customer_accounts):
    selected_account = None
    if len(customer_accounts) == 1:
        selected_account = customer_accounts[0]
        print('You have one account. Account Id is : ' + str(selected_account.account_id) + ' Account type is ' + AccountType.tostring(selected_account.account_type).upper())
    elif len(customer_accounts) > 1:
        print 'You have ' + str(len(customer_accounts)) + ' different accounts. '
        for account in customer_accounts:
            print str(account.account_id) + ' ' + AccountType.tostring((account.account_type))
        account_id = input('Which account would you like to use?')
        selected_accounts = filter(lambda account: account.account_id == account_id, customer_accounts)
        if len(selected_accounts) > 0:
            selected_account = selected_accounts[0]
        else:
            print "Error. You don't have that account."
            print "Please try again.\n"
    return selected_account


def launch_atm_transaction(account):
    print "How may I help you? \nPress 1 for balance view. \nPress 2 for withdrawals \nPress 3 to exit."
    action_value = input("Please enter your choice: ")
    if action_value == 1:
        account.display_amount()
    elif action_value == 2:
        amnt_to_withdraw = input("Enter the amount to withdraw: ")
        temp_str = str(amnt_to_withdraw)
        adjusted_amount = "%.2f" % amnt_to_withdraw
        # print "adjusted_amount:", adjusted_amount
        account.withdraw(adjusted_amount)
        print "current balance is", account.get_amount()
    elif action_value == 3:
        print "Thank for using the 24-hour ATM service."
        print "Have a pleasant day."
        print "##########################################"
        return False

    return True

def main():
    initialize_objects()
    while True:
        print "Welcome to 24-hour ATM service!!!!! \nInsert your card!!!!!"
        # Card reading the customer info representation
        customer_id = raw_input("Enter your customer id number: ")
        customer_id = int(customer_id)
        #customer_accounts = [account for account in master_list if account.customer_id == customer_id]
        customer_accounts = filter(lambda account: account.customer_id == customer_id, master_list)

        if len(customer_accounts) > 0:
            selected_account = None
            while selected_account is None:
                selected_account = get_selected_account(customer_accounts)
                is_account_session_on = selected_account is not None
                while is_account_session_on:
                    is_account_session_on = launch_atm_transaction(selected_account)
        else:
            print "Cannot find your record."
            print "Please get your card."
            print "Exiting this session..."


if __name__ == '__main__':
    main()