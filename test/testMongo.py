from pymongo import MongoClient

mongo_client=MongoClient("mongodb://43.140.198.186:27017")

db=mongo_client["users"]
db.create_collection("document")

db["document"].insert_one({"name":"zhangsan","age":"12"})
