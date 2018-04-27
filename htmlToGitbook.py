from bs4 import BeautifulSoup
import os
import sys
import re
import tomd
from os.path import basename, splitext
import fileinput


EXES = str(os.getcwd() + '/exes')
HTMLS = EXES + '/Modulo_'
PATH_FOR_BOOKS = str(os.getcwd() + '/books_pushed')
PATH_FOR_ARCHIVES_CREATED = str(os.getcwd() + '/books_to_push')
files_list = list()
folder = input('Introduce la carpeta en la que guardar el curso: ') #input('Introduce el nombre de la carpeta para guardar el curso: ')
repo = input('Introduce el repo de github: ')

git_ignore_text = 'venv/\nnode_modules\n_book'
book_json_text= ('''{ "plugins": ["youtube", "accordion", "image-captions", "styled-blockquotes", "localized-footer"], '''
				'''"pluginsConfig": { "image-captions": { "caption": "Imagen - _CAPTION_" }, "localized-footer": { "hline": true, "filename": "./FOOTER.md" } } }''')
elps = []

def number_of_chapters(folder):
	num = 0
	for root, dirs, files in os.walk(folder):
		for file in files:
			if file.endswith('.elp'):
				num = num + 1
				elps.append(file)
	elps.sort()
	return num

def generate_html():
	for i in range(len(elps)):
		os.system('exe_do -s style=base -w exes/' + elps[i])
		os.system('exe_do -x website exes/' + elps[i] + ' exes/Modulo_' + str((i+1)) + ' -f')

num_of_chapters = number_of_chapters(EXES)
generate_html()

for capitulo in range(num_of_chapters):
	url = HTMLS + str(capitulo + 1) + '/index.html'
	url_base = url[:-10]
	soup = None

	
	with open(url, 'r') as file:
		soup = BeautifulSoup(file, 'html.parser')
	
	title = soup.title.text

	if capitulo == 0:
		path = PATH_FOR_ARCHIVES_CREATED + '/' + folder

		os.mkdir(path)
		os.chdir(path)
		os.mkdir(path + '/img')
		os.system('gitbook init')
		with open('book.json', 'w') as book_json:
			book_json.write(book_json_text)

		with open('.gitignore', 'w') as fh_gitigonre:
			fh_gitigonre.write(git_ignore_text)

		fh_summary = open('SUMMARY.md', 'a')
		fh_summary.write('____\n')	

	fh_summary.write('### ' + title + '\n')
	os.system('cp ' + HTMLS + str(capitulo + 1) + '/*.jpg img')
	os.system('cp ' + HTMLS + str(capitulo + 1) + '/*.png img')
	os.system('cp ' + HTMLS + str(capitulo + 1) + '/*.JPG img')
	os.system('cp ' + HTMLS + str(capitulo + 1) + '/*.gif img')
	os.system('rm img/icon_*')
	os.system('rm img/Icon_*')
	os.system('rm img/_style_*')
	os.system('rm img/exe_*')	

	ulNum = 0
	li = 0
	uls = str(soup.find(id='siteNav'))

	for line in uls.splitlines():
		print(line)
		line = str(line)	
		if line.startswith('<ul') and not None:
			ulNum = ulNum + 1

		if line.startswith('</ul>'):
			ulNum = ulNum -1

		if line.startswith('<li'):
			li = li + 1
			line = BeautifulSoup(str(line), 'html.parser')
			link = line.find('a').get('href')
			item_title = line.find('a').text
			markdown_file = link.split('.')[0] + '.md'

			# Comienzo a escribir ficheros md
			if li == 1 or markdown_file in files_list:
				markdown_file = link.split('.')[0] + str(capitulo) + '.md'

			fh = open(markdown_file, 'a')
			file_url = url_base + link
			with open(file_url, 'r') as file_html:
				soup_file = BeautifulSoup(file_html, 'html.parser')
			content = str(soup_file.find(id='main'))
			mark = tomd.Tomd(content).markdown
			fh.write(mark)
			fh.close()

			summary_text = ''
			if ulNum == 1:
				summary_text = '* [' + item_title + ']' + '(' + markdown_file + ')\n'
			if ulNum == 2:
				summary_text = '	* [' + item_title + ']' + '(' + markdown_file + ')\n'
			if ulNum >= 3:
				summary_text = '		* [' + item_title + ']' + '(' + markdown_file + ')\n'

			fh_summary.write(summary_text)
			files_list.append(markdown_file)

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
				imgTag = BeautifulSoup(line, 'html.parser')
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
				for src, target in replacements.items():
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
		pasado_a_repo = input('¿Has creado el repo en github? ')

os.chdir(PATH_FOR_ARCHIVES_CREATED)
os.system('mv ' + folder + ' ' + PATH_FOR_BOOKS)
os.chdir(PATH_FOR_BOOKS + '/' + folder)
os.system('gitbook install')
os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system('git remote add origin ' + repo)
os.system('git push -u origin master')