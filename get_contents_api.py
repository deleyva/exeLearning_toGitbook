import requests
from bs4 import BeautifulSoup
import re
from slugify import slugify

def scrapying_function(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')

def get_course_title_folder(url):
    soup = scrapying_function(url)
    return slugify(soup.title.text[7:])

def get_items(url, pattern=''):
    '''
    Cojo los elementos que quiero scrapear de una web de curso de Moodle
    Parametros: url, expresión regular a encontrar
    Returns: lista de urls
    '''
    soup = scrapying_function(url)
    anclas = soup.find_all('a')
    return [
        ancla.get('href')
        for ancla in anclas
        if re.search(pattern, ancla.get('href')) is not None
    ]

def get_images(soup_object):
    '''
    Descarga todas las imágenes de una página a la carpeta ./img/
    '''
    content_soup = soup_object.find('div', {'role':'main'})
    images_urls = [img['src'] for img in content_soup.find_all('img')]
    urls_and_files = [(item,item.split('/')[-1]) for item in images_urls]
    for item in urls_and_files:
        url_r = requests.get(item[0])
        file = item[1]
        open('./img/{}'.format(file), 'wb').write(url_r.content)

def get_moodle_page(url, counter):
    '''
    Devuelve un objeto con los siguientes atributos:
    * tipo: si es página o libro
    * title: título para el summary
    * archive: nombre del archivo más .md
    * html: todo el html del contenido de la página
    
    Parametros: url, counter

    Returns: un objeto con los contenidos de la página
    '''
    page = {'id': counter, 'tipo': 'page' if 'mod/page' in url else 'book'}
    soup = scrapying_function(url)
    page['title'] = soup.title.text
    page['archive'] = slugify(soup.title.text) + '.md'
    page['html'] = str(soup.find('div', {'role':'main'}))
    get_images(soup)
    return page

def get_moodle_book_chapters(url):
    '''
    Si el curso contiene libros los subchapters son las páginas de ese libro.
    Parametros: url
    Returns: una lista urls.
    '''
    soup = scrapying_function(url)
    toc = soup.find('div', {'class':'book_toc_numbered'})
    anclas = toc.find_all('a')
    return [f'{url}&{str(ancla.get("href")).split("&")[-1]}' for ancla in anclas]

def summary_generation(list_of_dictionaries):
    '''
    Genera un archivo SUMMARY.md para gitbook
    '''
    dictionaries_sorted = sorted(list_of_dictionaries, key=lambda i: i['id'])
    list_of_pages = [[item['title'], item['archive']] for item in dictionaries_sorted]
    for item in list_of_pages:
        with open('SUMMARY.md', 'a') as summary:
            summary.write("* [{}]({})".format(item[0],item[1]))

