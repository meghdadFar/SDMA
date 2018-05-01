import math


def calculate_am(compounds, corpus_in_counts):
    pmis = {}
    npmis = {}
    for c in compounds:
        pmi, npmi = calculate_pmi(c, corpus_in_counts)
        pmis[c] = pmi
        npmis[c] = npmi
    return pmis, npmis


def calculate_pmi(compound, corpus_in_counts):
    pmi = 0
    npmi = 0
    if compound in corpus_in_counts.bigrams:
        m, h = compound.split(' ')
        p_of_c = corpus_in_counts.bigrams[compound] / float(corpus_in_counts.Nb)
        p_of_h = corpus_in_counts.unigrams[h]/float(corpus_in_counts.Nu)
        p_of_m = corpus_in_counts.unigrams[m] / float(corpus_in_counts.Nu)
        pmi = math.log(p_of_c/(p_of_h * p_of_m))
        npmi = pmi/float(-math.log(p_of_c))
    return pmi, npmi