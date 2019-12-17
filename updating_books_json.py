from github import Github
import json

g = Github("*******")

repo = g.get_repo("catedu/ajedrez-en-la-escuela")
book_json = repo.get_contents('book.json')
book_json_decoded = json.loads(book_json.decoded_content)

if 'ga' not in book_json_decoded['plugins']:
    book_json_decoded['plugins'].append('ga')

book_json_decoded['pluginsConfig']['ga'] = {"token": "UA-*******-2"}

