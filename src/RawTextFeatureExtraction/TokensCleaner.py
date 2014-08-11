import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from RelatedWordsCleaner import RelatedWordsCleaner
from AdjectivesCleaner import AdjectivesCleaner
import string
import itertools
from nltk.corpus import wordnet_ic
from sets import Set

class TokensCleaner(object):
    def __init__(self, configuration_map):
        self.__configuration_map = configuration_map

    def clean(self, rawText, cleaning_level):
        cleaned_tokens_levels = dict()
        tokens = nltk.word_tokenize(rawText)
        if cleaning_level >= 1:
            tokens = self.__normalize(tokens)
            tokens = self.__clean_stop_words(tokens)
            tokens = self.__clean_punctuation(tokens)
            tokens = self.__clean_shortWords(tokens)
            cleaned_tokens_levels['1'] = tokens
        if cleaning_level >= 2:
            tokens = self.__clean_related(tokens)
            cleaned_tokens_levels['2'] = tokens
        if cleaning_level >= 3:
            tokens = self.__clean_adjectives(tokens)
            cleaned_tokens_levels['3'] = tokens
        return cleaned_tokens_levels

    def __normalize(self, tokens):
        print "Normalizing"
        wnl = nltk.WordNetLemmatizer()
        return [wnl.lemmatize(t.lower()) for t in tokens]


    def __clean_stop_words(self, tokens):
        print "Cleaning stopwords"
        print "Before: ", str(len(tokens))
        cleaned_tokens = []
        for word in tokens:
            if not word in stopwords.words("english"):
                cleaned_tokens.append(word)
        print "After: ", str(len(cleaned_tokens))
        return cleaned_tokens

    def __clean_punctuation(self, tokens):
        print "Cleaning punctuation"
        print "Before: ", str(len(tokens))
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        cleaned_tokens = []
        for token in tokens:
               new_token = regex.sub(u'', token)
               if not new_token == u'':
                   cleaned_tokens.append(new_token)
        print "After: ", str(len(cleaned_tokens))
        return cleaned_tokens
    def __clean_shortWords(self, tokens):
        print "Cleaning short words"
        print "Before: ", str(len(tokens))
        cleaned_tokens = []
        for token in tokens:
               if len(token) > 2:
                   cleaned_tokens.append(token)
        print "After: ", str(len(cleaned_tokens))
        return cleaned_tokens

    def __clean_related(self, tokens):
        print "Cleaning related words"
        print "Before: ", str(len(tokens))

        print "Tokens set len: ", str(len(Set(tokens)))

        cleaner = RelatedWordsCleaner(self.__configuration_map)
        cleaned_tokens = cleaner.get_cleaned_tokens(tokens)

        print "After: ", str(len(cleaned_tokens))
        print "After Tokens set len: ", str(len(Set(cleaned_tokens)))
        return cleaned_tokens

    def __clean_adjectives(self, tokens):
        print "Cleaning adjectives words"
        print "Tokens set len: ", str(len(Set(tokens)))

        cleaner = AdjectivesCleaner()
        cleaned_tokens = cleaner.clean_adjectives(tokens)

        print "After: ", str(len(cleaned_tokens))
        print "After Tokens set len: ", str(len(Set(cleaned_tokens)))
        return cleaned_tokens




