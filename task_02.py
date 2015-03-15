#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a Docstring"""


def prepare_email(appointments):

    """Just some doc string for function.

    Arg:

    Return:

    Example:
    
    """
    output = []
    name = ''
    body = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe.'
    for i in appointments:
        name += body.format(i[0],i[1])
        output = [name]
    return output
