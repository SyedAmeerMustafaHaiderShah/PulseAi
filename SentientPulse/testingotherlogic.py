from pymongo import MongoClient
# Try this long link - it bypasses the DNS SRV issue
client = MongoClient('mongodb://haider:haider@cluster0-shard-00-00.cfipozu.mongodb.net:27017,cluster0-shard-00-01.cfipozu.mongodb.net:27017,cluster0-shard-00-02.cfipozu.mongodb.net:27017/db1?ssl=true&replicaSet=atlas-m1sh7l-shard-0&authSource=admin&retryWrites=true&w=majority')
db= client['db1']
collection =db['youtube']
document= {"name": "sktech", "city": "pune"}
insert_doc =collection.insert_one(document)
print(f"instered Document ID: {insert_doc.inserted_id}")
client.close()