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
        >>> myfunc(2, 3)
        ‘5, 3, Banana’

        >>> myfunc(1, 2, ‘Horse’)
        ‘3, 2, Horse’
    """
    letter = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    string = []
    for name, date in (appointments):
        return letter.format(name, date)
