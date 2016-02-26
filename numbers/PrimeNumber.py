__author__ = 'alakus'

import sys

def get_cost():
    return float(raw_input('Enter cost:$'))


def get_money():
    return float(raw_input('Enter money given:$'))


def get_change(cost, money_given):
    return float(money_given - cost)


def get_quarters(change_left):
    quarters = int((change_left * 100) / 25)
    change_left -= (quarters * .25)
    return (quarters, change_left)

def get_dimes(change_left):
    dimes = int((change_left * 100) / 10)
    change_left -= (dimes * .1)
    return (dimes, change_left)

def get_nickels(change_left):
    nickels = int((change_left * 100) / 5)
    change_left -= (nickels * .05)
    return (nickels, change_left)

def get_pennies(change_left):
    return int(change_left * 100)

def main(args):
    cost = get_cost()
    money = get_money()
    change_left = get_change(cost, money)
    while change_left < 0:
        print('The money given is less than cost!!!')
        money = get_money()
        change_left = get_change(cost, money)
    print('Change left is:${:,.2f}').format(change_left)
    quarters, change_left = get_quarters(change_left)
    dimes, change_left = get_dimes(change_left)
    nickels, change_left = get_nickels(change_left)
    pennies = get_pennies(change_left)
    print ("Change to give\n{:=<14}\n{:<12}{}\n{:<12}{}\n{:<12}{}\n{:<12}{}").format('','Quarters:',quarters,'Dimes:' ,dimes,'Nickels:', nickels,'Pennies:', pennies)

if __name__ == "__main__":
    main(sys.argv[1:])
    sys.stdout.flush()