#!/usr/bin/env python
from PyDictionary import PyDictionary
dictionary = PyDictionary()

print(dictionary.get_synonym("happy"))
sample = open("Loadbook.txt")
for line in sample:

    # insert any "word" that you want to search for
    if dictionary.get_synonym("happy") in line:
        print(line)
        #happycount + 1     total number lines it occurs
        sline = line
        sum(sline.count(x) for x in (dictionary.get_synonym("happy")))
        print("There are " + wordcount + "Occurrences Like Happy")


     # insert any "word" that you want to search for
    if dictionary.get_synonym("sad") in line:
        print(line)
       # linenumber #how do we get the line number?
       # sadcount + 1  #this counts total,
        sline = line
        sum(sline.count(x) for x in (dictionary.get_synonym("sad")))  #  how do we count the number of occurences in line?
        print("There are " + wordcount + "sad")

                #What parameters determine tone?

    #check every 4 lines

        # count some indiscriminate synonyms OR Synonyms from book





        # do some math good - bad
            #if 0 bad = good
            # if bad > good tone = bad
                # if difference small or big


