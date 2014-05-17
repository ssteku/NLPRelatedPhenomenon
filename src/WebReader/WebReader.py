from RawTextFeatureExtraction.MostFrequentWordsExtractor import MostFrequentWordsExtractor
from ExtractorFacade import ExtractorFacade
from RawTextFeatureExtraction.BigramsExtraction import BigramsExtractor
from storage.ArticlePersistence import ArticlePersistence

import transaction
from RawTextFeatureExtraction.FeatureExtractor import FeatureExtractor
from BTrees.OOBTree import OOBTree
current_version = 1
import langid
class WebReader(object):
    def __init__(self, database, configuration_map):
        self.database = database
        self.__configuration_map = configuration_map
    def extract_all_articles(self, url):

        article_db = self.database
        freq = MostFrequentWordsExtractor(configuration_map)
        bigrams_extractor = BigramsExtractor()
        extractor = ExtractorFacade(url)
        articles = extractor.get_article_list()
        # self.__print_article_list(articles)
        for article in articles:
            self.__parse_article(article)
            if self.__article_in_english(article):
                self.__extract_article(article, article_db, freq, bigrams_extractor)
            else:
                print "----------> Article: " + article.title + " is not in english <------------"

    # def extract_features_for_all_articles(self, url, feature_database):
    #     extractor = FeatureExtractor(feature_database)
    #     extractor_facase = ExtractorFacade(url)
    #     articles = extractor_facase.get_article_list()

    #     for article in articles:
    #         self.__parse_article(article)
    #         extractor.get_most_frequent_words_features(article)

    def __article_in_english(self, article):
        result = langid.classify(article.text)
        minimum_probability = self.__configuration_map['language_match_minimum_probability']
        return result[0] == 'en' and result[1] > minimum_probability

    def __print_article_list(self, article_list):
        print "--------------Parsing articles---------------"
        for article in article_list:
            print article.title
        print "---------------------------------------------"

    def __extract_article(self, article, article_db, freq, bigrams_extractor):
        if self.__should_be_stored(article, article_db):
            print "Processing article: " + article.title

            number_of_words_from_article = self.__configuration_map['number_of_words_extracted_from_article']
            freq_words_levels = freq.get_most_frequent(article.text, number = number_of_words_from_article)
            bigrams = bigrams_extractor.get_bigrams(article.text)

            article_record = self.__create_article_record(freq_words_levels, bigrams, article)
            article_db[article.title] = article_record

            transaction.commit()
        else:
            print "Article : " + article.title + " is already in DB or is too short : "
            print str(len(article.text))



    def __should_be_stored(self, article, article_db):
        article_minimum_words_number = self.__configuration_map['article_minimum_words_number']
        return len(article.text) > article_minimum_words_number and not article_db.has_key(article.title)

    def __parse_article(self, article):
        try:
            article.download()
            article.parse()
            article.nlp()
        except Exception:
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