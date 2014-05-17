from BTrees.OOBTree import OOBTree
import transaction
class FeatureWordsDatabaseUpdater(object):
    def __init__(self, database, database_structure):
        self.database_root = database
        self.database_structure = database_structure

    def update_words_database(self, feature_name, values):
        feature_words_db = self.__create_feature_words_database(feature_name, values)
        article_db = self.__get_article_db(self.database_root)
        return self.__fill_database_with_new_words(feature_words_db, article_db, feature_name)

    def __get_article_db(self, database_root):
        if not database_root.has_key('articles_db'):
            raise Exception("No database for articles available")
        return database_root['articles_db']

    def __create_feature_words_database(self, feature_name, values):
        words_database = {}

        for key in self.database_structure.keys():
            words_database[key] = {}
            key_database = words_database[key]
            if self.database_structure[key] != []:
                for inner_key in self.database_structure[key]:
                    key_database[inner_key] = {}
                    for value in values:
                        key_database[inner_key][value] = []
            else:
                for value in values:
                    key_database[value] = []
        return words_database

    def __fill_database_with_new_words(self, words_database, articles_db, feature_name):
        articles = self.__extract_new_articles_keys(articles_db, feature_name)
        print "Articles to be proceeded: " + str(len(articles))
        for key in articles:
            # print "Updating article : " + key
            self.__extract_bigram_words(articles_db[key], words_database['bigrams'], feature_name)
            self.__extract_level_words(articles_db[key], words_database['levels'], '1', feature_name)
            self.__extract_level_words(articles_db[key], words_database['levels'], '2', feature_name)
            self.__extract_level_words(articles_db[key], words_database['levels'], '3', feature_name)
        return words_database

    def __extract_new_articles_keys(self, article_db, feature_name):
        articles_with_feature = []
        for key in article_db.keys():
            if hasattr(article_db[key], feature_name):
                articles_with_feature.append(key)
        print 'articles_with_feature len: ' + str(len(articles_with_feature))
        return articles_with_feature

    def __extract_bigram_words(self, article, bigrams, feature_name):
        bigrams[getattr(article, feature_name, '')].extend(article.bigrams)

    def __extract_level_words(self, article, levels_db, level, feature_name):
        article_levels = article.frequency_distribution_levels
        levels_db[level][getattr(article, feature_name, '')].extend(article_levels[level])
