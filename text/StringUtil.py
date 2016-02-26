__author__ = 'alakus'


class StringUtil():
    def reverse(self, some_seq):
        """
            Input:     Sequence
            output:    Sequence:
                         reversed version
        """
        return some_seq[::-1]

    def count_vowels(self, string):
        """
            @param string:   String
            @return:         Integer:
                                No. of vowels or 0
        """
        vowels = "aeiou"
        count = {char: 0 for char in vowels}
        for char in string:
            if char in vowels:
                count[char] += 1
        return count

    def is_palindrome(self, some_seq):
        """
            @param some_seq: sequence of anything
            @return:         Boolean:
                        palindrome check of sequence passed
        """
        return some_seq == self.reverse(some_seq)

    def count_words(self, string=None, file=None):
        """
            @param string:    A string
            @param file:      A file to be read
        """
        word_count = 0
        if string:
            word_count = len(string.split())
        if file:
            with open(file) as f:
                word_count = len(f.read().split())
        return word_count

    def find_in_iter(self, some_iter):
        """
        just an example for someone.
        """
        if isinstance(some_iter, str):
            cond = lambda sequence, string: [char for char in string if char in sequence]
            vowels = ("a,e,i,o,u")
            return [word for word in some_iter.lower().split(" ") if len(cond(vowels, word)) > 1]
        elif isinstance(some_iter, int):
            return [num for num in str(some_iter) if num > 5]

    def piglatin(self, some_iter):
        """
        Pig Latin : Pig Latin is a game of alterations played on the English language game.
        To create the Pig Latin form of an English word the initial consonant sound is transposed
        to the end of the word and an ay is affixed
        (Ex.: banana would yield anana-bay).
        """
        vowels = ("a,e,i,o,u")
        return reduce(lambda word1, word2: word1 + ' ' + word2, map(
            lambda word: (word[1::] + word[0] + 'ay') if len(word) > 2 and word[0] not in vowels else word + 'ay',
            some_iter.strip().split(' ')))


