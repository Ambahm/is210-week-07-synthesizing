#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to count total of guests and tables required"""

def get_party_stats(families, table_size=6):
    """ This fnction returns guest total and tables required,
        takes two parameters: families and table_size

    Args:
        families (List): list of families which are,themselves,lists of members
        table_size (int): number of seats at each table, max seating is = 6

    Return:
        tuple: Total number of guests and number of tables required

    Example:
       >>> get_party_stats([('Hugo', 'Horace', 'Helen', 'Hesther'),
       ('Finnegan', 'Florance', 'Foster'),('Jim', 'Jen', 'Jill',
       'Justin', 'Janice', 'Jacob', 'Megatron')])
        (14, 4)

        >>> get_party_stats(data.get_party_list())
        (161, 31)

    """
    total_guest = 0
    max_table = 0
    guest_list = []
    index = 0


    for families[index] in families:        #[(0:1,0:2), (1:0)]

        for family in families[index]:
            guest_list.append(family)
            total_guest = len(guest_list)

        if families[index] > table_size:
            max_table += 1
        index += 1

    max_table += -(-len(families) // table_size)

    return total_guest, max_table






