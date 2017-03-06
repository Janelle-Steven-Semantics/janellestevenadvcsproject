from PyDictionary import PyDictionary
thesaurus = PyDictionary()

class Synonym_extension(object):

    term = ''
    synonyms = []
    count = 0

    def __init__(self, term):
        self.term = term;
        self.synonyms = dict((elt, 0) for elt in thesaurus.synonym(term))
        self.count = 0

    def increment(self, word = None):
        if word in self.synonyms:
            self.synonyms[word] += 1
        self.count += 1