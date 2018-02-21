#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
import os
from bs4 import BeautifulSoup

# Luego debes cambiar la url por 'url'
url = raw_input('Enter url: ')
os.system('image-scraper -s img ' + url)

files_list = ['README.md', 'contenidos.md']

replacements = {'&aacute;':'á', '&eacute;':'é', '&iacute;':'í', '&oacute;':'ó', '<strong>':'**', '</strong>':'**', '<'}

for file in files_list:
    tmp_file = str(file) + '1'
    file_name = str(file)
    with open(file) as infile, open(tmp_file, 'w') as outfile:
        for line in infile:
            if line.startswith('|<img'):
                imgTag = BeautifulSoup(line, 'lxml')
                imgTag = imgTag.find('img')
                img = imgTag.get('src')
                line = line.replace(line, '![' + img[:-4] + ']' + '(img/' + img + ')')
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            if line.startswith('Obra publicada con'):
                line = line.replace(line, '')
            outfile.write(line)
    infile.close()
    outfile.close()
    os.remove(file)
    os.rename(tmp_file, file_name)
        
        