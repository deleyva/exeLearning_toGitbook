import os
import re
import json
from itertools import islice
import time
from github import Github


def download_remotes():
    g = Github("************")

    repos = []

    for repo in g.get_organization("catedu").get_repos():
        print(repo.name)
        repos.append(repo.git_url)

    return repos



def get_remotes(path):
    """
    Devuelve un tuple con:
    * el tipo de repo (https o git) 
    * el nombre (abies-administrador.git)
    """
    dirs = os.scandir(path)
    remotes = []
    pattern = re.compile(r"(https:\/\/github.com\/catedu\/|git@github\.com:catedu\/)(.*\.git|) \(fetch\)", re.DOTALL)
    print(dirs)
    for entry in dirs:
        try:
            os.chdir(entry.path)
            remote = os.popen('git remote -v').read()
            remote_tupple = pattern.findall(remote)[0]
            remotes.append(remote_tupple)
            os.chdir(path)
        except:
            continue

            ## print("Not a directory")
    return remotes
    
def update_locals(path):
    """
    Trae todos los cambios remotos de los
    repos que tengo en local
    """
    dirs = os.scandir(path)
    for entry in dirs:
        try:
            os.chdir(entry.path)
            check = os.popen('git pull').read()
            if check != 'Already up-to-date.\n':
                print(entry.path)
        except:
            print("Not a directory")


# def update_plugins(path):
#     """
#     Actualiza los plugins que indiquemos,
#     dentro de la función por ahora
#     """
#     dirs = os.scandir(path)
#     repos = []
#     remotes = []
#     pattern = re.compile(r"(git@github\.com:catedu\/)(.*\.git|) \(fetch\)", re.DOTALL)
#     for entry in islice(dirs, 15, 92):
#         try:
#             os.chdir(entry.path)
#             remote = os.popen('git remote -v').read()
#             remote_tupple = pattern.findall(remote)[0]
#             name = remote_tupple[1][:-4]
#             base = 'https://github.com/catedu/' + name + '/edit/master'
#             with open("book.json", 'r', encoding='utf-8') as file:
#                 dict_book = json.load(file)
                    
#             plugins = ["edit-link", "githubcontributors"]
#             for plugin in plugins:
#                 if plugin not in dict_book["plugins"]:
#                     dict_book["plugins"].append(plugin)

#             dict_book["pluginsConfig"] = dict_book.get("pluginsConfig", {})
#             dict_book["pluginsConfig"]["edit-link"] = dict_book["pluginsConfig"].get("edit-link", {})
#             dict_book["pluginsConfig"]["edit-link"]["base"] = dict_book["pluginsConfig"]["edit-link"].get("base", base)
#             dict_book["pluginsConfig"]["edit-link"]["label"] = dict_book["pluginsConfig"]["edit-link"].get("label", 'Edita esta página')

#             dict_book["pluginsConfig"]["githubcontributors"] = dict_book["pluginsConfig"].get("githubcontributors", {})
#             dict_book["pluginsConfig"]["githubcontributors"]["githubOwner"] = dict_book["pluginsConfig"]["githubcontributors"].get("githubOwner", "catedu")
#             dict_book["pluginsConfig"]["githubcontributors"]["githubRepository"] = dict_book["pluginsConfig"]["githubcontributors"].get("githubRepository", name)

#             with open("book.json", "w", encoding="utf-8") as file:
#                 json.dump(dict_book, file, ensure_ascii=False)
#             os.system('git add book.json')
#             os.system("git commit -m 'añado plugins de edit-link y githubcontributors'")
#             os.system('git push')
#             print('#############', name, '################')
#             repos.append(name)
#             time.sleep(50)
#         except:
#             print("Not a directory")
#     print(repos)



# update_plugins('/home/jesus/Documentos/exeLearning_toGitbook/books_pushed')