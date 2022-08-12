from queries import *

server = Server()
token = server.login("muneeb", "admin")
# db = server.get_database("latest")
# db = server.create_database("latest")
# record1 = dict(name = "Gill Gandu", gpa=2.9, batch="19", address="Wapda Town, Lahore")
# record2 = dict(name="Hamza Bondu", gpa = 3.4, batch="19")
# record3 = dict(name="Ibrahim Banana", gpa=3.8, batch="19", department="CS", degree="BS")
# db.add_doc(record1, key="BSCS19010")
# db.add_doc(record2, key="BSCS19017")
# db.add_doc(record3, key="BSCS19003")

# doc = db.get_doc("BSCS19017")
# doc.update(["address"], ["Multan"])
# print(f"after updating doc {doc}")


# query = {'gpa': {'$gte' : 3}}
# query = {'name':'Gill Gandu'}
# ans = db.search(query)
# print(ans)

# db = couch.create('python-tests')
# db = couch['python-tests']
# doc_id, doc_rev = db.save({'type': 'Person', 'name': 'John Doe'})
# print("doc_id: ", doc_id)

# print("get the document with this id: ", doc_id)
# doc = db[doc_id]
# print("Initial value of field 'name' in doc")
# print(f"doc['name']: {doc['name']}")



# print("change the value of field 'name' in doc")
# doc['name'] = 'Mary Jane'
# print(f"doc['name']: {doc['name']}")

# print("save() create with random id")
# db['BSCS19010'] = {'name': 'Usman Gill', 'gpa': 3.5}
# print('BSCS19010' in db)

# db['johndoe'] = dict(type='Person', name='John Doe')
# db['maryjane'] = dict(type='Person', name='Mary Jane')
# db['gotham'] = dict(type='City', name='Gotham City') 

def add_doc(db, doc, key=None):
    if key == None:
        db.save(doc)
    else:
        db[key] = doc

# add_doc(db, dict(type="Student", name="Ali", batch=19))
# add_doc(db, dict(type="Student", name="Fahad", batch=20), key="1")

def get_doc(db, id):
    return db[id]
    
def update(doc, id, value):
    for i, v in zip(id, value):
        doc[i] = v

# doc = get_doc(db, "1")
# update(doc, ["gpa", "address"], [3.7, "Lahore"])
# print(f"doc: {doc}")
# mango = {
#     'selector': {'type': 'Student'}
#     }
# for row in db.find(mango):
#     print(row)
    