#!/usr/bin/env python
from PyDictionary import PyDictionary
import re
dictionary = PyDictionary()

# initialize word count system
<<<<<<< HEAD
searchlist = ["good", "sweet"]
=======
searchlist = ['happy', 'sad', 'good', 'bad', 'death', 'peace', 'fear', 'anxious', 'life', 'gloomy']
>>>>>>> origin/master


for listword in range(len(searchlist)):
    word = searchlist[listword]  # the word we're looking for (including synonyms)
    wordcount = 0  # how many instances of the word
    wordlist = []  # what synonyms we found

# open up the book!
    sample = open("Loadbook.txt")
    linecount = 0
# walk through the book, line by line
    for line in sample:
        linecount = linecount + 1  #counts the line number
    # is our search term in the line?

        if word in line:
            if word not in wordlist:
                wordlist.append(word)
            print(line)
            wordcount = wordcount + line.count(word)
            print("Occurs on line " + str(linecount))
        for w in dictionary.synonym(word):
            if w in line:
                if w not in wordlist:
                    wordlist.append(w)
                    print(line)
                    wordcount = wordcount + line.count(w)
                    print("Occurs on line " + str(linecount))

        usablewordlist = [i for i in range(10)]
        for j in range(0,10,1):
          i = wordcount

        highesttone = max(usablewordlist)
        print(highesttone)

        if usablewordlist[2n-1] > usablewordlist[2n]:
            n = n + 1
            print("the tone for line " + str(linecount) + "is slightly good")


# print out the results
print("There are {} Occurrences like {} ({})".format(wordcount, word, wordlist))


