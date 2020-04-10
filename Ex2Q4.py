#from pymongo import MongoClient
#client=MongoClient("mongodb+srv://201701230:201701230@parth-mwo9a.mongodb.net/test?retryWrites=true&w=majority")
#db=client["201701230"]
#casa=db.posts.find(
#{
#	"$or":
#	[
#		{"category":"Politics"},
#		{"number_of_views":{"$lte": 10},"author":"Jules Winnfield"}
#	]
#})
#for docs in casa:
#    print(docs)

#Recommended to use python try-except block to perform error handling.
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
    print('connected to database')
    casa=db.Sales.aggregate([{"$match":{"storeLocation":"Denver"}},{"$group":{"_id":"null","Total":{"$sum":{"$sum":{"$map":{"input": "$items","as": "i","in": {"$multiply": [ "$$i.price", "$$i.quantity" ]}}}}}}}])

finally:
	client.close()

for docs in casa:
    pprint(docs)
