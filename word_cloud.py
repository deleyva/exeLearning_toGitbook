from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
from gensim.models import TfidfModel, LsiModel
from gensim.models.ldamodel import LdaModel
from gensim import corpora
from gensim import matutils
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import defaultdict
import pyLDAvis.gensim as gensimvis
import pyLDAvis
import pandas as pd
import numpy as np
import lda
import os
from IPython.utils.signatures import signature

mds = []
STOPWORDS = set(stopwords.words('spanish'))

exlude = ['node_modules', '_book']
def number_of_chapters(folder):
	for root, dirs, files in os.walk(folder, topdown=True):
		dirs[:] = [d for d in dirs if d not in exlude]
		for file in files:
			if file.endswith('.md'):
				data = {}
				data['slug'] = os.path.join(root, file)
				with open(data['slug'], 'r') as infile:
					data['content'] = infile.read()
				mds.append(data)

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

number_of_chapters(str(os.getcwd() + '/books_pushed'))

texts = [tokenize(mds[i]['content']) for i in range(len(mds))]

print(len(texts))

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 10] for text in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

speeches_topics = LdaModel(corpus=corpus,
                           id2word=dictionary,
                           num_topics=20,
                           passes=10)

for i, topic in enumerate(speeches_topics.print_topics(10)):
    print('{} --- {}'.format(i, topic))

vis_data = gensimvis.prepare(speeches_topics, corpus, dictionary)
pyLDAvis.show(vis_data)