from storage.DatabaseFacade import DatabaseFacade
import transaction

database = DatabaseFacade("./Database.fs")
database_root = database.dbroot
articles = database_root['articles_db']
if database_root.has_key('sentiment_words'):
    del database_root['sentiment_words']
if database_root.has_key('articles_db'):
    del database_root['articles_db']
for key in articles.keys():
    if hasattr(articles[key], 'sentiment'):
        print "deleting attr for "+key
        delattr(articles[key], 'sentiment')
        delattr(articles[key], 'uploaded')
        transaction.commit()