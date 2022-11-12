from test_framework import generic_test


def reverse_bits(x: int) -> int:
    s = f'{x:b}'
    s = '0'*(64 - len(s)) + s

    return int(s[::-1], 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
