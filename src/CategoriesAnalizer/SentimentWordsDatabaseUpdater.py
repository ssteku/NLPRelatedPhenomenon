from BTrees.OOBTree import OOBTree
import transaction
class SentimentWordsDatabaseUpdater(object):
    def __init__(self, database):
        self.database_root = database

    def updateWordsDatabase(self):
        self.database_root
        sentiment_words_db = self.__createSentimentWordsDatabase()
        if not self.database_root.has_key('articles_db'):
            raise Exception("No database for articles available")                  
        article_db = self.database_root['articles_db']
        print "Level1 : " + str(len(sentiment_words_db['levels']['1']['positive']))
        print "Level1 : " + str(len(sentiment_words_db['levels']['1']['negative']))
        print "Level2 : " + str(len(sentiment_words_db['levels']['2']['positive']))
        print "Level2 : " + str(len(sentiment_words_db['levels']['2']['negative']))

        print "Level3 : " + str(len(sentiment_words_db['levels']['3']['positive']))
        print "Level3 : " + str(len(sentiment_words_db['levels']['3']['negative']))
        print "Bigrams : " + str(len(sentiment_words_db['bigrams']['positive']))
        print "Bigrams : " + str(len(sentiment_words_db['bigrams']['negative']))
        self.__fillDatabaseWithNewWords(sentiment_words_db, article_db)
    

    def __createSentimentWordsDatabase(self):
        if not self.database_root.has_key('sentiment_words') :
            print "Creating new sentiment words database"
            self.database_root['sentiment_words'] = OOBTree()
            words_database = self.database_root['sentiment_words']
            words_database['bigrams'] = OOBTree()
            words_database['bigrams']['positive'] = []
            words_database['bigrams']['negative'] = []
            words_database['bigrams']['most_frequent'] = dict()
            words_database['bigrams']['most_frequent']['positive'] = []
            words_database['bigrams']['most_frequent']['negative'] = []

            words_database['levels'] = OOBTree()
            levels = words_database['levels']
            levels['1'] = OOBTree()
            levels['1']['positive'] = []
            levels['1']['negative'] = []
            levels['1']['most_frequent'] = dict()
            levels['1']['most_frequent']['positive'] = []
            levels['1']['most_frequent']['negative'] = []

            levels['2'] = OOBTree()
            levels['2']['positive'] = []
            levels['2']['negative'] = []
            levels['2']['most_frequent'] = dict()
            levels['2']['most_frequent']['positive'] = []
            levels['2']['most_frequent']['negative'] = []

            levels['3'] = OOBTree()
            levels['3']['positive'] = []
            levels['3']['negative'] = []
            levels['3']['most_frequent'] = dict()
            levels['3']['most_frequent']['positive'] = []
            levels['3']['most_frequent']['negative'] = []

        return self.database_root['sentiment_words']

    def __fillDatabaseWithNewWords(self, words_database, articles_db):        
        articles = self.__extractNewArticlesKeys(articles_db)
        print "Articles to be proceeded: " + str(len(articles))
        for key in articles:
            print "Updating article : " + key
            self.__extractBigramWords(articles_db[key], words_database['bigrams'])
            self.__extractLevelWords(articles_db[key], words_database['levels'], '1')
            self.__extractLevelWords(articles_db[key], words_database['levels'], '2')
            self.__extractLevelWords(articles_db[key], words_database['levels'], '3')
            articles_db[key].uploaded = True
        print transaction.commit()
    def __extractNewArticlesKeys(self, article_db):
        articles_with_sentiment = [] 
        for key in article_db.keys():
            if hasattr(article_db[key], 'sentiment'):
                articles_with_sentiment.append(key)
        print 'articles_with_sentiment len: ' + str(len(articles_with_sentiment))
        return [key for key in articles_with_sentiment if not hasattr(article_db[key], 'uploaded')]

    def __extractBigramWords(self, article, bigrams):
        bigrams[article.sentiment].extend(article.bigrams)
        bigrams._p_changed = True

    def __extractLevelWords(self, article, levels_db, level):
        article_levels = article.frequency_distribution_levels        
        levels_db[level][article.sentiment].extend(article_levels[level])
        levels_db[level]._p_changed = True
