# -*- coding: utf-8 -*-
import sys
from model import Model
from tokenizer import Tokenizer
from summarizer import Summarizer
import codecs

file_name = sys.argv[1]
with codecs.open(file_name, encoding='utf-8') as f:
    text = f.read().split('\n')
    text = ' '.join(text)
    tokenizer = Tokenizer()
    model = Model()
    data = tokenizer.tokenize_sentence(text)
    clusters = model.fit(data)
    summarizer = Summarizer(clusters)
    print(summarizer.generate())
