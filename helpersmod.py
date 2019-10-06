# -*- coding: utf-8 -*-
import re
import datetime
import numpy

re_non_word = re.compile(r'\W+')


def slug(s):
    return re.sub(re_non_word, '-', s).lower()
