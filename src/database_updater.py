from storage.DatabaseFacade import DatabaseFacade
import transaction

database = DatabaseFacade("./Database.fs")
database_root = database.dbroot
articles = database_root['articles_db']
print "Database size: " + str(len(articles.keys()))




non_clasified_keys = [key for key in articles.keys() if not hasattr(articles[key], 'sentiment')]
print "To be clsified: size: "
print str(len(non_clasified_keys))
print "---------------------------------"
for key in non_clasified_keys:
    print "Title : " + key
    print "Keywords: " + str(articles[key].benchmark_keywords)
    print "Summary: " + (articles[key].benchmark_summary)
    print "Bigrams " + str(articles[key].bigrams)
    answer = raw_input('Choose sentiment of article(P/N): ')
    if answer.lower() == 'n':
        setattr(articles[key], "sentiment" , 'negative')
    elif answer.lower() == 'p':
        setattr(articles[key], "sentiment" , 'positive')
    transaction.commit()
    print 'Sentiment : %s \n' + str(answer)