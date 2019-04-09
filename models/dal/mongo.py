from pymongo import MongoClient
from bson.objectid import ObjectId
from models.dal.basedal import BaseDal

class Mongo(BaseDal):

	host = 'mongo'
	port = 27017
	database = 'log'

	def __init__(self, collection):
		try:
			client = MongoClient(self.host, self.port)
			db = client[self.database]
			self.collection = db[collection]
		except Exception as e:
			print(e)

	def insert(self, data):
		return self.collection.insert_one(data).inserted_id

	def findById(self, id):
		return self.collection.find_one(({"_id": ObjectId(str(id))}))

	def find(self, field, value):
		return self.collection.find(({field: value}))

	def findAll(self, skip, limit):
		return self.collection.find({},{"_id": 0}).skip(int(skip)).limit(int(limit))

	def remove(self, id):
		return self.collection.delete_one(({"_id": ObjectId(str(id))})).deleted_count