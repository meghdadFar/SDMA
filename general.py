from nltk import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def preprocess(s):
    tokenized = ' '.join(word_tokenize(s))
    tokenized = tokenized.lower()
    tokenized = tokenized.strip()
    return tokenized


def sentence_to_ngram(sentence, n):
    s = preprocess(sentence).split(' ')
    ngrams = [' '.join(s[i:i + n]) for i in xrange(len(s) - n + 1)]
    return ngrams


def sentencelist_to_ngram(sentence_list, n, ngram_filter_set=None):
    all_ngrams = {}
    for s in sentence_list:
        ngrams = sentence_to_ngram(s, n)
        for ng in ngrams:
            all_ngrams[ng] = all_ngrams.get(ng, 0) + 1
    N = sum(all_ngrams.values())
    V = len(all_ngrams)
    if ngram_filter_set:
        all_ngrams = filter_ngrams(all_ngrams, ngram_filter_set)
    return all_ngrams, N, V


def filter_ngrams(ngrams, filter_set):
    results = {}
    for ng in filter_set:
        if ng in ngrams:
            results[ng] = ngrams[ng]
    return results


def ngrams(config, ngram_filter):
    with open(config['PATH']['CORPUS'],) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    unigrams, _, _ = sentencelist_to_ngram(content, 1, ngram_filter)
    bigrams, N, V = sentencelist_to_ngram(content, 2, ngram_filter)
    return unigrams, bigrams, N, V


def extract_constituent(compounds):
    constituetns = []
    for c in compounds:
        constituetns.extend(c.split(' '))
    return constituetns


def extract_from_sub(sub):
    all = []
    all.append(sub.compound)
    all.extend(sub.modifier_alts)
    all.extend(sub.head_alts)
    all.extend(sub.combined_alts)
    all.extend(extract_constituent(all))
    return all


def create_filter(compound_to_alts):
    filter = set()
    for cmpnd, subs in compound_to_alts.iteritems():
        tmp = extract_from_sub(subs)
        for t in tmp:
            filter.add(t)
    return filter


def sort_by_value(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def print_tuples(list_of_tuple):
    for k in list_of_tuple:
        print k[0], '\t', k[1]