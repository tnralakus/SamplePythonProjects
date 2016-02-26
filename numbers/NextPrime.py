__author__ = 'alakus'

def is_prime(x):
    """
    Checks whether the given
    number x is prime or not
    """

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False

    return True

def find_next_prime(current_prime):
    """
   Returns the next prime
   after the currentPrime
   """
    next_prime = current_prime + 1
    while True:
        if not is_prime(next_prime):
            next_prime += 1
        else:
            break
    return next_prime


def main():  # Wrapper function
    current_prime = 2

    while True:

        answer = raw_input('Would you like to see the next prime? (Y/N) ')

        if answer.lower().startswith('y'):
            print(current_prime)
            current_prime = find_next_prime(current_prime)
        else:
            break

if __name__ == '__main__':
    main()