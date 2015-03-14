#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" week 7 syn  task_01"""

# table_size = 6


def get_party_stats(families, table_size=6):
    """a function that takes two parameters: families and table_size
    Args:
        families (List): list of families which are,themselves,lists of members
        table_size (int): number of seats at each table, defaults to six (6)
    return:
        return tuple of total number of guests and number of tables

    example:
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'],
                            ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats([['Jan'], ['Jen', 'Jess'],
                            ['Jem', 'Jack', 'Janis']],2)
        (6, 4)
        >>> get_party_stats(data.get_party_list())
        (1118, 263)
    """

    counter = 0
    total_guest = 0
    total_tables = 0
    tables = 0

    for fam in families:
        for size in fam:
            counter += 1
        tables += -(-len(fam) // table_size)
    total_guest += counter
    total_tables += tables
    return total_guest, total_tables
