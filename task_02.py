#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Email listing by taking tuples consiting of two parameters:
   name and appointment details.
"""


def get_email_data(appointments):
    """Returns an email listing for names and appointments.

    Args:
        appointment (mixed): It takes two parameters to create a list
                             patient name and appointment detail

    Returns:
        list: A list of emails created

    Examples:
        >>> get_email_data([('Hadi','2015'),('AA','MARCH 3')])
        ['Dear Hadi,\nI look forward to meeting with you on 2015.\nBest,\nMe',
         'Dear AA,\nI look forward to meeting with you on MARCH 3.\nBest,\nMe']

    """

    fmtstr = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    email_list = []                                     # Empty email list

    for mail in appointments:                           # Email body loop
        email_list.append(fmtstr.format(mail[0], mail[1])) # Append list

    return email_list                                    # New emails added
