#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from BeautifulSoup import *
import os
import sys
import re
import tomd
import progressbar
import codecs
from os.path import basename, splitext
import pdb
import fileinput
reload(sys)
sys.setdefaultencoding('utf8')

bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

files_list = list()
urls = list()
path_for_books = '/home/jesus/Documentos/libros'
path_for_archives_created = '/home/jesus/Documentos/exeLearning_toGitbook/libros'
course_title = raw_input('Introduce el nombre del curso: ')
repo = raw_input('Introduce el repo de github: ')

num_capitulos = 0
for root, dirs, files in os.walk(os.getcwd() + '/exes/'):
    for file in files:
        if file.endswith('.elp'):
            num_capitulos = num_capitulos + 1

for capitulo in range(num_capitulos):
	url = 'http://aularagon.catedu.es/materialesaularagon2013/exes/Modulo_' + str(capitulo + 1) + '/index.html'
	url_base = url[:-10]
	html = urllib.urlopen(url).read()

	soup = BeautifulSoup(html)

	# title = soup.find('li', {'id': 'active'})
	# title = title.contents[0]
	title = raw_input('Introduce el nombre del capítulo ' + str(capitulo+1) + ': ' )

	if capitulo == 0:
		path = str(os.getcwd()) + '/libros/' + course_title

		os.mkdir(path)
		os.chdir(path)

		os.system('gitbook init')
		fh_summary = open('SUMMARY.md', 'a')
		fh_json = open('book.json', 'a')
		fh_json.write('''{"plugins": ["youtube", "accordion"]}''')
		fh_gitigonre = open('.gitignore', 'a')
		fh_gitigonre.write('_book/')

		fh_json.close()
		fh_gitigonre.close()

	fh_summary.write('____\n')
	fh_summary.write('### ' + title + '\n')
	index = soup.findAll('div', {'id': 'siteNav'}, True)
	print index
	indexUp = BeautifulSoup(str(index))
	indexUp = str(indexUp.find('ul'))

	ulNum = 0
	li = 0

	for line in indexUp.splitlines():
		if line.startswith('<ul'):
			ulNum = ulNum + 1

		if line.startswith('</ul>'):
			ulNum = ulNum -1

		if line.startswith('<li'):
			li = li + 1
			line_searchable = BeautifulSoup(str(line))
			link = [tag.attrMap['href'] for tag in line_searchable.findAll('a', {'href': True})]
			enlace = None
			for lien in link:
				enlace = lien
			# pdb.set_trace()
			item_title = line_searchable.find(text=True)
			# item_title = item_title.decode('utf-8').encode('latin1').decode('utf-8').encode('utf-8')
			# print item_title
			archivo = enlace.split('.')[0] + '.md'

			# Comienzo a escribir ficheros md
			if li == 1 or archivo in files_list:
				archivo = enlace.split('.')[0] + str(capitulo) + '.md'


			url = url_base + enlace
			os.system('image-scraper -s img ' + url)
			html = urllib.urlopen(url).read()
			fh = open(archivo, 'a')
			soup = BeautifulSoup(html)
			content = str(soup.findAll('div', {'id': 'main'}, True))
			mark = tomd.Tomd(content).markdown
			fh.write(mark)
			fh.close()

			summary_text = ''
			if ulNum == 1:
				summary_text = '* [' + item_title + ']' + '(' + archivo + ')\n'
			if ulNum == 2:
				summary_text = '    * [' + item_title + ']' + '(' + archivo + ')\n'
			if ulNum >= 3:
				summary_text = '        * [' + item_title + ']' + '(' + archivo + ')\n'

			fh_summary.write(summary_text)
			files_list.append(archivo)

fh_summary.close()
files_list.append('README.md')
files_list.append('SUMMARY.md')

