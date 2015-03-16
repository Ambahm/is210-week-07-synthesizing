#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program for automated emails"""


def prepare_email(appointments):
    """ A function to prepare email.

     Args:
        appointments (tuple): Name and date strings.

    Returns:
        str:  Merged letters.

    Examples:
        >>> prepare_email([('john', '05:16PM'), ('Wiley2', 'Monday')])
        ['Dear Wiley,\nI look forward to meeting with you on 05:16PM.
        \nBest,\nMe', 'Dear Wiley2,\nI look forward to meeting with
        you on Monday.\nBest,\nMe']

        >>> prepare_email([('Sal', '5PM'), ('Chick', 'Monday'), ('Tom', '6p')])
        ['Dear Sal,\nI look forward to meeting with you on 5PM.\nBest,\nMe',
        'Dear Chick,\nI look forward to meeting with you on Monday.\nBest,\nMe',
        'Dear Tom,\nI look forward to meeting with you on 6p.\nBest,\nMe']
    """
    letter = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    alltr = []
    for name, date in appointments:
        alltr.append(letter.format(name, date))
    return alltr
