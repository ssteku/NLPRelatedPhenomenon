from ZODB import FileStorage, DB
import transaction
from BTrees.OOBTree import OOBTree

class DatabaseFacade(object):
    def __init__(self, path):
        self.storage = FileStorage.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()
        if not self.dbroot.has_key('test_results'):
            self.dbroot['test_results'] = OOBTree()

def close(self):
    self.connection.close()
    self.db.close()
    self.storage.close()