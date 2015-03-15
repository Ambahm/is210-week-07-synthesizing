#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a Docstring"""


def prepare_email(appointments):
    """ Just some docstring sample
    Arg:
    Return:
    Example:
    
    """
    email = []
    body = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for i in appointments:
        email += [body.format(i[0], i[1])]
    return email
