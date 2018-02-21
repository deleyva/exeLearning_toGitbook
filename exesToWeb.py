#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# Con los .elp descargados en la carpeta 'exes'
# les establece la plantilla 'base' a todos y
# los exporta a formato web.

elps = []
for root, dirs, files in os.walk(os.getcwd() + '/exes/'):
    for file in files:
        if file.endswith('.elp'):
            elps.append(file)

elps.sort()
print elps
# for i in range(len(elps)):
#     new_name = str(i + 1) + '.elp'
#     os.system('mv ' + elps[i] + ' ' + new_name)
#     elps[i] = new_name
#     print elps[i]


os.chdir('exes')
for i in range(len(elps)):
    os.system('exe_do -s style=base -w ' + elps[i])
    os.system('exe_do -x website ' + elps[i] + ' Modulo_' + str((i+1)) + ' -f')