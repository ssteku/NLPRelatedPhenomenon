from BTrees.OOBTree import OOBTree
from ZODB import FileStorage, DB


class DatabaseFacade(object):
    def __init__(self, path):
        self.storage = FileStorage.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()
        if 'test_results' not in self.dbroot:
            self.dbroot['test_results'] = OOBTree()

def close(self):
    self.connection.close()
    self.db.close()
    self.storage.close()