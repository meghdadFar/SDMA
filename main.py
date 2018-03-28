from general import create_filter, ngrams, sort_by_value, print_tuples
from IO import reddy_ncs
import configparser
from sdma import create_alternative, calculate_sdma
from CorpusInCounts import CorpusInCounts
import logging
import sys
import logging_config


if __name__ == '__main__':

    logging.info("Reading configuration from " + sys.argv[1])
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    logging.info("Reading compounds")
    ncs, _ = reddy_ncs(config['PATH']['COMPOUNDS'])
    logging.info("Creating alternatives")
    compound_to_alts = create_alternative(ncs, config)
    logging.info("Creating filter")
    filter = create_filter(compound_to_alts)
    logging.info("Reading corpus and ngrams")
    unigrams, bigrams, N, V = ngrams(config, filter)
    logging.info("N, V = " + str(N) + ' ' + str(V))
    corpus_in_counts = CorpusInCounts(N, V, unigrams, bigrams)
    logging.info("Calculating SDMAs")
    results = calculate_sdma(compound_to_alts, corpus_in_counts)
    sorted_results = sort_by_value(results)
    print_tuples(sorted_results)

