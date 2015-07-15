import pymongo
import traceback

class LibMongo(object):
    def __init__(self, host, port):
        """
        Establish the connection by connecting to the host and port
        :param : host
        :param : string
        :param : port
        :param : integer
        """
        self.host = host
        self.port = port
        self.Client = None
        self.db = None
        self.collection = None

    def dbconnect(self):
        """
        Connect to the host.
        """
        try:
            if self.Client is None:
                self.Client = pymongo.MongoClient(self.host, self.port)
        except pymongo.errors.OperationFailure as err:
            traceback(err)

    def dbcloseconnection(self):
        """
        Disconnect from host
        """
        try:
            if self.Client is not None:
                self.Client.close()
        except:
            traceback('Failed to disconnect the database')

    def dbconnectdatabase(self, dbname):
        """
        Establish connection to Database
        :params : dbname
        :type   : string
        """
        try:
            self.dbconnect()
            self.db = self.Client[dbname]
            self.dbcloseconnection()
        except pymongo.InvalidName as err:
            traceback(err)

    def getcollectionlist(self, dbname):
        """
        :params : dbname
        :type   : string
        """
        try:
            self.CollectionList = []
            self.dbconnect()
            self.db = self.Client[dbname]
            self.CollectionList = self.db.collection_names(include_system_collections = False)
            self.dbcloseconnection()
        except TypeError as err:
            traceback(err)

    def dbgetcollection(self, dbname, collection):
        """
        Check Collections and connect
        :params : dbname
        :type   : string
        :param  : collection
        :type   : string
        """
        try:
            self.dbconnect()
            self.db = self.Client[dbname]
            self.collection = self.db[collection]
            self.dbcloseconnection()
        except pymongo.InvalidName as err:
            traceback(err)

if __name__ == "__main__":
    DB= LibMongo('localhost',17710)
    DB.getcollectionlist('Companies')
    print DB.CollectionList
