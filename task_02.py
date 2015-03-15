#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module returns a list of names and appointment times as email list"""


def prepare_email(appointments):
    """Takes client name/time and returns list of reminder email.

    Args:
    appointments (list of tuple):List of two item tuple, name/appointment time.

    Returns:
    email (list of string): List containig name and appointment time.

    Examples:
    >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
    ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
    'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

   >>> prepare_email([('Jane', '2016'), ('Mitch', 'June 2')])
    ['Dear Jane,\nI look forward to meeting with you on 2016.\nBest,\nMe',
    'Dear Mitch,\nI look forward to meeting you on June 2.\nBest\nMe']
    """
    email = []
    body = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for i in appointments:
        email += [body.format(i[0], i[1])]
    return email
