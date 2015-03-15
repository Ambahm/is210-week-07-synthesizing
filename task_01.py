#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""This is a Party Organizer, Tables of 6 Members, 1 Family per table"""

def get_party_stats(families, table_size=6):
    """ Analyze arbitrary lists of families and returns total headcount, tables.

    Args:
    families (list of str): list of family members name by family.
    table_size (int): Maximum table seating capacity.
    headcount = 0
    table = 0

    Returns:
    tuple: total of headcount, total of tables needed.

    Examples:
    >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)

    >>> get_party_stats([['Jane','Rain'], ['Mary'],['Jess'], ['Jack']])
    (5, 4)
    """
    headcount = 0
    table = 0
    for i in families:
        headcount += len(i)
        table += -(-len(i)//table_size)
    return headcount, table
