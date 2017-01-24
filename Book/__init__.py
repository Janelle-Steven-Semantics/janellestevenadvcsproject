#!/usr/bin/env python
from PyDictionary import PyDictionary
dictionary = PyDictionary()

print(dictionary.get_synonym("happy"))
sample = open("Loadbook.txt")
for line in sample:
    # insert any "word" that you want to search for
    if dictionary.get_synonym("happy") in line:
        print(line)
        i + 1
        print(i)



