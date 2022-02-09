from bs4 import BeautifulSoup
import os
import sys
import re
from os.path import basename, splitext
import fileinput
import json

# find . -name "*elp" -exec mv {} . \;

EXES = str(os.getcwd() + '/exes')
HTMLS = f'{EXES}/Modulo_'
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
				num += 1
				elps.append(file)
	elps.sort()
	return num

def generate_html():
	for i in range(len(elps)):
		os.system('exe_do -s style=base -w exes/' + elps[i])
		os.system(f'exe_do -x website exes/{elps[i]} exes/Modulo_' + str((i + 1)) +
		          ' -f')

num_of_chapters = number_of_chapters(EXES)
generate_html()

webs = {}
counter = 0

for capitulo in range(num_of_chapters):
	url = HTMLS + str(capitulo + 1) + '/index.html'
	url_base = url[:-10]
	soup = None


	with open(url, 'r') as file:
		soup = BeautifulSoup(file, 'html.parser')

	title = soup.title.text

	if capitulo == 0:
		path = f'{PATH_FOR_ARCHIVES_CREATED}/{folder}'

		os.mkdir(path)
		os.chdir(path)
		os.mkdir(f'{path}/img')
		os.system('gitbook init')
		os.system('cp ../../book.json .')
		os.system('cp ../../FOOTER.md .')
		os.system('cp ../../crditos-buenos.md .')

		with open('.gitignore', 'w') as fh_gitigonre:
			fh_gitigonre.write(git_ignore_text)

		fh_summary = open('SUMMARY.md', 'a')
		fh_summary.write('____\n')	

	fh_summary.write(f'### {title}' + '\n')
	os.system(f'cp {HTMLS}' + str(capitulo + 1) + '/*.jpg img')
	os.system(f'cp {HTMLS}' + str(capitulo + 1) + '/*.png img')
	os.system(f'cp {HTMLS}' + str(capitulo + 1) + '/*.JPG img')
	os.system(f'cp {HTMLS}' + str(capitulo + 1) + '/*.gif img')
	try:
		os.system('rm img/icon_*')
	except Exception:
		pass
	try:
		os.system('rm img/Icon_*')
	except Exception:
		pass
	try:
		os.system('rm img/_style_*')
	except Exception:
		pass
	try:
		os.system('rm img/exe_*')
	except Exception:
		pass

	ulNum = 0
	li = 0
	uls = str(soup.find(id='siteNav'))

	for line in uls.splitlines():
		print(line)
		line = str(line)
		if line.startswith('<ul'):
			ulNum += 1

		if line.startswith('</ul>'):
			ulNum -= 1

		if line.startswith('<li'):
			li += 1
			line = BeautifulSoup(str(line), 'html.parser')
			link = line.find('a').get('href')
			item_title = line.find('a').text
			markdown_file = f'{link.split(".")[0]}.md'

			# Comienzo a escribir ficheros md
			if li == 1 or markdown_file in files_list:
				markdown_file = link.split('.')[0] + str(capitulo) + '.md'

			page = {'archive': markdown_file}
			file_url = url_base + link
			with open(file_url, 'r') as file_html:
				soup_file = BeautifulSoup(file_html, 'html.parser')
			page['html'] = str(soup_file.find(id='main'))
			webs[counter] = page
			counter += 1

			summary_text = ''
			if ulNum == 1:
				summary_text = f'* [{item_title}]({markdown_file}' + ')\n'
			elif ulNum == 2:
				summary_text = '	* [' + item_title + ']' + '(' + markdown_file + ')\n'
			if ulNum >= 3:
				summary_text = '		* [' + item_title + ']' + '(' + markdown_file + ')\n'

			fh_summary.write(summary_text)
			files_list.append(markdown_file)

fh_summary.close()
files_list.append('README.md')
files_list.append('SUMMARY.md')

with open('webs.json', 'w') as outfile:
    json.dump(webs, outfile)

os.system('cp ../../html-to-markdown.js .')
os.system('node html-to-markdown.js')
os.system('rm html-to-markdown.js')
os.system('rm webs.json')

replacements = {'í©':'é', '&hellip;':'...', '&Oacute;':'Ó', '&rdquo;':'"', '&ldquo;':'"', '&iquest;':'¿', '&uacute;':'ú', '&ntilde;':'ñ', '&nbsp;':'', 'í¡':'á','í³':'ó','<br />':'', 'Introduction':'Introducción','&aacute;':'á', '&eacute;':'é', '&iacute;':'í', '&oacute;':'ó', '<strong>':'**', '</strong>':'**', 'Ã³':'ó', 'Ã±':'ñ', 'Ã¡':'á', 'Ã©':'é', 'Ã':'í'}

for file in files_list:
	tmp_file = str(file) + '1'
	file_name = str(file)
	with open(file) as infile, open(tmp_file, 'w') as outfile:
		negrita = 0
		malaPuntuacion = [' !', ' .', ' ,', ' ?', ' \"', ' ']
		for line in infile:			
			if '![' in line:
				line = re.sub(r'(?!\[.*)\]\((?!http)', '](img/', line)
			else:
				for src, target in replacements.items():
					line = line.replace(src, target)

			# if 'youtube.com/embed/' in line:
			# 	youtubeString = re.findall(r'(www\.youtube\.com/embed/\S*)"', line)
			# 	youtubeStringStringed = youtubeString[0]
			# 	youtubeStringFixed = 'https//' + youtubeStringStringed
			# 	youtubeStringFixed = re.sub(r'embed/', 'watch?v=', youtubeStringFixed)
			# 	wholeLine = '{% youtube %}' + youtubeStringFixed + '{% endyoutube %}'
			# 	line = '\n' + wholeLine + '\n'

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
os.system(f'mv {folder} {PATH_FOR_BOOKS}')
os.chdir(f'{PATH_FOR_BOOKS}/{folder}')
os.system('gitbook install')
os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system(f'git remote add origin {repo}')
os.system('git push -u origin master')