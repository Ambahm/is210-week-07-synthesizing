#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a Docstring"""


def prepare_email(appointments):

    """Just some doc string for function.

    Arg:

    Return:

    Example:
    
    """
    output =[]
    email = ''
    body = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe.'
    for i in appointments:
        email += body.format(i[0],i[1])
        output.append(email)
    return output
prepare_email([('Jen', '2015'), ('Max', 'March 3')])
