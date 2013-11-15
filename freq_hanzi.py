#!/usr/bin/python
#coding=utf-8

import sys
import re
import os
from string import punctuation
from operator import itemgetter

default_encoding='utf-8'

N = 1000
words = {}

def cut_hanzi(sentence):
    if not ( type(sentence) is unicode):
        try:
            sentence = sentence.decode('utf-8')
        except:
            sentence = sentence.decode('gbk','ignore')
    re_han, re_skip = re.compile(ur"([\u4E00-\u9FA5])"), re.compile(ur"(\d+\.\d+|[a-zA-Z0-9]+)")
    blocks = re_han.split(sentence)
    for hanzi in blocks:
		yield hanzi 

with open(sys.argv[1]) as file: 
	text = file.read()
	words_gen = cut_hanzi(text)

with open("easy_words.txt") as file: 
	text = file.read()
	easy_words_gen = cut_hanzi(text)

for word in words_gen:
    words[word] = words.get(word, 0) + 1

for word in easy_words_gen:
	if word in words:
		del words[word]

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)

for word, frequency in top_words:
	print ("%d\t\t%s" % (frequency, word.encode(default_encoding)))

