#!/usr/bin/env python
# -*- coding: utf-8 *-*
"""This program calculates total guests and tables."""


def get_party_stats(families, table_size=6):
    """This function loops through a list, calculates a sum.

    Args:
        families(list): List or list of lists.
        table_size(int): Number of seats at table, default is 6.

    Returns:
        total_people(int): Total calculated number of guests.
        total_tables(int): Total number of tables for individual families.

    Example:
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'],
        ['Jem', 'Jack', 'Janis']])
        (6, 3)
    """

    total_people = 0
    total_tables = 0
    for member in families:
        total_people += len(member)
        seats = -(-len(member) // table_size)
        total_tables += seats

    return total_people, total_tables
