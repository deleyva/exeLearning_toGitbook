from github import Github
import json
from time import sleep


def download_remotes(g_token):

    repos = []

    for repo in g_token.get_organization("catedu").get_repos():
        print(repo.name)
        repos.append(repo.git_url)

    return repos

g = Github("*************")

repos = download_remotes(g)

for element in repos:
    repo = g.get_repo(element[17:-4])
    try:
        book_json = repo.get_contents('book.json')
        book_json_decoded = json.loads(book_json.decoded_content)

        if 'ga' not in book_json_decoded['plugins']:
            book_json_decoded['plugins'].append('ga')
            book_json_decoded['pluginsConfig']['ga'] = {"token": "UA-135691041-2"}

            book_json_stringified = json.dumps(book_json_decoded, indent=2, ensure_ascii=False).encode('utf8')

            repo.update_file(book_json.path,"Añado Google Analytics", content=book_json_stringified, sha=book_json.sha, branch="master")
            print("{} actualizado".format(repo.name))
            sleep(3)
        else:
            print("El curso {} ya tiene el código de Analytics introducido".format(repo.name))

    except:
        print("El repo {} no tiene book.json".format(repo.name))




