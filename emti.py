import pymongo


uri = "mongodb+srv://<cosmo>:<cosmo>@cluster0.nfkbemi.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)


db = client['Cosmo']

col = db['Users']

test = {
    "name": "Cosmo",
    "age": 21,
}

col.insert_one(test)