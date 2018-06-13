import requests
from bs4 import BeautifulSoup
import sys
import re
import os
from os.path import basename, splitext
import fileinput
import json
from io import open as iopen

PATH_FOR_BOOKS = str(os.getcwd() + '/books_pushed')
PATH_FOR_ARCHIVES_CREATED = str(os.getcwd() + '/books_to_push')
files_list = list()
folder = input('Introduce la carpeta en la que guardar el curso: ') #input('Introduce el nombre de la carpeta para guardar el curso: ')
repo = input('Introduce el repo de github: ')
url = input('Introduce la url del curso: ')

git_ignore_text = 'venv/\nnode_modules\n_book'
book_json_text= ('''{ "plugins": ["youtube", "accordion", "image-captions", "styled-blockquotes", "localized-footer"], '''
				'''"pluginsConfig": { "image-captions": { "caption": "Imagen - _CAPTION_" }, "localized-footer": { "hline": true, "filename": "./FOOTER.md" } } }''')

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
ims = soup.find_all('a')
chapters = [a['href'] for a in soup.find_all('a', href=True) if str(a['href']).startswith('http://formacion.educalab.es/mod/imscp/')]
# Para el intef http://formacion.educalab.es/mod/imscp/
# Para Aularagón http://moodle.catedu.es/mod/imscp/

webs = {}
counter = 0
equals = 0
print(chapters)

for i, capitulo in enumerate(chapters):
	print(capitulo)
	req_capitulo = requests.get(str(capitulo))
	soup_capitulo = BeautifulSoup(req_capitulo.text, 'html.parser')
	
	title = soup_capitulo.title.text

	if i == 0:
		path = PATH_FOR_ARCHIVES_CREATED + '/' + folder

		os.mkdir(path)
		os.chdir(path)
		os.mkdir(path + '/img')
		os.system('gitbook init')
		os.system('cp ../../book.json .')
		os.system('cp ../../FOOTER.md .')
		os.system('cp ../../crditos-buenos.md .')

		with open('.gitignore', 'w') as fh_gitigonre:
			fh_gitigonre.write(git_ignore_text)

		fh_summary = open('SUMMARY.md', 'a')
		fh_summary.write('____\n')	

	fh_summary.write('### ' + title + '\n')

	ulNum = 0
	li = 0
	lines = soup_capitulo.find('div', {'id': 'imscp_toc'}, True)
	uls = soup_capitulo.find('div', {'id': 'imscp_toc'}, True).findAll('a')
	a_s = 0


	for line in lines.prettify().splitlines():
		line = str(line).strip()
		if line.startswith('<ul') and not None:
			ulNum = ulNum + 1

		if line.startswith('</ul>'):
			ulNum = ulNum -1

		if line.startswith('<li'):
			page = {}
			li = li + 1
			link = uls[a_s].get('href')
			item_title = uls[a_s].text
			markdown_file = link.split('/')[-1]
			markdown_file = markdown_file.split('.')[0] + '.md'
			a_s = a_s + 1

			# Comienzo a escribir ficheros md
			if markdown_file in files_list:
				markdown_file = markdown_file.split('.')[0] + str(equals) + '.md'
				equals = equals + 1
				
			page['archive'] = markdown_file

			file_html = requests.get(link)
			file_html.encoding = 'utf-8'
			soup_file = BeautifulSoup(file_html.text, 'html.parser')
			page['html'] = str(soup_file.find(id='main'))
			webs[counter] = page
			counter = counter + 1

			# Descargo las imágenes
			url_base = link.split('/')[0:-1]
			url_base = '/'.join(url_base)
			images = soup_file.find_all('img')
			for x in range(len(images)):
				source = images[x]['src']
				if source.startswith('htt'):
					image_name = source.split('/')[-1]
					i = requests.get(source)
					with iopen('img/' + image_name, 'wb') as file:
						file.write(i.content)
				elif source != None:
					image_name = source
					i = requests.get(url_base + '/' + source)
					with iopen('img/' + image_name, 'wb') as file:
						file.write(i.content)
			


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
os.system('mv ' + folder + ' ' + PATH_FOR_BOOKS)
os.chdir(PATH_FOR_BOOKS + '/' + folder)
os.system('gitbook install')
os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system('git remote add origin ' + repo)
os.system('git push -u origin master')
