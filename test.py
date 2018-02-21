#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
import os
from BeautifulSoup import *


line = '|<img style="display: block; margin-left: auto; margin-right: auto;" src="article.jpg" height="180" width="320" />'
imgTag = BeautifulSoup(line)
imgTag = imgTag.find('img')
print imgTag
img = imgTag.get('src')
print img
line = line.replace(line, '![' + img[:-4] + ']' + '(img/' + img + ')')
print line