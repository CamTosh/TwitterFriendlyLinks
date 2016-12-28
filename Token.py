import json


class Token(object):

	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):

		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret


	def __str__(self):
		return self.consumer_key + " " + self.access_token


	def getConsumer_key(self):
		return self.consumer_key

	def getConsumer_secret(self):
		return self.consumer_secret

	def getAccess_token(self):
		return self.access_token

	def getAccess_token_secret(self):
		return self.access_token_secret



class LoadToken(object):

	def __init__(self):
		pass

	def load(self, file):
		dico = {}

		with open(file, 'r') as f:
			dico = json.load(f)

		return dico['tokens']


	def createToken(self, dico):
		l = []

		for d in dico:
			t = Token(d['consumer_key'], d['consumer_secret'], d['access_token'], d['access_token_secret'])
			l.append(t)

		return l