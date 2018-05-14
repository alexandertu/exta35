#!/usr/bin/env python3
import re
import requests
import json
import base64

import csv
import urllib.request

from joblib import Parallel, delayed
import multiprocessing

#https://audio00.forvo.com/audios/mp3/p/f/
# this function return a json, the url prefix is *https://forvo.com/mp3/*
def get_english_pronunciation(word):
	webPageUrl = "https://forvo.com/word/%s/#zh" % word
	webPageText = requests.get(webPageUrl).text
	englishPageTextList = re.findall("<em id=\"zh.*?</article>", webPageText, re.DOTALL)
	if len(englishPageTextList) == 0:
		return '{"status":"error"}'
	englishPageText = englishPageTextList[0]
	pronunciations = re.findall("Play\(\d+,'(.*?)'", englishPageText)
	for l in range(len(pronunciations)):
		pronunciations[l] = base64.b64decode(pronunciations[l]).decode()
	return pronunciations

# return list of words
def get_words(filename):
	out = []
	with open(filename) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			out.append(row)
	return out

def download_and_save(word, url):
	urllib.request.urlretrieve(url, "audio/" + word + ".mp3")	

def a(word):
	save = word['english']
	save = re.sub("[^a-zA-Z]","", save)
	save = save + "_" + word['character']

	print("Downloading " + save)

	download_and_save(save, "https://forvo.com/mp3/" + get_english_pronunciation(word['character'])[min(0, max(0, -1 + len(word['character'])))])

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(a)(i) for i in get_words('decks.csv'))
