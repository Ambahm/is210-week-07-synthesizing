#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""


def get_party_stats(families, table_size=6):
    """Counts the number of people and tables needed.

    Args:
        families(nested lists): lists of families and their members.
        table_size(int): max number of seats at each table.

    Returns:
        Total number of guests and tables needed as a tuple.

    Examples:

        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']]
        , 2)
        (6, 4)
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']]
        , )
        (6, 3)

    """
    guests = 0
    tablesum = 0
    for members in families:
        guests += len(members)
        chairs = -(-len(members)//table_size)
        tablesum += chairs
    return (guests, tablesum)
