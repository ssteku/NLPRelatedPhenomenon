from BTrees.OOBTree import OOBTree
import transaction
class FeatureWordsDatabaseUpdater(object):
    def __init__(self, database, database_structure):
        self.database_root = database
        self.database_structure = database_structure

    def update_words_database(self, feature_name, values):
        feature_words_db = self.__create_feature_words_database(feature_name, values)
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
                        print "\t\t"+str(len(feature_words_db[key][inner_key][value]))
            else:
                for value in values:
                    print "\tValue: " + str(value)
                    print key + " : " + str(len(feature_words_db[key][value]))
        print "END--------------------------------"

        self.__fill_database_with_new_words(feature_words_db, article_db, feature_name)

    def __get_article_db(self, database_root):
        if not database_root.has_key('articles_db'):
            raise Exception("No database for articles available")
        return database_root['articles_db']

    def __create_feature_words_database(self, feature_name, values):
        database_name = feature_name+'_words'
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
        return self.database_root[database_name]

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
        articles_with_feature = []
        for key in article_db.keys():
            if hasattr(article_db[key], feature_name):
                articles_with_feature.append(key)
        print 'articles_with_feature len: ' + str(len(articles_with_feature))
        return [key for key in articles_with_feature if not hasattr(article_db[key], feature_name+'_uploaded')]

    def __extract_bigram_words(self, article, bigrams, feature_name):
        bigrams[getattr(article, feature_name, '')].extend(article.bigrams)
        bigrams._p_changed = True

    def __extract_level_words(self, article, levels_db, level, feature_name):
        article_levels = article.frequency_distribution_levels
        levels_db[level][getattr(article, feature_name, '')].extend(article_levels[level])
        levels_db[level]._p_changed = True
