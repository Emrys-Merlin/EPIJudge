from test_framework import generic_test


def reverse(x: int) -> int:

    sgn, x = (x < 0), abs(x)

    res = 0
    while x:
        digit, x = x % 10, x//10
        res = 10*res + digit

    return res * (-1)**sgn


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