replacements = {'í©':'é', '&hellip;':'...', '&Oacute;':'Ó', '&rdquo;':'"', '&ldquo;':'"', '&iquest;':'¿', '&uacute;':'ú', '&ntilde;':'ñ', '&nbsp;':'', 'í¡':'á','í³':'ó','<br />':'', 'Introduction':'Introducción','&aacute;':'á', '&eacute;':'é', '&iacute;':'í', '&oacute;':'ó', '<strong>':'**', '</strong>':'**', 'Ã³':'ó', 'Ã±':'ñ', 'Ã¡':'á', 'Ã©':'é', 'Ã':'í'}

for file in files_list:
    tmp_file = str(file) + '1'
    file_name = str(file)
    with open(file) as infile, open(tmp_file, 'w') as outfile:
        negrita = 0
        malaPuntuacion = [' !', ' .', ' ,', ' ?', ' \"', ' ']
        for line in infile:            
            if '<img' in line and 'http' not in line:
                imgTag = BeautifulSoup(line)
                img = imgTag.find('img')
                img['src'] = 'img/' + img['src']
                line = str(imgTag)
                lineString = re.findall(r'(img/\S*)"', line)
                lineStringStringed = lineString[0]
                wholeLine = '![](' + lineStringStringed + ')'
                line = wholeLine
            elif '<img' in line and 'http' in line:
                lineString = re.findall(r'src="(\S*)"', line)
                lineStringStringed = lineString[0]
                wholeLine = '![](' + lineStringStringed + ')'
                line = wholeLine
            else:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
            
            if 'youtube.com/embed/' in line:
                youtubeString = re.findall(r'(www\.youtube\.com/embed/\S*)"', line)
                youtubeStringStringed = youtubeString[0]
                youtubeStringFixed = 'https//' + youtubeStringStringed
                youtubeStringFixed = re.sub(r'embed/', 'watch?v=', youtubeStringFixed)
                wholeLine = '{% youtube %}' + youtubeStringFixed + '{% endyoutube %}'
                line = '\n' + wholeLine + '\n'
			
            if line.startswith('Obra publicada con'):
                line = line.replace(line, '')

            if '![' in line:
                line = '\n' + line + '\n'

            # bar.start()
            # for i in range(len(line)):
            #     if i > 1:
            #         # enciendo negritas normales
            #         if line[i-2:i+1] == ' **' and negrita == 0:
            #             negrita = 1
            #         # apago negritas normales
            #         elif line[i-2:i+1] == '** ' and negrita == 1:
            #             negrita = 0
            #         # enciendo negritas con espacio antes del lineo
            #         elif line[i-2:i+1] == '** ' and negrita == 0:
            #             negrita = 1
            #             line = line[:i-2] + ' ' + line[i-1:]
            #             line = line[:i-1] + '*' + line[i:]
            #             line = line[:i] + '*' + line[i+1:]
            #         # apago negritas con espacio despues del lineo
            #         elif line[i-2:i+1] == ' **' and negrita == 1:
            #             negrita = 0
            #             line = line[:i-2] + '*' + line[i-1:]
            #             line = line[:i-1] + '*' + line[i:]
            #             line = line[:i] + ' ' + line[i+1:]
            #             print(negrita)
            #         # elimino el espacio antes de un signo de puntuacion
            #         elif line[i-1:i+1] in malaPuntuacion:
            #             line = line[:i-1] + '' + line[i:]
            #             try:
            #                 line = line[:i] + line[i] + line[i+1:]
            #             except:
            #                 pass
            # bar.finish()
            outfile.write(line)
    infile.close()
    outfile.close()
    os.remove(file)
    os.rename(tmp_file, file_name)

pasado_a_repo = 'No'
while pasado_a_repo != 'Sí':
    	pasado_a_repo = raw_input('¿Has creado el repo en github? ')

os.chdir(path_for_archives_created)
os.system('mv ' + course_title + ' ' + path_for_books)
os.chdir(path_for_books + '/' + course_title)
os.system('gitbook install')
os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system('git remote add origin ' + repo)
os.system('git push -u origin master')