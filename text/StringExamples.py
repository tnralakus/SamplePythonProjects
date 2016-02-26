from text.StringUtil import StringUtil

__author__ = 'alakus'


def main():
    string = "a barbie vanquished the knights of the round table by hitting them in the face"
    print 'Our string is : ' + string
    util = StringUtil()
    print util.reverse(string)
    print util.count_vowels(string)
    print 'Is it a palindrome? ' + str(util.is_palindrome(string))
    print util.count_words(string)
    print util.find_in_iter(string)
    print util.piglatin(string)


if __name__ == '__main__':
    main()
