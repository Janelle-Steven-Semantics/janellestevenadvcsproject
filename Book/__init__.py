#!/usr/bin/env python
from PyDictionary import PyDictionary
dictionary = PyDictionary()

# initialize word count system
searchlist = ['happy','sad','good','bad']


for listword in range(len(searchlist)):
    word = listword # the word we're looking for (including synonyms)
    wordcount = 0 # how many instances of the word
    wordlist = [] # what synonyms we found

# open up the book!
    sample = open("Loadbook.txt")

# walk through the book, line by line
    for line in sample:
    
    # is our search term in the line?
      if word in line:
            if word not in wordlist:
                wordlist.append(word)
            print(line)
            wordcount = wordcount + line.count(word)
        
    # are any synonyms in the line?
    for w in dictionary.synonym(word):
        if w in line:
            if w not in wordlist:
                wordlist.append(w)
            print(line)
            wordcount = wordcount + line.count(w)

# print out the results
    print("There are {} Occurrences like {} ({})").format(wordcount, word, wordlist)
