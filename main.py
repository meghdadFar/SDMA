from general import create_filter, ngrams, sort_by_value, print_tuples, write_tuples
from IO import reddy_ncs
import configparser
from sdma import create_alternative, calculate_sdma
from am import calculate_am
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
    logging.info("Reading unigrams")
    unigrams, N1, V1 = ngrams(config, filter, 1)
    logging.info("Reading bigrams")
    bigrams, N2, V2 = ngrams(config, filter, 2)
    corpus_in_counts = CorpusInCounts(unigrams, N1, V1, bigrams, N2, V2)
    logging.info("Calculating SDMAs")
    sdma_results = calculate_sdma(compound_to_alts, corpus_in_counts)
    pmi_results, npmi_results = calculate_am(compound_to_alts, corpus_in_counts)
    logging.info("Writing results to files")
    write_tuples(sort_by_value(sdma_results), '_sdma.csv')
    write_tuples(sort_by_value(pmi_results), '_pmi.csv')
    write_tuples(sort_by_value(npmi_results), '_npmi.csv')

    # print_tuples(sort_by_value(sdma_results))
    # print('------------------------------')
    # print_tuples(sort_by_value(pmi_results))
    # print('------------------------------')
    # print_tuples(sort_by_value(npmi_results))