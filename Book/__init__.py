#!/usr/bin/env python
from PyDictionary import PyDictionary
dictionary = PyDictionary()

print(dictionary.get_synonym("happy"))
sample = open("Loadbook.txt")
for line in sample:
    # insert any "word" that you want to search for
    if dictionary.get_synonym("happy") in line:
        print(line)
        wordcount + 1
        print("There are " + wordcount + "Occurrences Like Happy")


        #What parameters determine tone?



    #check every 4 lines

        # count some indiscriminate synonyms OR Synonyms from book

        # do some math good - bad
            #if 0 bad = good
            # if bad > good tone = bad
                # if difference small or big


