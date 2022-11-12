from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    if y < 0:
        x = 1/x
        y = -y

    prod = 1.
    while y:
        y, res = y//2, y % 2
        if res:
            prod *= x
        x = x*x

    return prod


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
