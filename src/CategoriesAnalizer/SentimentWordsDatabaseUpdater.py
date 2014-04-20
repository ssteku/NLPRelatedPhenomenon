from BTrees.OOBTree import OOBTree
import transaction
class SentimentWordsDatabaseUpdater(object):
    def __init__(self, database, database_structure):
        self.database_root = database
        self.database_structure = database_structure

    def update_words_database(self, feature='sentiment', values=['negative', 'positive']):
        sentiment_words_db = self.__create_sentiment_words_database(feature, values)
        article_db = self.__get_article_db(self.database_root)
        for key in self.database_structure.keys():
            print "----------------------------------"
            print key + " : "
            if self.database_structure[key] != []:
                for inner_key in self.database_structure[key]:
                    print "\t"+inner_key + " : "
                    for value in values:
                        print "\tValue: " + str(value)
                        print "Key: " + key + " , inner_key: " + inner_key + " , value: "+value
                        print "\t\t"+str(len(sentiment_words_db[key][inner_key][value]))
            else:
                for value in values:
                    print "\tValue: " + str(value)
                    print key + " : " + str(len(sentiment_words_db[key][value]))
        print "END--------------------------------"

        self.__fill_database_with_new_words(sentiment_words_db, article_db, feature)

    def __get_article_db(self, database_root):
        if not database_root.has_key('articles_db'):
            raise Exception("No database for articles available")
        return database_root['articles_db']

    def __create_sentiment_words_database(self, feature, values):
        database_name = feature+'_words'
        if not self.database_root.has_key(database_name) :
            print "Creating new " + database_name + " database"
            self.database_root[database_name] = OOBTree()
            words_database = self.database_root[database_name]

            for key in self.database_structure.keys():
                print "----------------------------------"
                words_database[key] = OOBTree()
                key_database = words_database[key]
                if self.database_structure[key] != []:
                    for inner_key in self.database_structure[key]:
                        key_database[inner_key] = OOBTree()
                        key_database[inner_key]['most_frequent'] = dict()
                        for value in values:
                            key_database[inner_key][value] = []
                            key_database[inner_key]['most_frequent'][value] = []
                else:
                    key_database['most_frequent'] = dict()
                    for value in values:
                        key_database[value] = []
                        key_database['most_frequent'][value] = []
            print "END--------------------------------"
            transaction.commit()
        return self.database_root['sentiment_words']

    def __fill_database_with_new_words(self, words_database, articles_db, feature_name):
        articles = self.__extract_new_articles_keys(articles_db, feature_name)
        print "Articles to be proceeded: " + str(len(articles))
        for key in articles:
            print "Updating article : " + key
            self.__extract_bigram_words(articles_db[key], words_database['bigrams'], feature_name)
            self.__extract_level_words(articles_db[key], words_database['levels'], '1', feature_name)
            self.__extract_level_words(articles_db[key], words_database['levels'], '2', feature_name)
            self.__extract_level_words(articles_db[key], words_database['levels'], '3', feature_name)
            setattr(articles_db[key], feature_name+'_uploaded', True)
        print transaction.commit()
    def __extract_new_articles_keys(self, article_db, feature_name):
        articles_with_sentiment = []
        for key in article_db.keys():
            if hasattr(article_db[key], feature_name):
                articles_with_sentiment.append(key)
        print 'articles_with_sentiment len: ' + str(len(articles_with_sentiment))
        return [key for key in articles_with_sentiment if not hasattr(article_db[key], feature_name+'_uploaded')]

    def __extract_bigram_words(self, article, bigrams, feature_name):
        bigrams[getattr(article, feature_name, '')].extend(article.bigrams)
        bigrams._p_changed = True

    def __extract_level_words(self, article, levels_db, level, feature_name):
        article_levels = article.frequency_distribution_levels
        levels_db[level][getattr(article, feature_name, '')].extend(article_levels[level])
        levels_db[level]._p_changed = True
