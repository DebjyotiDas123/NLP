# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:55:12 2017

@author: Lenovo
"""
#import nltk.tag.stanford

from nltk.tag.stanford import StanfordNERTagger

# nltk.tag.stanford.StanfordNERTagger


#http://grepcode.com/snapshot/repo1.maven.org/maven2/edu.stanford.nlp/stanford-parser/3.3.1
demo = StanfordNERTagger('')
demo.tag(('Rami Eid is studying at Stony Brook University in NY'.split()))


from nltk.tag.stanford import StanfordPOSTagger


english_postagger = StanfordPOSTagger('D:\\SPJAIN\\NLP\\stanford-postagger-full-2017-06-09\\stanford-postagger-full-2017-06-09\\models\\english-bidirectional-distsim.tagger', 'D:\\SPJAIN\\NLP\\stanford-postagger-full-2017-06-09\\stanford-postagger-full-2017-06-09\\stanford-postagger.jar')
english_postagger.tag('this is stanford postagger in nltk for python users'.split())    

#Parser installation


#import nltk.tag.stanford
from nltk.parse.stanford import StanfordParser
from nltk import*

english_parser = StanfordParser('D:\\SPJAIN\\NLP\\stanford-parser-full-2017-06-09\\stanford-parser-full-2017-06-09\\stanford-parser.jar', 'D:\\SPJAIN\\NLP\\stanford-parser-full-2017-06-09\\stanford-parser-full-2017-06-09\\stanford-parser-3.8.0-models.jar')
sentences = english_parser.raw_parse_sents(('this is the english parser test', 'the parser is from stanford parser'))

for myListiterator in sentences:
    for t in myListiterator:
        print(t)
        
english_parser = StanfordParser('D:\\SPJAIN\\NLP\\stanford-parser-full-2017-06-09\\stanford-parser-full-2017-06-09\\stanford-parser.jar', 'D:\\SPJAIN\\NLP\\stanford-parser-full-2017-06-09\\stanford-parser-full-2017-06-09\\stanford-parser-3.8.0-models.jar')
sentences = english_parser.raw_parse_sents(('I am Debjyoti Das and I am studying in SpJAIN', 'the parser is from stanford parser'))

for myListiterator in sentences:
    for t in myListiterator:
        print(t)
        
        
        

#import nltk.tag.stanford
from nltk.tag.stanford import StanfordNERTagger
#==============================================================================
# nltk.tag.stanford.StanfordNERTagger
#==============================================================================
#This is just for a string
demo = StanfordNERTagger('D:/SP_JAIN/16-NLP/class_assignment/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz', 'D:/SP_JAIN/16-NLP/class_assignment/stanford-ner-2015-12-09/stanford-ner.jar')
demo.tag(('Rami Eid is studying at Stony Brook University in NY'.split()))

###########################D:\SPJAIN\NLP\stanford-ner-2017-06-09\stanford-ner-2017-06-09\classifiers\english.all.3class.distsim.crf.ser
#This is just for a string
demo = StanfordNERTagger('D:\\SPJAIN\\NLP\\stanford-ner-2017-06-09\\stanford-ner-2017-06-09\\classifiers\\english.all.3class.distsim.crf.ser\\english.all.3class.distsim.crf.ser', 'D:\\SPJAIN\\NLP\\stanford-ner-2017-06-09\\stanford-ner-2017-06-09\\stanford-ner.jar')
demo.tag(('Rami Eid is studying at Stony Brook University in NY'.split()))


f= open('D:\\SPJAIN\\NLP\\cnv_spjain_cleaned.txt')
print(f)

len(f)


from nltk.tag.stanford import StanfordPOSTagger
rwf= f.read()
f_splitlines = rwf.splitlines()
english_postagger = StanfordPOSTagger('D:\\SPJAIN\\NLP\\stanford-postagger-full-2017-06-09\\stanford-postagger-full-2017-06-09\\models\\english-bidirectional-distsim.tagger', 'D:\\SPJAIN\\NLP\\stanford-postagger-full-2017-06-09\\stanford-postagger-full-2017-06-09\\stanford-postagger.jar')
english_postagger.tag(f_splitlines)   


for a in f_splitlines:
    b= english_postagger.tag(f_splitlines)
    print(b)
