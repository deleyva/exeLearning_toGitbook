import requests
from bs4 import BeautifulSoup
url = 'http://formacion.educalab.es/course/view.php?id=516'
req = requests.get(url)
ims = soup.find('ul').find_all('li', {'class': 'activity imscp modtype_imscp'})
soup = BeautifulSoup(req.text, 'html.parser')
ims = soup.find('ul').find_all('li', {'class': 'activity imscp modtype_imscp'})
clear
print(soup)
clear
print(ims)
ims = soup.find_all('li', {'class': 'activity imscp modtype_imscp'})
print(ims)
ims = soup.find_all('li', {'class': 'modtype_imscp'})
print(ims)
for im in ims:
    print(im.find('href').text)
for im in ims:
    print(im.find('href'))
for im in ims:
    print(im)
ims = soup.find_all('a')
for a in ims:
    if 'imscp' in a[href]:
        print(a[href])
for a in ims:
    if 'imscp' in a['href']:
        print(a['href'])
for a in ims:
    if 'imscp' in a['href']:
        print(a['href'])
print([a['href'] for a in soup.find_all('a', href=True) if a.text])
print([a['href'] for a in soup.find_all('a', href=True) if str(a['href']).startswith('http://formacion.educalab.es/mod/imscp/')])
history
