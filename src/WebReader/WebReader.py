from RawTextFeatureExtraction.MostFrequentWordsExtractor import MostFrequentWordsExtractor
from ExtractorFacade import ExtractorFacade
from RawTextFeatureExtraction.BigramsExtraction import BigramsExtractor
from storage.ArticlePersistence import ArticlePersistence

import transaction
from RawTextFeatureExtraction.FeatureExtractor import FeatureExtractor
from BTrees.OOBTree import OOBTree
current_version = 1
class WebReader(object):
    def __init__(self, database):
        self.database = database

    def extract_all_articles(self, url):

        article_db = self.database
        freq = MostFrequentWordsExtractor()
        bigrams_extractor = BigramsExtractor()
        extractor = ExtractorFacade(url)
        articles = extractor.get_article_list()
        for article in articles:
            self.__parse_article(article)
            self.__extract_article(article, article_db, freq, bigrams_extractor)

    def extract_features_for_all_articles(self, url, feature_database):
        extractor = FeatureExtractor(feature_database)
        extractor_facase = ExtractorFacade(url)
        articles = extractor_facase.get_article_list()
        for article in articles:
            self.__parse_article(article)
            extractor.get_most_frequent_words_features(article)

    def __extract_article(self, article, article_db, freq, bigrams_extractor):
        if self.__should_be_stored(article, article_db):
            print "Processing article: " + article.title

            freq_words_levels = freq.get_most_frequent(article.text, number = 40)
            bigrams = bigrams_extractor.get_bigrams(article.text)

            article_record = self.__create_article_record(freq_words_levels, bigrams, article)
            article_db[article.title] = article_record

            transaction.commit()
        else:
            print "Article : " + article.title + " is already in DB or is too short : "
            print str(len(article.text))



    def __should_be_stored(self, article, article_db):
        return len(article.text) > 200 and not article_db.has_key(article.title)

    def __parse_article(self, article):
        try:
            article.download()
            article.parse()
            article.nlp()
        except IOError:
            print "File parsing failed"

    def __create_article_record(self, freq_words_levels, bigrams, article):
        article_record = ArticlePersistence()
        article_record.frequency_distribution_levels = freq_words_levels
        article_record.bigrams = bigrams
        article_record.benchmark_authors = article.authors
        article_record.benchmark_summary = article.summary
        article_record.benchmark_keywords = article.keywords
        article_record.current_version = current_version
        return article_record