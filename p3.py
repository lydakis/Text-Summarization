# -*- coding: utf-8 -*-
import sys
from model import Model
from tokenizer import Tokenizer
from summarizer import Summarizer
import codecs

#Opening file to read
file_name = sys.argv[1]
#File Name: greekpdf-2.txt
with codecs.open(file_name, encoding='utf-8') as f:
	text = f.read().split('\n')

chapter_dictionary = dict()
for i in range(len(text)):
	if(text[i].isdigit()):
		chapter_dictionary[text[i]] = text[i+1]
		for j in range(i+2,len(text)):
			if not (text[i].isdigit()):
				chapter_dictionary[text[i]].append(text[j])

tokenizer = Tokenizer()
model = Model()

file_output =  open("a.txt","w")

for k, v in chapter_dictionary.items():
	v = ''.join(v)
	data = tokenizer.tokenize_sentence(v)
	clusters = model.fit(data)
	summarizer = Summarizer(clusters)
	file_output.write(summarizer.generate()+"\n")
