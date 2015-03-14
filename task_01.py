#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A get_party_status function"""

DATA = []


def get_party_stats(families, table_size=6):
    """Do some math and get family member number and table number.

    Args:
        families(list): A list of family members.
        table_size(int): A number, default is 6.

    Return: a tuple

    Examples:
        >>> get_party_stats([['Hugo', 'Horace', 'Helen', 'Hesther'],
               ['Finnegan', 'Florance', 'Foster'],
               ['Jim', 'Jen', 'Jill', 'Justin', 'Janice', 'Jacob', 'Megatron']])
        (14, 4)
    """
    i = 0
    total_member = 0
    total_table = 0
    for family in families:
        family = families[i]
        total_member += len(family)
        total_table += (-(-len(family)//table_size))
        i += 1
    DATA.append(total_member)
    DATA.append(total_table)
    return tuple(DATA)
