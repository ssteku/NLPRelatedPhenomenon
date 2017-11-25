import transaction

from src.storage.DatabaseFacade import DatabaseFacade

database = DatabaseFacade("./Database.fs")
database_root = database.dbroot
articles = database_root['articles_db']
if database_root.has_key('sentiment_words'):
    del database_root['sentiment_words']
if database_root.has_key('articles_db'):
    del database_root['articles_db']

transaction.commit()