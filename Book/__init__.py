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
    'light',
    'worried',
    'confident',
    'cruel',
    'aggressive',
    'harm',
    'anger',
    'offense',
    'rude',
    'truth',
    'afraid',
    'regret',
    'scold',
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
    'afraid',
    'regret',
    ]

termsominous = [
    'death',
    'fear',
    'anxious',
    'gloomy',
    'dank',
    'worried',
    'cruel']
termsgood = [
    'happy',
    'good',
    'peace',
    'kind',
    'confident',
    'light',
    'wonderful'
]
termspeaceful = [
    'peace',
    'calm',
    'easy']
termscandid = [
    'offense',
    'rude',
    'truth',
]
termsaggressive = [
    'aggressive',
    'harm',
    'anger',
    'scold'
]
termshappy = [
    'happy',
    'good',
    'laugh',
    'joy',
]

omcount = 0
gocount = 0
bacount = 0
pecount = 0
agcount = 0
cacount = 0
hacount = 0

for token in tokens:
    for term in searchResults:
        if term.term in token and term.term in termsgood and term.term not in 'no':
            term.increment()
            ++gocount
            print(token)
            print("/////This tone is good!")

        if term.term in token and term.term in termsbad and term.term not in 'no':
            term.increment()
            ++bacount
            print(token)
            print("/////This tone is bad!")
        if term.term in token and term.term in termsominous and term.term not in 'no':
            term.increment()
            ++omcount
            print("/////This tone is ominous!")
        if term.term in token and term.term in termspeaceful and term.term not in 'no':
            term.increment()
            ++pecount
            print("/////This tone is peaceful!")
        if term.term in token and term.term in termsaggressive and term.term not in 'no':
            term.increment()
            ++agcount
            print("/////This tone is aggressive!")
        if term.term in token and term.term in termscandid and term.term not in 'no':
            term.increment()
            ++cacount
            print("/////This tone is candid!")
        if term.term in token and term.term in termshappy and term.term not in 'no':
            term.increment()
            ++hacount
            print("/////This tone is Happy!")


        for synonym in term.synonyms:
            if synonym in token and term.term in termsgood:
                term.increment(synonym)
                ++gocount
                print("/////This tone is good! :)")
            if synonym in token and term.term in termsbad:
                term.increment(synonym)
                ++bacount
                print("/////This tone is bad!")
            if synonym in token and term.term in termsominous:
                term.increment(synonym)
                ++omcount
                print("/////This tone is ominous! :)")
            if synonym in token and term.term in termspeaceful:
                term.increment(synonym)
                ++pecount
                print("/////This tone is peaceful!")
            if synonym in token and term.term in termscandid:
                term.increment(synonym)
                ++cacount
                print("/////This tone is candid! :)")
            if synonym in token and term.term in termshappy:
                term.increment(synonym)
                ++hacount
                print("/////This tone is Happy!")


tokencount= 0
for token in tokens[0:]:
    if gocount > bacount:
        print("For the first third of the book, the tone is mostly good.")
    else:
        print("For the first third of the book, the tone is mostly bad.")


#for token in tokens[tokens.size() / 3: tokens.size() * 2 / 3]:



#for token in tokens[tokens.size() * 2 / 3: tokens.size()]:
                #tone.count = term.count
                #print(tone.count)


for term in searchResults:
    print('There are {} occurrences of synonyms of {} (using {} as synonyms)'.format(term.count, term.term, term.synonyms))