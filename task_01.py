#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK7 synthesizing task_01 - Party planing."""


def get_party_stats(families, table_size=6):
    """Counts the number of people at a party and the tables necessary to
    seat them.

    Args:
        families(tuple): The people attending the party.
        table_size(int): The max number of people at a table.
    Returns:
        total_guest(int): The total number of people attending
        total_table(int): The total tables needed to seat everyone.

    Examples:
    >>> get_party_stats([['Jess', 'Mike', 'Tina', 'Simon', 'Felix'],
    ['Vinnie', 'Brian'], ['Des']])
    (8, 3)

    >>> get_party_stats([['Jess', 'Mike', 'Tina', 'Simon', 'Felix'],
    ['Vinnie', 'Brian'], ['Des'], ['Hochi'], ['Grace']], 2)
    (10, 7)

    """
    total_guest = sum([len(names) for names in families])
    total_table = sum([-(-len(names) // table_size) for names in families])
    return (total_guest, total_table)
