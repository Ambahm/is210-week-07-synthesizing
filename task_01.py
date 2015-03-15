#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""This is a Party Organizer, Tables of 6 Members, 1 Family per table"""

def get_party_stats(families, table_size=6):
    headcount = 0
    table = 0
    for i in families:
        headcount += len(i)
        table = float(table_size)
    return headcount, table

print get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
