#!/usr/bin/env python
from PyDictionary import PyDictionary
dictionary = PyDictionary()

# initialize word count system
searchlist = ['happy', 'sad', 'good', 'bad', 'peace', 'death', 'light', 'fear', 'humour', 'anxious', 'life', 'gloomy', 'respect']


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

        usablewordlist = [11]
        for j in range(len(usablewordlist)):
            usablewordlist.insert(usablewordlist, 1, wordcount)

        highesttone = max(usablewordlist)
        print(highesttone)

        n = 1
        #if usablewordlist[2n-1] > usablewordlist[2n]:
            #n = n + 1
        if usablewordlist[1] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "Happy")
        if usablewordlist[2] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "Sad")
        if usablewordlist[3] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "good")
        if usablewordlist[4] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "bad")
        if usablewordlist[5] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "peace")
        if usablewordlist[6] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "death")
        if usablewordlist[7] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "light")
        if usablewordlist[8] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "fear")
        if usablewordlist[9] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "humour")
        if usablewordlist[10] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "anxious")
        if usablewordlist[11] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "life")
        if usablewordlist[12] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "gloomy")
        if usablewordlist[13] = max(usablewordlist):
            print("the tone for line " + str(linecount) + "respect")





# print out the results
    print("There are {} Occurrences like {} ({})".format(wordcount, word, wordlist))


