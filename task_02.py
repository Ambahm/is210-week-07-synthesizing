#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK7 synthesizing task_02 - Email reminders."""


def prepare_email(appointments):
    """Automating a reminder email to clients.

    Args:
        appointments(list): A list of two-item tuples with the client's
        name and their appointment time.
    Returns:
        email(string): The actual email body for each client.

    Examples:
    >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
    ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
    'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

    >>> prepare_email([('Dan', 'Monday, March 03, 2015 at 11 AM'), (
    'Mr. Hightower', 'Wednesday, April 06, All Day Meeting')])
    ['Dear Dan,\nI look forward to meeting with you on Monday, March 03, 2015
    at 11 AM.\nBest,\nMe', 'Dear Mr. Hightower,\nI look forward to meeting
    with you on Wednesday, April 06, All Day Meeting.\nBest,\nMe']

    """

    email = []
    email_txt = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    for client in appointments:
        email.append(email_txt.format(client[0], client[1]))
    return email
