#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i in range(len(sieve)) if sieve[i]]
    c = 0
    for i in range(x):
        for j in sieve:
            if j <= nums[i]:
                c += 1
        if c % 2 == 0:
            return "Ben"
        else:
            return "Maria"
