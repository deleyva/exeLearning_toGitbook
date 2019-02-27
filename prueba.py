import os
import re
import json
from itertools import islice

def update_plugins(path):
    """
    Actualiza los plugins que indiquemos,
    dentro de la función por ahora
    """
    dirs = os.scandir(path)
    remotes = []
    pattern = re.compile(r"(git@github\.com:catedu\/)(.*\.git|) \(fetch\)", re.DOTALL)
    for entry in islice(dirs, 2):
        try:
            os.chdir(entry.path)
            print(entry.path)
            remote = os.popen('git remote -v').read()
            remote_tupple = pattern.findall(remote)[0]
            name = remote_tupple[1][:-4]
            base = 'https://github.com/catedu/' + name + '/edit/master'
            print(name, base)
        except:
            print("XXXXXXXXXXXXXXXXXXXXX")

update_plugins('/home/jesus/Documentos/exeLearning_toGitbook/books_pushed')