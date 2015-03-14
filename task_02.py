#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A prepare email module"""

NEW_LIST = []


def prepare_email(appointments):
    """A prepare email funcion.

    Args:
        appointments: a list of two-item tuples with name and time.

    Return: a new list

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest, \nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest, \nMe']
    """
    i = 0
    for member in appointments:
        member = appointments[i]
        name = member[0]
        date = member[1]
        information = 'Dear {},\nI look forward to meeting with you \
on {}.\nBest, \nMe'.format(name, date)
        i += 1
        NEW_LIST.append(information)
    return NEW_LIST
