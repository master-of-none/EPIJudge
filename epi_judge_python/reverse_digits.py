from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    copy = abs(x)
    while copy:
        temp = copy % 10
        result = result * 10 + temp
        copy = copy // 10

    return result if x > 0 else -result 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
