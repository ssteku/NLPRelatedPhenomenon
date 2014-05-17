from storage.DatabaseFacade import DatabaseFacade
import transaction

def manual_clasification(feature = 'sentiment', values = ['negative', 'positive'], shortcuts = ['n','p']):
    non_clasified_keys = [key for key in articles.keys() if not hasattr(articles[key], feature)]
    print "To be clsified: size: "
    print str(len(non_clasified_keys))
    print "---------------------------------"
    for key in non_clasified_keys:
        print "Title : " + key
        print "Keywords: " + str(articles[key].benchmark_keywords)
        print "Summary: " + (articles[key].benchmark_summary)
        print "Bigrams " + str(articles[key].bigrams)
        answer = raw_input('Choose ' + feature + ' of article('+str(shortcuts)+'): ')
        if answer.lower() == shortcuts[0].lower():
            setattr(articles[key], feature , values[0])
        elif answer.lower() == shortcuts[1].lower():
            setattr(articles[key], feature , values[1])
        transaction.commit()
        print feature+' : %s \n' + str(answer)

database = DatabaseFacade("/home/ssteku/Database/Database.fs")
database_root = database.dbroot
articles = database_root['articles_db']
print "Database size: " + str(len(articles.keys()))
manual_clasification()

