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
thesaurus = PyDictionary()

terms = ['happy', 'sad', 'strange']
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
