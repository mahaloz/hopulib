from typing import List, Generator


def split_into_n_parts(lst: List, n: int) -> Generator:
    """
    Splits a list into approximately n parts with an equal amount of items in each sublist.

    :param lst:
    :param n:
    :return:
    """
    k, m = divmod(len(lst), n)
    return (lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

