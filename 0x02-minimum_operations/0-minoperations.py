#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" number that calculates the fewest number of operations needed to result"""


def minOperations(n):
    """ minOperations function """
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(int(n / i)) + i

    return 0
