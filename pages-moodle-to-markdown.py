from get_contents_api import *
import json
import time

main_url = 'https://moodle.catedu.es/course/view.php?id=7' # input('Introduce la url: ')
pattern = r'(mod/book|mod/page)' # input('Introduce la expresión regular: ')
pages = []

sources = get_items(main_url, pattern)

for source in sources:
    time.sleep(2)
    if 'mod/page' in source:
        page = get_moodle_page(source)
        pages.append(page)
    else:
        page = get_moodle_page(source)
        pages.append(page)
        sub_pages = get_moodle_book_chapters(source)
        for item in sub_pages:
            time.sleep(2)
            page = get_moodle_page(item)
            pages.append(page)

with open('outputfile.json', 'w') as fout:
    json.dump(pages, fout)