import requests
from bs4 import BeautifulSoup
import sys
import re
import os
from os.path import basename, splitext
import fileinput
import json
from io import open as iopen
from slugify import slugify

# Lo primero que hay que hacer es descargarse la web en concreto y guardarla como 'gps.html'

PATH_FOR_BOOKS = str(os.getcwd() + '/books_pushed')
PATH_FOR_ARCHIVES_CREATED = str(os.getcwd() + '/books_to_push')
folder = input('Introduce la carpeta en la que guardar el curso: ') #input('Introduce el nombre de la carpeta para guardar el curso: ')
repo = input('Introduce el repo de github: ')

git_ignore_text = 'venv/\nnode_modules\n_book'
book_json_text= ('''{ "plugins": ["youtube", "accordion", "image-captions", "styled-blockquotes", "localized-footer"], '''
				'''"pluginsConfig": { "image-captions": { "caption": "Imagen - _CAPTION_" }, "localized-footer": { "hline": true, "filename": "./FOOTER.md" } } }''')

file = ''
with open('gps.html', 'r') as myfile:
	file = myfile.read()
soup = BeautifulSoup(file, 'html.parser')
tables = soup.find_all('table', {'class': 'generaltable'})
pages = {}

for i, table in enumerate(tables):
	page = {'archive': slugify(table.find('th').text) + '.md'}
	page['title'] = table.find('th').text
	page['html'] = str(table.find_all('tr')[1])
	page['questions'] = [x.text for x in table.find_all('tr')[3:]]
	pages[i] = page

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
with open('questions.txt', 'a') as fh_questions:
	for i in range(len(pages)):
		summary_text = f'* [{pages[i]["title"]}]({pages[i]["archive"]}' + ')\n'
		print(summary_text)
		fh_summary.write(summary_text)
		print(pages[i]['questions'])
		print(type(pages[i]['questions']))
		for question in range(len(pages[i]['questions'])):
			fh_questions.write(pages[i]['questions'][question])

	fh_summary.close()
files_list = ['README.md', 'SUMMARY.md']
with open('webs.json', 'w') as outfile:
	json.dump(pages, outfile)

os.system('cp ../../html-to-markdown.js .')
os.system('node html-to-markdown.js')
os.system('rm html-to-markdown.js')
os.system('rm webs.json')

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
