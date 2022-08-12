import couchdb

couch = couchdb.Server('http://usman:hitman786@127.0.0.1:5984')

def add_database(couch, name):
    db = couch.create(name)
    return db

def add_doc(db, doc):
    db.save(doc)


#add entry
#remove entry
#get entry:
    #key
#update entry
#replication


# couch = couchdb.Server()
# print("done")
# db = couch.create('db_test2')
# db = couch['db_test'] # existing

# dic = {
#     'id': 777,
#     'content':{
#         'person_name': 'Gill and Muneeb Gandu',
#         'email':'myselfgandu@gmail.com'
#     }
# }
# db.save(dic)
# source = couch['companies']
# destination = couch['companies_2']


# db = couch.create('companies_2')
# source = 'hello '
# destination = 'hello_2'
# couch.replicate(source, destination, continuous=True)

db = couch['db_test']
print(db)
mongo = {
    'selector':{'email': 'pdude@gmail.com'},
    'fields':['person_name']
}
print(db.find(mongo))
# for row in db.find(mongo):
#     print(row['person_name'])
# explain = db.explain(mongo)
# print(explain)