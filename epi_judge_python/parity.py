from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.

    parity = 0
    while x:
        parity = (parity + x & 1) % 2
        x >>= 1

    return parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
