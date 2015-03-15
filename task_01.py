#!/urs/bin/env python
# -*- coding: utf-8 -*-
"""This is a Party Organizer, Tables of 6 Members"""

families = [['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis'],['jack','prob']]


def get_party_stats(families, table_size=6):
    for i in families:
        families = len(i[:])
        print families

    
get_party_stats(families)
