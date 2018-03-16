git_ignore_text = 'venv/\nnode_modules'
book_json_text= ('''{ "plugins": ["youtube", "accordion", "image-captions"], '''
                '''"pluginsConfig": { "image-captions": { "caption": "Imagen - _CAPTION_" } } }''')


def number_of_chapters(folder):
    num = 0
    for root, dirs, files in folder:
        for file in files:
            if file.endswith('.elp'):
                num_capitulos = num_capitulos + 1
    return num

def start_book():
    path = str(os.getcwd()) + '/libros/' + course_title

	os.mkdir(path)
	os.chdir(path)
    os.system('gitbook init')
	with open('book.json', 'a') as book_json:
		book_json.write(book_json_text)
	
    with open('.gitignore', 'a')
		fh_gitigonre.write(git_ignore_text)

		fh_json.close()
		fh_gitigonre.close()