import pymongo 

mongo_url = "mongodb+srv://class:4asYZandEhrSbJIm@cluster0.ikguw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url)

db = client.get_database("StoreRegis")