#!usr/bin/env python
# *-* coding: utf-8 *-*
"""Doctstring"""

EMAIL = ()

def prepare_email(appointments):
    """Creating a new client using their email

    Arg:
        appointments(tuple): a tuple with client's name & appt time

    Return:
        client's info & appoitment time

    Example:
        >>>>>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """

    i = 0
    appointments = ()
    n_email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    return n_email

    for info in appointments:
        info = appointments[i]
        name = appointments.format(0)
        day = appointments.format(1)
        i += 1
        final_email = n_email.format(name, day)
        send_email = n_email.append(final_email)
        
    
