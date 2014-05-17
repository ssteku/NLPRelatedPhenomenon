import nltk
from nltk import FreqDist

from TokensCleaner import TokensCleaner


class MostFrequentWordsExtractor(TokensCleaner):
    def __init__(self, configuration_map):
        super(MostFrequentWordsExtractor, self).__init__(configuration_map)

    def get_most_frequent(self, rawText, number = None, cleaning_level = 3):
        cleaned_tokens_levels = TokensCleaner.clean(self, rawText, cleaning_level)
        freq_distributions_levels = dict()
        for level, cleand_tokens in cleaned_tokens_levels.items():
            all_words = FreqDist(cleand_tokens)
            if number == None:
                freq_distributions_levels[level] = all_words.items()
            else:
                freq_distributions_levels[level] = all_words.items()[:number]
        return freq_distributions_levels


