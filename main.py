from Token import Token, LoadToken
from TwitterApi import TwitterApi
from Database import DB
import json


if __name__ == '__main__':
	l = LoadToken()
	dico = l.load("token.json")

	d = {}

	for i in l.createToken(dico):
		try:
			t = TwitterApi(i)

			friends = []

			for f in t.findFriends():
				dUser = {}
				dUser['name'] = f['screen_name']
				dUser['id'] = f['id']
				
				"""
				friendsOfFriends = []

				for fof in t.findFriendsWithId(f['id']):
					friendsOfFriends.append(fof['screen_name'])
					dUser['friends'] = friendsOfFriends
				"""
				
				friends.append(dUser)
			d[t.check()['id']] = friends
			
		except Exception as e:
			print(e)

	print(json.dumps(d))
