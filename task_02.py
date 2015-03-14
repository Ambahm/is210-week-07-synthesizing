#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 syn task_02"""


def prepare_email((appointments)):
    """a function to prepare email that takes one argument
    args:
        appointments(list): A list of two-item tuples with the client's name
                             and their appointment time as members
    return:
        new(list): Return new list of email formatted lists
    example:
    >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """

    new = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    news = []

    for appt in appointments:

        news.append(new.format(appt[0], appt[1]))

    return news
