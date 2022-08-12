import couchdb

couch = couchdb.Server('http://usman:hitman786@127.0.0.1:5984')
# db = couch['python-tests']
# mango = {
#     'selector': {'type': 'Person'},
#     'fields': ['name']
#     }
# for row in db.find(mango):
#     print(row['name']) 

db = couch['db_test']
# mango = {
#     'selector': {'content':{'email': 'pdude@gmail.com'}},
#     }
# for row in db.find(mango):
#     print(row) 

# print([i for i in db.find(mango)])
def search(db, query):
    mango = {
    'selector': query,
    }
    return [i for i in db.find(mango)]

query = {'content':{'email': 'pdude@gmail.com'}}
print(search(db, query))