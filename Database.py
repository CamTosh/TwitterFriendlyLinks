from pymongo import MongoClient
import pendulum
import json


class DB(object):

	def __init__(self):
		
		c = MongoClient('192.168.1.42', 27017)
		self.db = c.twitter


	def getObjectWithID(self, userId):
		id = self.db.twitter.find({
				"id": str(userId)
			})
		
		return str(id)


	def getObjectWithName(self, userName):
		name = self.db.twitter.find({
				"id": str(userName)
			})
		
		return str(name)


	def addUser(self, user):
		now_in_paris = pendulum.now('Europe/Paris')

		self.db.twitter.insert_one({
		  "date": str(now_in_paris.in_timezone('UTC')),
		  "name": user.getName(),
		  "id": user.getId(),
		  "friends": user.getFriends()
		})