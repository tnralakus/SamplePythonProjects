__author__ = 'alakus'

from classes.Account import Account
from classes.AccountType import AccountType

class BusinessAccount(Account):

    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id, AccountType.BUSINESS)
        self.amount = deposit_amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.amount > float(withdraw_amount):
            self.amount -= float(withdraw_amount)

            self.amount = round(float(self.amount), 2)
        else:
            print "Error! Cannot withdraw larger than what you have."

    def display_amount(self):
        print self.amount

    def get_amount(self):
        return self.amount
