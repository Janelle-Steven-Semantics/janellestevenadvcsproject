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
import sys
import fileinput

f = open('output.html', 'r+')
sys.stdout = f

try:
    f2 = open('Loadbook.txt','a')

except:
    print('something went wrong ')
    sys.exit(0)

for token in f:
    if 'Dashwood' in token:
       token= token.replace('Dashwood', 'batman')
      # print("Alexa" + " " + line)
       f2.write(token)

terms = [
    'happy',
    'sad',
    'good',
    'bad',
    'death',
    'peace',
    'fear',
    'anxious',
    'anxious',
    'life',
    'gloomy',
    'dark',
    'light',
    'worried',
    'confident',
    'charming',
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
    'friendly',
    'generous'
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
    'dislike',
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
    'wonderful',
    'hope',
    'charming',
    'generous'
]
termspeaceful = [
    'peace',
    'calm',
    'easy']


termsaggressive = [
    'aggressive',
    'harm',
    'anger',
    'scold'
    'offense',
    'rude',

]
termshappy = [
    'happy',
    'good',
    'laugh',
    'joy',
    'friendly'
]

badprefixes= [
    'un', 'anti', 'in', 'dis'
]

omcount = 0
gocount = 0
bacount = 0
pecount = 0
agcount = 0
cacount = 0
hacount = 0
tokencount = 0;

def color_positive(f, token):
    f.write('<p style="color:#63EB19">%s</p>' % token)

def color_negative(f, token):
    f.write('<p style="color:#FF0000">%s</p>' % token)

def color_ominous(f, token):
    f.write('<p style="color:#E9EC1A">%s</p>' % token)


for token in tokens:
    ++tokencount
    for term in searchResults:
        if term.term in token and term.term in termsgood and not term.term.startswith(tuple(badprefixes)):
            term.increment()
            color_positive(f, token)
            ++gocount


        if term.term in token and term.term in termsbad:
            term.increment()
            color_negative(f, token)
            ++bacount


        if term.term in token and term.term in termsominous:
            term.increment()
            color_ominous(f, token)
            ++omcount

        if term.term in token and term.term in termspeaceful and not term.term.startswith(tuple(badprefixes)):
            term.increment()
            color_positive(f, token)
            ++pecount

        if term.term in token and term.term in termsaggressive:
            term.increment()
            color_negative(f, token)
            ++agcount

        if term.term in token and term.term in termshappy and not term.term.startswith(tuple(badprefixes)):
            term.increment()
            color_positive(f, token)
            ++hacount

    for synonym in term.synonyms:
        if synonym in token and synonym not in terms and term.term in termsgood and not term.term.startswith( tuple(badprefixes)):
            print("The tone of this sentence is also partly good.")
            term.increment(synonym)
            ++gocount

        if synonym in token and synonym not in terms and term.term in termsbad:
            print("The tone of this sentence is also partly bad.")
            term.increment(synonym)
            ++bacount

        if synonym in token and synonym not in terms and term.term in termsaggressive:
            print("The tone of this sentence is also partly aggressive.")
            term.increment(synonym)
            ++agcount

        if synonym in token and synonym not in terms and term.term in termsominous:
            print("The tone of this sentence is also partly ominous.")
            term.increment(synonym)
            ++omcount

        if synonym in token and synonym not in terms and term.term in termspeaceful and not term.term.startswith(tuple(badprefixes)):
            print("The tone of this sentence is also partly peaceful.")
            term.increment(synonym)
            ++pecount

        if synonym in token and synonym not in terms and term.term in termshappy and not term.term.startswith(tuple(badprefixes)):
            print("The tone of this sentence is also partly happy.")
            term.increment(synonym)
            ++hacount


tokecount = 0

tokencount= 0
for token in tokens[0:20]:
    if gocount > bacount:
        print("For the first third of the book, the tone is mostly good.")

for token in tokens[0:20]:
    tokencount
    if gocount > bacount:
        print("For the first third of the book, the tone is mostly good")
        if pecount > tokecount/10:
            print("For the first third of the book, the tone is also peaceful")
        if hacount > tokecount/10:
            print("and happy")

    else:
        print("For the first third of the book, the tone is mostly bad.")


#for token in tokens[tokens.size() / 3: tokens.size() * 2 / 3]:



#for token in tokens[tokens.size() * 2 / 3: tokens.size()]:
                #tone.count = term.count
                #print(tone.count)


for term in searchResults:
    print('There are {} occurrences of synonyms of {} (using {} as synonyms)'.format(term.count, term.term, term.synonyms))

f.close()
f2.close()
