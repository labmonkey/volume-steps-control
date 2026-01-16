import shelve
import tempfile
import os

class Storage:

    def __init__(self, storage_name):
        self.shelve_path = os.path.join(tempfile.gettempdir(), storage_name)

    def setStorageValue(self, key, value):
        with shelve.open(self.shelve_path) as db:
            db[key] = value

    def getStorageValue(self, key):
        with shelve.open(self.shelve_path) as db:
            return db[key]

    def hasStorageValue(self, key):
        with shelve.open(self.shelve_path) as db:
            return key in db