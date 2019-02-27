import json
import os

with open("book.json") as file:
     dict_book = json.load(file)
     
plugins = ["edit-link", "githubcontributors"]
dict_book["plugins"].extend(plugins)

dict_book["pluginsConfig"] = dict_book.get("pluginsConfig", {})
dict_book["pluginsConfig"]["edit-link"] = dict_book["pluginsConfig"].get("edit-link", {})
dict_book["pluginsConfig"]["edit-link"]["base"] = dict_book["pluginsConfig"]["edit-link"].get("base", 'https://github.com/catedu/ensena-pensamiento-computacional-con-arduino/edit/master')
dict_book["pluginsConfig"]["edit-link"]["label"] = dict_book["pluginsConfig"]["edit-link"].get("label", 'Edita esta página')

dict_book["pluginsConfig"]["githubcontributors"] = dict_book["pluginsConfig"].get("githubcontributors", {})
dict_book["pluginsConfig"]["githubcontributors"]["githubOwner"] = dict_book["pluginsConfig"]["githubcontributors"].get("githubOwner", "catedu")
dict_book["pluginsConfig"]["githubcontributors"]["githubRepository"] = dict_book["pluginsConfig"]["githubcontributors"].get("githubRepository", "ensena-pensamiento-computacional-con-arduino")

with open("book.json", "w", encoding="utf-8") as file:
      json.dump(dict_book, file)
      
