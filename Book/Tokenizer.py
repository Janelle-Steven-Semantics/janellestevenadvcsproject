import nltk
from book.ntlk import *
nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
sample=open("Loadbook.txt").read()
tokens=sent_tokenize(sample)
tokens=tokens[1:5]
sample.concordance("Dashwood")
