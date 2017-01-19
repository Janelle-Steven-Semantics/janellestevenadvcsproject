#!/usr/bin/env python

sample = open("Loadbook.txt")
for line in sample:
    # insert any "word" that you want to search for
    if "great" in line:
        print(line)
