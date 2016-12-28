from twitter import *

class TwitterApi(object):

	def __init__(self, token):

		self.tw = Twitter(
			auth=OAuth(token.getAccess_token(), token.getAccess_token_secret(), token.getConsumer_key(), token.getConsumer_secret()))


	def check(self):
		return self.tw.account.verify_credentials()['id']


	def setTarget(self, id):
		self.target = id

		return self.target

	def getTarget(self):
		if self.target:
			return self.target
		else:
			return "No target"

	def findFriends(self):
		return self.tw.friends.ids()['ids']