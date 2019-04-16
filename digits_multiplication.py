'''
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
'''


def checkio(number):
    result = 1
    number = str(number)
    for num in number:
        s = int(num)
        if s == 0:
            continue
        result *= s
    return result


if __name__ == '__main__':
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
