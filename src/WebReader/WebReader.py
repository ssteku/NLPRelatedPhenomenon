from RawTextFeatureExtraction.MostFrequentWordsExtractor import MostFrequentWordsExtractor
from ExtractorFacade import ExtractorFacade
from RawTextFeatureExtraction.BigramsExtraction import BigramsExtractor
from storage.ArticlePersistence import ArticlePersistence

import transaction

from BTrees.OOBTree import OOBTree
current_version = 1
class WebReader(object):   
    def __init__(self, database):
        self.database = database

    def extractAllArticles(self, url):
        database_root = self.database.dbroot
        freq = MostFrequentWordsExtractor()
        bigrams_extractor = BigramsExtractor()
        extractor = ExtractorFacade(url)
        articles = extractor.getArticleList()
        if not database_root.has_key('articles_db'):
            database_root['articles_db'] = OOBTree()                
        article_db = database_root['articles_db']
        for article in articles:
            try:
                article.download()
                article.parse()
            except IOError:
                print "File parsing failed"
            

            if len(article.text) > 200 and not article_db.has_key(article.title):
                print "Processing article: " + article.title
                article.nlp()
                freq_words_levels = freq.getMostFrequent(article.text, number = 40)
                bigrams = bigrams_extractor.get_bigrams(article.text)
 
                article_record = ArticlePersistence()
                article_record.frequency_distribution_levels = freq_words_levels
                article_record.bigrams = bigrams
                article_record.benchmark_authors = article.authors
                article_record.benchmark_summary = article.summary
                article_record.benchmark_keywords = article.keywords
                article_record.current_version = current_version
                article_db[article.title] = article_record
                   
                transaction.commit()
            else:
                print "Article : " + article.title + " is already in DB or is too short : "  + str(len(article.text))

            

