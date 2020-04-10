from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
client=MongoClient("mongodb+srv://201701230:201701230@parth-mwo9a.mongodb.net/test?retryWrites=true&w=majority")
db=client["201701230"]
try:
    client.admin.command('ismaster')

except ConnectionFailure:
    print('Server not available')

except OperationFailure:
    print('wrong credentials')

else:
    print('connected established to database')
    casa=db.Sales.aggregate([{ "$group": { "_id": "$storeLocation", "total": { "$sum":1 } } }])


finally:
	client.close()

for docs in casa:
    print(docs)
