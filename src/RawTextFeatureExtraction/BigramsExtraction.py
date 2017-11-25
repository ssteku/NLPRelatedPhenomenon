
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

from src.RawTextFeatureExtraction.TokensCleaner import TokensCleaner


class BigramsExtractor(TokensCleaner):
    def __init__(self, configuration_map):
        super(BigramsExtractor, self).__init__(configuration_map)

    # TODO configuration value
    def get_bigrams(self, rawText, score_fn=BigramAssocMeasures.pmi, n=40):
        # TODO configuration value
        clean_text = TokensCleaner.clean(self, rawText, cleaning_level=3)
        bigram_finder = BigramCollocationFinder.from_words(clean_text['3'])
        bigram_measures = BigramAssocMeasures()
        bigrams = bigram_finder.nbest(bigram_measures.pmi, n)
        return bigrams
