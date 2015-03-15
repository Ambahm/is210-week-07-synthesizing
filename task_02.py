#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a Docstring"""

def prepare_email(appointments):
    body = ''
    for i in appointments:
        body += 'Dear{0:1},\nI look forward to meeting with you on{1:1}.\nBest,\nMe.'.format(i[0],i[1])
    return body

print prepare_email([('Bruno','June 3'),('Reeses','March 3')])
