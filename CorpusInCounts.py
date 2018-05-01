class CorpusInCounts(object):
    def __init__(self, unigrams, Nu, Vu, bigrams, Nb, Vb):
        self.Nu = Nu
        self.Vu = Vu
        self.Nb = Nb
        self.Vb = Vb
        self.bigrams = bigrams
        self.unigrams = unigrams
