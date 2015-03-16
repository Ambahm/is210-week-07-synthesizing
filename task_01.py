#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1"""


def get_party_stats(families, table_size=6):
    """ Calculating how many people and tables.

    ARGS:
        families(list): names of the family.
        table_size(int): numbers of tables.

    RETURNS:
        how many people and how many tables in tuple

    EXAMPLES:
    >>> get_party_stats([['hihi', 'mimi'], ['wawa', 'lala',
    'chuchu'], ['meanie','hottie']])
    (7, 3)
    """

    total_guest = sum([len(names) for names in families])
    total_table = sum([-(-len(names) // table_size) for names in families])
    return (total_guest, total_table)
