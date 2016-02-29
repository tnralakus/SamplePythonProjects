__author__ = 'alakus'

from classes.Account import Account
from classes.AccountType import AccountType

class SavingsAccount(Account):
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id, AccountType.SAVINGS)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_part = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_whole = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_part = int(self.numstr[self.numstr.find('.') + 1:])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # debugging purposes only
        # print "self whole", self.amount_whole
        # print "self part", self.amount_part

        # separates the whole number from decimal number of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_part = int(numstr[numstr.find('.') + 1:])

        # debugging purposes only
        # print "whole", self.withdraw_whole
        # print "part", self.withdraw_part

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_whole -= self.withdraw_whole

            # if the decimal value of requested amount is greater than the
            # decimal value of the amount in the account, then 1 dollar is taken out
            # and then calculates the remaining decimal value
            if self.withdraw_part > self.amount_part:
                self.amount_part = self.withdraw_part - self.amount_part
                self.amount_whole -= 1
                self.amount_part = 100 - self.amount_part
            else:
                self.amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_whole) + "." + str(self.amount_part)

            # debugging purposes only
            # print "\nnew whole", self.amount_whole
            # print "new part", self.amount_part
            # print "new amount", new_amount

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print "Error! Cannot withdraw larger than what you have."

    def display_amount(self):
        print self.amount

    def get_amount(self):
        return self.amount