from TokensCleaner import TokensCleaner

from TokensCleaner import TokensCleaner

import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

class BigramsExtractor(TokensCleaner):
    def __init__(self):
        super(BigramsExtractor, self).__init__()

    def get_bigrams(self, rawText, score_fn=BigramAssocMeasures.pmi, n=40):
    	clean_text = TokensCleaner.clean(self, rawText, cleaning_level=3)
        bigram_finder = BigramCollocationFinder.from_words(clean_text['3'])
        bigram_measures = BigramAssocMeasures()
        bigrams = bigram_finder.nbest(bigram_measures.pmi, n)
        # print bigrams
        return bigrams
