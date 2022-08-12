import couchdb

class Server:
    def __init__(self, username, password) -> None:
        self.addr = f'http://{username}:{password}@127.0.0.1:5984'
        self.couch = couchdb.Server(self.addr)

    def get_database(self, name):
        self.DB = DB(self.couch[name])
        return self.DB

    def create_database(self, name):
        return DB(self.couch.create(name))
    

class DB:
    def __init__(self, original_db) -> None:
        self.database = original_db
    
    def search(self, query):
        mango = {
            'selector': query
            }
        return [i for i in self.database.find(mango)]

    def add_doc(self, doc, key=None):
        if key == None:
            self.database.save(doc)
        else:
            self.database[key] = doc

    def get_doc(self, key):
        return DOC(self.database[key])

class DOC:
    def __init__(self, original_doc) -> None:
        self.document = original_doc
    
    def __getitem__(self, key):
        return self.document[key]
    
    def update(self, id, value):
        for i, v in zip(id, value):
            self.document[i] = v

    def __str__(self) -> str:
        return str(self.document)
