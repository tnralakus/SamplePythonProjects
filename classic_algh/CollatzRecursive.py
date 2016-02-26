__author__ = 'alakus'


def collatz_recur(curNum, count=0):
    '''This recursively solves the Collatz Conjecture'''
    if curNum <= 1:  # Base case
        return count
    if curNum % 2 == 0:
        return collatz_recur(curNum / 2, count + 1)
    else:
        return collatz_recur(curNum * 3 + 1, count + 1)


def main():
    print collatz_recur(10)


if __name__ == "__main__":
    main()