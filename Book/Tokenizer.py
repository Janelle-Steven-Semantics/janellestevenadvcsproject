import nltk
nltk.download()
from nltk.tokenize import word_tokenize
sample=open("Loadbook.txt")
print(word_tokenize(sample))
