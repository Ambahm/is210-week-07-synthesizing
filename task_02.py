#!usr/bin/env python
# *-* coding: utf-8 *-*
"""Doctstring"""

def prepare_email(appointments):
    """Creating a new client using their email

    Arg:
        appoitment(tuple): a tuple with client's name & appt time

    Return:
        client's info & appoitment time

    Example:
        >>>>>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """
    return n_appt

n_email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

n_appt = []

for info in appointments:
    n_appt.append(n_email.format(info[0], info[1]))
