'''
You are given the current stock prices. You have to find out which stocks cost more.
'''


def best_stock(data):
    max_price = 0
    result = ''
    for num in data:
        if data[num] > max_price:
            max_price = data[num]
            result = num
    return result


if __name__ == '__main__':
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
