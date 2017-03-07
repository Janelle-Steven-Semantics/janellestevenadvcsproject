#!/usr/bin/env python
#IMPORTANT IMPORTS. You might need to download packages in NLTK
from Synonym_extension import Synonym_extension
from PyDictionary import PyDictionary
import nltk
from PyDictionary import PyDictionary
nltk.download()
from nltk.tokenize import sent_tokenize
from nltk.book import*
from nltk.corpus import*
from Synonym_extension import Synonym_extension
from PyDictionary import PyDictionary
thesaurus = PyDictionary()

terms = [
    'happy',
    'sad',
    'good',
    'bad',
    'death',
    'peace',
    'fear',
    'anxious',
    'life',
    'gloomy'
]
searchResults = []
for term in terms:
    searchResults.append(Synonym_extension(term))

#Hey Steven, this is a way to get the Project Gutenberg books
book = 'austen-sense.txt'
book = nltk.corpus.gutenberg.raw(book)
tokens = nltk.sent_tokenize(book)

#told you the tokenizer would come in handy
#searches the broken down sentences
#prints in order--we definitely need the line numbers printed

for token in tokens:
    for term in searchResults:
        if term.term in token:
            term.increment()
            print(token)
        for synonym in term.synonyms:
            if synonym in token:
                term.increment(synonym)
                print(token)

for term in searchResults:
 print('There are {} occurrences of synonyms of {} (using {} as synonyms)'.format(term.count, term.term, term.synonyms))
book = open('loadbook.txt')
for line in book:
    for term in searchResults:
        if term.term in line:
            term.increment()

        for synonym in term.synonyms:
            if synonym in line:
                term.increment(synonym)

for term in searchResults:
    print('There are {} occurrences of synonyms of {} (using {} as synonyms)'.format(term.count, term.term, term.synonyms))





usablewordlist = [searchlist]
for j in range(len(usablewordlist)):
    usablewordlist.insert(j, wordcount)

highesttone = max(usablewordlist)
print(highesttone)
#n = 0
#for n in range(len(usablewordlist)):
    #n = n + 1
    #if usablewordlist[2n-1] > usablewordlist[2n]:
        #print("the tone for line " + str(linecount) + " sorta good")
if usablewordlist[1] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " Happy")
if usablewordlist[2] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " Sad")
if usablewordlist[3] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " good")
if usablewordlist[4] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " bad")
if usablewordlist[5] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " peace")
if usablewordlist[6] == max(usablewordlist):
    if usablewordlist[3] != 0:
        print("the tone for line " + str(linecount) + " humorous")
    else:
        print("the tone for line " + str(linecount) + " death")
if usablewordlist[7] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " light")
if usablewordlist[8] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " fear")
if usablewordlist[9] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " humour")
if usablewordlist[10] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " anxious")
if usablewordlist[11] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " life")
if usablewordlist[12] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " gloomy")
if usablewordlist[13] == max(usablewordlist):
    print("the tone for line " + str(linecount) + " respect")

