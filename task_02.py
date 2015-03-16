#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2"""


def prepare_email(appointments):
    """Reminder email.

    Args:
        appointments(list): A list of two items, name & time.

    Returns:
        email(string): The email for each client.

    Examples:
    >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
    ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
    'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

    """

    email = []
    email_txt = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    for client in appointments:
        email.append(email_txt.format(client[0], client[1]))

    return email
