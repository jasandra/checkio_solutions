'''
You are given a string where you have to find its first word.
Input string consists of only english letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
'''


def first_word(text):
    text = text.split(' ')
    return text[0]


if __name__ == '__main__':
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
