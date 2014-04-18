from BTrees.OOBTree import OOBTree
import transaction

class MostFrequentWordsExtractor(object):
    def __init__(self, database):
        self.database_root = database

    def updateMostFrequentWordsInDb(self):
        words_database = self.database_root['sentiment_words']
        self.__fillDatabaseWithMostFrequentWords(words_database)
    def __fillDatabaseWithMostFrequentWords(self, words_database):    
        self.__extractBigramWords(words_database['bigrams'])
        self.__extractLevelWords(words_database['levels'], '1')
        self.__extractLevelWords(words_database['levels'], '2')
        self.__extractLevelWords(words_database['levels'], '3')
        transaction.commit()

    def __extractBigramWords(self,bigrams):
        print "Todo"
    def __extractLevelWords(self, levels_db, level):
        print "Todo"


# //TODO
# Sprawdzanie najczestszych slow jakie występują dla positive/negative
# Wyciaganie ze sprawdzanego artykułu jakie ma slowa, tak jak dla tych w bazie
# Zaznaczanie w tablicy featurów to jakie słowa artykuł posiada a jakie nie
# Po wygenerowaniu tablicy ([slowo: true, slowo: false, ..., slowo: true], positive) wrzucić do serii uczącej
# Klasyfikacja oparta na tym samym tyle ze bez positive/negative
# Mozliwe wykorzystanie Bayesa, MLP, Kochonen