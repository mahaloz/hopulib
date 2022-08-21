from typing import List, Generator
import itertools

def split_into_n_parts(lst: List, n: int) -> Generator:
    """
    Splits a list into approximately n parts with an equal amount of items in each sublist.

    :param lst:
    :param n:
    :return:
    """
    k, m = divmod(len(lst), n)
    return (lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def n_combinations(lst: List, n: int):
    lists = [
        lst for _ in range(n)
    ]
    return itertools.product(*lists)

def n_byte_combinations(n: int):
    lst = [b for b in range(256)]
    return n_combinations(lst, n)

def n_ascii_combinations():
    pass