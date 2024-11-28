#!/usr/bin/python3


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total

    Args:
        coins (list): a list of coin denominations
        total (int): the total amount of money

    Returns:
        int: the fewest number of coins needed
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total == 0:
        return count
    else:
        return -1
