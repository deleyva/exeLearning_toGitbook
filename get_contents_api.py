import requests
from bs4 import BeautifulSoup
import re

def get_items(url, pattern):
    '''
    Cojo los elementos que quiere scrapear de una web de curso de Moodle
    Parametros: url, expresión regular a encontrar
    Returns: lista de urls
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anclas = soup.find_all('a')
    sources = [ancla.get('href') for ancla in anclas if re.search(pattern, ancla.get('href')) is not None]
    return sources


def get_moodle_page(url):
    '''
    TODO Definir el objeto devuelto
    Devuelve un objeto con los siguientes atributos:
    * is_subchapter: número que definirá el tamaño de la indentación
    * tipo: si es página o libro
    * title: título para el summary
    * archive: nombre del archivo más .md
    * html: todo el html del contenido de la página
    
    Parametros: url

    Returns: un objeto con los contenidos de la página
    '''
    pass

def get_moodle_book_chapters(url):
    '''
    Si el curso contiene libros los subchapters son las páginas de ese libro.
    Parametros: url
    Returns: una lista urls.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    toc = soup.find('div', {'class':'book_toc_numbered'})
    anclas = toc.find_all('a')
    sources = [url + '&' + str(ancla.get('href')).split('&')[-1] for ancla in anclas]
    return sources


def data_to_json(lista):
    '''Genera un archivo .json con objetos que tienen cuatro atributos:
    * is_subchapter: número que definirá el tamaño de la indentación
    * tipo: si es página o libro
    * title: título para el summary
    * archive: nombre del archivo más .md
    * html: todo el html del contenido de la página
    '''
    pass

def summary_generation(jsonfile):
    '''
    Genera un archivo SUMMARY.md para gitbook
    '''
    pass
