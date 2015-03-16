#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Analyze a list to return a total headcount for catering and tables."""

PARTY = ()

def get_party_stats(families, table_size=6):
    """Get total headcount and table amounts for party.

    Args:
        families(list): a list of family members
        table_size(int): number of tables, default=6
        
    Return:
        Provides how many members to cater to & tables needed

    Example:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
                            'Janis'])
            (6, 3)
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
                            'Janis'], 2)
            (6, 4)
    """
    i = 0
    t_member = 0
    t_table = 0
    for party in families:
        i += 1
        t_member = len(party)
        t_table = (-(-len(party) // table_size))
        return (t_member, t_table)
