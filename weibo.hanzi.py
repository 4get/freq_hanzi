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
	if re.match((ur"([\u4E00-\u9FA5])"), word):
		words[word] = words.get(word, 0) + 1

for word in easy_words_gen:
	if word in words:
		del words[word]

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)


print ("<table border=\"1\">")
print ("  <tr>")
print ("    <th>word</th>")
print ("    <th>Weibo</th>")
print ("    <th>eudic</th>")
print ("    <th>52words</th>")
print ("    <th>Pic.bing.cn</th>")
print ("  </tr>")

for word, frequency in top_words:
	word = word.encode(default_encoding)
	#print ("%s" % (word))
	print ("<tr>")
	print ("<font size=\"4\">")
	print ("<td>%s</td>" % (word))
	print ("<td><a href=\"http://s.weibo.com/weibo/%s&Refer=STopic_box\" target=\"_blank\">%s</a></td>" % (word, word))
	print ("<td><a href=\"http://cn.bing.com/images/search?q=%s&go=&qs=bs&form=QBIR\" target=\"_blank\">%s</a></td>" % (word, word))
	print ("</tr>")

print ("</table>")

