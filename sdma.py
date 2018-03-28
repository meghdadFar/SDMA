import logging
import logging_config
from gensim.models.keyedvectors import KeyedVectors
from substitute import Substitute
import math


def create_alternative(compounds, config):
    gensim_w2v_model = get_gensim_model(config)
    result = {}
    for cmpnd in compounds:
        modifier, head = cmpnd.split(' ')
        new_headed_list = rep_head(modifier, head, gensim_w2v_model, int(config['VECTOR_SPACE']['NUM_NEIGHBOUR']))
        new_modfiered_list = rep_modifier(modifier, head, gensim_w2v_model, int(config['VECTOR_SPACE']['NUM_NEIGHBOUR']))
        new_mod_headed_list = rep_head_modifier(modifier, head, gensim_w2v_model, int(config['VECTOR_SPACE']['NUM_NEIGHBOUR']))
        result[cmpnd] = Substitute(cmpnd, new_modfiered_list, new_headed_list, new_mod_headed_list)
    return result


def get_gensim_model(config):
    logging.info('Reading gensim model')
    gensim_w2v_model = KeyedVectors.load_word2vec_format(config['PATH']['GENSIM_WE_MODEL'], binary=False)
    return gensim_w2v_model


def rep_head(modifier, head, gensim_model, num_neighbours):
    head_neighbours = get_neighbours(gensim_model, head, num_neighbours)
    with_new_head = []
    for hn in head_neighbours:
        with_new_head.append(modifier + ' ' + hn)
    return with_new_head


def rep_modifier(modifier, head, gensim_model, num_neighbours):
    mod_neighbours = get_neighbours(gensim_model, modifier, num_neighbours)
    with_new_modifier = []
    for mod in mod_neighbours:
        with_new_modifier.append(mod + ' ' + head)
    return with_new_modifier


def rep_head_modifier(modifier, head, gensim_model, num_neighbours):
    head_neighbours = get_neighbours(gensim_model, head, num_neighbours)
    mod_neighbours = get_neighbours(gensim_model, modifier, num_neighbours)
    with_new_mod_head = []
    for mod in mod_neighbours:
        for hn in head_neighbours:
            with_new_mod_head.append(mod + ' ' + hn)
    return with_new_mod_head


def is_one_word(input_string):
    if len(input_string.split('-')) == 1:
        return True
    else:
        return False


def get_neighbours(gensim_model, word, num_neighbours):
    neighbours = gensim_model.most_similar(positive=word, topn=num_neighbours)
    neighbours = [tup[0] for tup in neighbours if is_one_word(tup[0])]
    return neighbours


def calculate_sdma(compound_to_substitute, corpus_in_counts):
    results = {}
    for k, v in compound_to_substitute.iteritems():
        results[k] = sdma_1(v, corpus_in_counts)
    return results


def sdma_1(substitute, corpus_in_counts):
    p = sigma([substitute.compound], corpus_in_counts, 1)/float(corpus_in_counts.N + corpus_in_counts.V)
    p_of_m = sigma(substitute.modifier_alts, corpus_in_counts, 1)/float(corpus_in_counts.N + corpus_in_counts.V)
    sdma = math.log(p/float(p_of_m))
    return sdma


def sigma(compounds, corpus_in_counts, smooth=False):
    sigma_frequency = 1  # To avoid division by zero upstream
    for c in compounds:
        if c in corpus_in_counts.bigrams:
            sigma_frequency += corpus_in_counts.bigrams[c]
            if smooth:
                sigma_frequency += smooth
    return sigma_frequency



