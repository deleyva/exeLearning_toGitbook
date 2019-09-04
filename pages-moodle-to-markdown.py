from get_contents_api import *
import json
import time
import os

PATH_FOR_BOOKS = str(os.getcwd() + '/books_pushed')
PATH_FOR_ARCHIVES_CREATED = str(os.getcwd() + '/books_to_push')

main_url = 'https://moodle.catedu.es/course/view.php?id=7' # input('Introduce la url: ')
pattern = r'(mod/book|mod/page)' # input('Introduce la expresión regular: ')
# repo = input('Introduce el repo de github: ')
pages = []

# Creo las carpetas y copio los archivos básicos
folder = get_course_title_folder(main_url)
path = PATH_FOR_ARCHIVES_CREATED + '/' + folder
os.mkdir(path)
os.chdir(path)
os.mkdir(path + '/img')
os.system('gitbook init')
os.system('cp ../../book.json .')
os.system('cp ../../.gitignore .')
os.system('cp ../../FOOTER.md .')
os.system('cp ../../crditos-buenos.md .')

sources = get_items(main_url, pattern)

counter = 0

for source in sources:
    time.sleep(2)
    if 'mod/page' in source:
        page = get_moodle_page(source, counter)
        pages.append(page)
        counter += 1
    else:
        page = get_moodle_page(source, counter)
        pages.append(page)
        counter += 1
        sub_pages = get_moodle_book_chapters(source)
        for item in sub_pages:
            time.sleep(2)
            page = get_moodle_page(item, counter)
            pages.append(page)
            counter += 1

with open('outputfile.json', 'w', encoding='utf8') as fout:
    json.dump(pages, fout, ensure_ascii=False)

summary_generation(pages)