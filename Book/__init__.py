#!/usr/bin/env python
#IMPORTANT IMPORTS. You might need to download packages in NLTK
from Synonym_extension import Synonym_extension
from PyDictionary import PyDictionary
import nltk
from PyDictionary import PyDictionary
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
    'gloomy',
    'dark',
    'light'
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
tone = 0
termsbad = [
    'sad',
    'bad',
    'death',
    'fear',
    'anxious',
    'gloomy',
    'dark',]
termsgood = [
    'happy',
    'good',
    'peace',
    'kind']
for token in tokens:
    for term in searchResults:
        if term.term in token and term.term in termsgood:
            term.increment()
            print(token + "/////This tone is good! :)")
        if term.term in token and term.term in termsbad:
            term.increment()
            print(token + "/////This tone is bad! :(")



        for synonym in term.synonyms:
            if synonym in token and term.term in termsgood:
                term.increment(synonym)
                print(token+ "/////This tone is good! :)")
            if synonym in token and term.term in termsbad:
                term.increment(synonym)
                print(token + "/////This tone is bad!")
                #tone.count = term.count
                #print(tone.count)

for term in searchResults:
    print('There are {} occurrences of synonyms of {} (using {} as synonyms)'.format(term.count, term.term, term.synonyms))

