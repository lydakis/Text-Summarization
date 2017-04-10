# -*- coding: utf-8 -*-
import codecs
import re
import sys
from model import Model
from tokenizer import Tokenizer
from summarizer import Summarizer

# ΒΙΒΛΙΟΓΡΑΦΙΚΕΣ ΑΝΑΦΟΡΕΣ BIBLIOGRAPHICAL REFERENCES
# Βιβλιογραφικές Αναφορές Bibliographical references
# Πίνακας περιεχομένων Table of Contents
# Περιεχόμενα Contents
# ΠΕΡΙΕΧΟΜΕΝΑ CONTENTS
# Κατάλογος Σχημάτων List Of Figures
# ΚΑΤΑΛΟΓΟΣ ΤΩΝ ΕΙΚΟΝΩΝ LIST OF FIGURES

#Opening file to read
file_name = sys.argv[1]
#File Name: greekpdf-2.txt
with codecs.open(file_name, encoding='utf-8') as f:
    text = f.read().split('\n')

#Reading Table of Contents

#Start Reading from var table_content
table_content = [u"Βιβλιογραφικές Αναφορές", u"Βιβλιογραφία", u"ΒΙΒΛΙΟΓΡΑΦΙΚΕΣ ΑΝΑΦΟΡΕΣ", u"Κατάλογος Σχημάτων", u"ΚΑΤΑΛΟΓΟΣ ΤΩΝ ΕΙΚΟΝΩΝ"]

#Stop reading when var is bibliography
bibliography = [u"Βιβλιογραφικές Αναφορές", u"Βιβλιογραφία", u"ΒΙΒΛΙΟΓΡΑΦΙΚΕΣ ΑΝΑΦΟΡΕΣ"]

#Clean Corpus
i = 0
while(i<len(text)):
    if(text[i] == u''):
        text.remove(u'')
    elif(text[i].isdigit()):
        text.remove(text[i])
    else:
        i = i+1

#Counting for headers and footers and removing them
sen_count = {}
for i in range(len(text)):
    if(text[i] not in sen_count):
        sen_count[text[i]] = 1
    else:
        sen_count[text[i]] += 1
a = [key for key,val in sen_count.items() if val == max(sen_count.values())]
header = a[0]
footer = a[1]

i = 0
while(i<len(text)):
    if(text[i] == header):
        text.remove(header)
    elif(text[i] == footer):
        text.remove(footer)
    else:
        i = i+1

count = 0
toc = []
chapter = {}
subtext = {}
for i in range(len(text)):
    if(text[i] == u"ΠΕΡΙΕΧΟΜΕΝΑ" or text[i] == u"Πίνακας περιεχομένων"):
        j = i+1
        while(not re.search(u'ΒΙΒΛΙΟΓΡΑΦΙΚΕΣ ΑΝΑΦΟΡΕΣ',text[j])):
            toc.append(text[j].split('..',1))
            j = j+1
        curr = j+1

for i in range(len(toc)):
    toc[i] = toc[i][0].strip()
# print(toc[3])
# print(text[255])

#Converting text to key value pair
#Dictionary name: module
module = dict()
curr_key = ''
while(curr < len(text)):
    if(text[curr] in toc):
        curr_key = text[curr]
        if(text[curr] not in module):
            module[text[curr]] = []
        curr += 1
    if(text[curr] in bibliography):
        break
    if curr_key != '':
        module[curr_key].append(text[curr])

    curr += 1

tokenizer = Tokenizer()
model = Model()

# data = tokenizer.tokenize_sentence(corpus)
# clusters = model.fit(data)
# summarizer = Summarizer(clusters)
# import pdb; pdb.set_trace()
# print(summarizer.generate())
for k, v in module.items():
    v = ' '.join(v)
    data = tokenizer.tokenize_sentence(v)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(k)
    clusters = model.fit(data)
    summarizer = Summarizer(clusters)
    print('***************************************')
    print(summarizer.generate())


    # print(k)
    # if(re.match(ur'ΚΕΦΑΛΑΙΟ [1-9]ο :',text[i])):
    #   if(text[i] not in chapter):
    #       chapter[text[i]] = 1
    #   else:
    #       j = i+1
    #       para = ""
    #       while not(re.match(ur'ΚΕΦΑΛΑΙΟ [1-9]ο :',text[j])):
    #           if(text[j] == u"Βιβλιογραφικές Αναφορές" or text[j] == u"Βιβλιογραφία" or text[j] == u"ΒΙΒΛΙΟΓΡΑΦΙΚΕΣ ΑΝΑΦΟΡΕΣ"):
    #               break
    #           para += text[j]
    #           j = j+1
    #       subtext[text[i]] = para
