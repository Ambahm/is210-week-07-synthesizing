#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Just a Docstring"""

def prepare_email(appoitments):
    appointments = [(),()]
    body = 'Dear{0},\nI look forward to meeting with you on{0}.\nBest,\nMe'
    for i in appointments:
        appointments = body.format(i[0:])
        print appointments
print prepare_email([('Bruno','2015'),('Reeses','March 3')])
