#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Party planning program"""


def get_party_stats(families, table_size=6):
    """ A def docstring.

    Args:
        families (list): List of families.
        table_size (int): Number of seats at table.

    Returns:
        tuple:  (total number of guest, total number of tables).

    Examples:
        >>> get_party_stats([['a', 'b', 'c'], ['be', 'ce'], ['b', 'c', 'd']],2)
        (8, 5)

        >>> get_party_stats([['a', 'b', 'c'], ['be'], ['b', 'c', 'd']],2)
        (7, 5)
    """
    count = 0
    ele = 0

    for name in families:
        tcount = -(-len(name) // table_size)
        ele += tcount
        for item in name:
            count += 1
    return (count, ele)
