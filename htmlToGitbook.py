import requests
import os
import sys
import re
import tomd
from os.path import basename, splitext
import fileinput
import helpers
reload(sys)
sys.setdefaultencoding('utf8')

files_list = list()
urls = list()
PATH_FOR_BOOKS = str(getcwd()) + '/books_to_push'
PATH_FOR_ARCHIVES_CREATED = str(getcwd()) + '/books_pushed'
course_title = input('Introduce el nombre del curso: ')
repo = input('Introduce el repo de github: ')

num_of_chapters = helpers.number_of_chapters()

for capitulo in range(num_of_chapters):
	url = 'http://aularagon.catedu.es/materialesaularagon2013/exes/Modulo_' + str(capitulo + 1) + '/index.html'
	url_base = url[:-10]
	html = urllib.urlopen(url).read()

	soup = BeautifulSoup(html)

	# title = soup.find('li', {'id': 'active'})
	# title = title.contents[0]
	title = raw_input('Introduce el nombre del capítulo ' + str(capitulo+1) + ': ' )

	if capitulo == 0:
		helpers.start_book()
    fh_summary = open('SUMMARY.md', 'a')
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
                
            outfile.write(line)
    infile.close()
    outfile.close()
    os.remove(file)
    os.rename(tmp_file, file_name)

pasado_a_repo = 'No'
while pasado_a_repo != 'Sí':
    	pasado_a_repo = raw_input('¿Has creado el repo en github? ')

os.chdir(PATH_FOR_ARCHIVES_CREATED)
os.system('mv ' + course_title + ' ' + PATH_FOR_BOOKS)
os.chdir(PATH_FOR_BOOKS + '/' + course_title)
os.system('gitbook install')
os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system('git remote add origin ' + repo)
os.system('git push -u origin master')