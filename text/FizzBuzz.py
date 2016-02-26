__author__ = 'alakus'

"""
This program will print the numbers from 1 to 100.
For multiples of three, the program will print "Fizz" instead of the number and "Buzz" if the number is multiples of five.
For multiples of both three and five, the program will print "FizzBuzz"
"""

def check_value(x):
    if x%15 == 0:
        return "FizzBuzz"
    elif x%3==0:
        return "Fizz"
    elif x%5==0:
        return "Buzz"
    else:
        return str(x)

def main():
    print map(check_value, range(1,100))

if __name__ == '__main__':
    main()