#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from BeautifulSoup import *
import os
import sys
import re
import tomd
from os.path import basename, splitext
import fileinput
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from io import open as iopen
from slugify import slugify

def contar_capitulos():
    x = 0
    for root, dirs, files in os.walk(os.getcwd() + '/exes/'):
        for file in files:
            if file.endswith('.html'):
                x = x + 1
    return x

files_list = list()
path_for_books = os.getcwd() + '/libros_hechos/'
path_for_archives_created = os.getcwd() + '/libros/'
course_title = raw_input('Introduce el nombre del curso: ')

user_name = raw_input('Introduce tu usuario de Moodle: ')
user_password = raw_input('Introduce tu contraseña de Moodle: ')

payload = {
    "username":user_name,
    "password":user_password
}

paginas = ["http://moodle.catedu.es/mod/book/view.php?id=841&chapterid=4",
          "http://moodle.catedu.es/mod/book/view.php?id=841&chapterid=5",
          "http://moodle.catedu.es/mod/book/view.php?id=841&chapterid=6",
          "http://moodle.catedu.es/mod/book/view.php?id=841&chapterid=7",
          "http://moodle.catedu.es/mod/book/view.php?id=843&chapterid=8",
          "http://moodle.catedu.es/mod/book/view.php?id=843&chapterid=9",
          "http://moodle.catedu.es/mod/book/view.php?id=843&chapterid=10",
          "http://moodle.catedu.es/mod/book/view.php?id=843&chapterid=11"]

repo = raw_input('Introduce el repo de github: ')

with requests.Session() as session:
    post = session.post('http://moodle.catedu.es/login/index.php?', data=payload)

    for i, pagina in enumerate(paginas):
        pagina = session.get(pagina)
        soup = BeautifulSoup(pagina.text)
        title = soup('title')[0].text.encode('utf8')
        archivo = slugify(title) + '.md'
        content = str(soup.findAll('div', {'class': 'box generalbox book_content p-y-1'}, True)[0])
        images_urls = BeautifulSoup(content)
        images_urls = images_urls.findAll('img')
        # with requests.Session() as session:
        #     post = session.post('http://moodle.catedu.es/login/index.php?', data=payload)
        #     r = session.get(urls_de_capitulos[capitulo])
        #     print(r)
        #     html = r.text

        if i == 0:
            path = str(os.getcwd()) + '/libros/' + course_title

            os.mkdir(path)
            os.chdir(path)
            os.mkdir('img')

            os.system('gitbook init')
            fh_summary = open('SUMMARY.md', 'a')
            print('Ha entrado en el if')
            fh_json = open('book.json', 'a')
            fh_json.write('''{"plugins": ["youtube", "accordion", "image-captions"],"pluginsConfig": {"image-captions": {"caption": "Imagen - _CAPTION_"}}}''')
            fh_gitigonre = open('.gitignore', 'a')
            fh_gitigonre.write('''_book/\nnode_modules''')

            fh_json.close()
            fh_gitigonre.close()

        fh_summary.write('____\n')
        fh_summary.write('### ' + title + '\n')

        # imagen_de_la_hostia = images_urls[0]['src']
        for x in range(len(images_urls)):
            source = images_urls[x]['src']
            image_name = source.split('/')[-1]
            i = session.get(source)
            with iopen('img/' + image_name, 'wb') as file:
                file.write(i.content)
        mark = tomd.Tomd(content).markdown
        fh = open(archivo, 'a')
        fh.write(mark)
        fh.close()

        summary_text = '* [' + title + ']' + '(' + archivo + ')\n'

        fh_summary.write(summary_text)
        files_list.append(archivo)

fh_summary.close()
files_list.append('README.md')
files_list.append('SUMMARY.md')

replacements = {'í©':'é', '&hellip;':'...', '&Oacute;':'Ó', '&rdquo;':'"', '&ldquo;':'"', '&iquest;':'¿', '&uacute;':'ú', '&ntilde;':'ñ', '&nbsp;':'', 'í¡':'á','í³':'ó','<br />':'','Introduction':'Introducción','&aacute;':'á', '&eacute;':'é', '&iacute;':'í', '&oacute;':'ó', 'Ã³':'ó', 'Ã±':'ñ', 'Ã¡':'á', 'Ã©':'é', 'Ã':'í'}

for file in files_list:
    print(os.getcwd())
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

os.chdir(path_for_archives_created)
os.system('mv ' + course_title + ' ' + path_for_books)
os.chdir(path_for_books + '/' + course_title)
os.system('gitbook install')
os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system('git remote add origin ' + repo)
os.system('git push -u origin master')