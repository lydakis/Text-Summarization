# -*- coding: utf-8 -*-
from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.sentence import TokenizeSentence
from cltk.stop.greek.stops import STOPS_LIST
import math
import codecs

class Tokenizer(object):
    def __init__(self):
        corpus_importer = CorpusImporter('greek')
        corpus_importer.import_corpus('greek_models_cltk')
        self.tokenizer = TokenizeSentence('greek')

    def calc_word_freq(self, data):
        word_dict = {}
        freq_dict = {}
        words = data.split()
        total_word = 0
        for word in words:
            if word in STOPS_LIST:
                continue
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
            total_word += 1
        for key in word_dict.keys():
            freq_dict[key] = word_dict[key] / float(total_word)
        return freq_dict

    def tokenize_sentence(self, data):
        sentence_dict = {}
        sentences = self.tokenizer.tokenize_sentences(data)
        word_frequency = 0
        freq_dict = self.calc_word_freq(data)
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            for word in words:
                if word in STOPS_LIST:
                    continue
                word_frequency += freq_dict[word] if word in freq_dict else 0.00000000000000000001
            len_words = len(words)
            calc = word_frequency/len_words
            sentence_dict[sentence] = ((calc, len_words), i)
        return sentence_dict
