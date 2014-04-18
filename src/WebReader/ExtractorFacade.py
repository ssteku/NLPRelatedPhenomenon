import newspaper
from newspaper import Article
class ExtractorFacade(object):
    """ExtractorFacade class hiding dependencies"""
    """ to text from web extraction libs """
    def __init__(self, baseUrl):
        super(ExtractorFacade, self).__init__()
        print "Building extractor with url: ", baseUrl
        self.extractor = newspaper.build(baseUrl, memoize_articles=False, language='en')

    """ Extracts all articles from url """
    def getArticleList(self):
        print "Found articles num: ", len(self.extractor.articles)
        print "Also found categories num: ", len(self.extractor.categories)
        articles_list = self.extractor.articles
        # for category in self.extractor.category_urls():
        #     category_extraxtor = newspaper.build(category, memoize_articles=False, language='en')
        #     articles_list.extend(category_extraxtor.articles)
        print "Returning articles num: ",len(articles_list)
        return articles_list

        