#!/usr/bin/python3
from calculator_1 import sub, mul, div, add


def main():

    a = 10
    b = 5

    sum = add(a, b)
    minus = sub(a, b)
    times = mul(a, b)
    divide = div(a, b)

    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, minus))
    print("{} * {} = {}".format(a, b, times))
    print("{} / {} = {}".format(a, b, divide))


if __name__ == '__main__':
    main()
