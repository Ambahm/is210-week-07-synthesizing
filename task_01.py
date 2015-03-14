#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Analyze a list to return a total headcount for catering and tables."""

MEMBER = [['Angel', 'Micheal', 'Samuel'], ['Jennifer', 'James']]

def get_party_stats(families, table_size=6):
    
    """Get total headcount and table amounts for party.

    Args:
        families(list): family member
        table_size(int): number of tables, default=6
        
    Return:
        Provides how many members to cater to & tables needed

    Example:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
                            'Janis']])
            (6, 3)
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
                            'Janis']], 2)
            (6, 4)
    """
    return t_guest, t_tables

counter = 0
t_guest = 0
t_tables = 0

for fnum in families:
    for t_size in fnum:
        counter += 1
    tables += -(-len(fnum) // table_size)
    t_guest += counter
    t_tables += tables


