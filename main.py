from Token import Token, LoadToken
from TwitterApi import TwitterApi
import json

if __name__ == '__main__':
	l = LoadToken()
	dico = l.load("token.json")

	d = {}

	for i in l.createToken(dico):
		t = TwitterApi(i)
		dUser = {}
		friends = []
		
		# je parcour les amis
		for f in t.findFriends():
			dUser['name'] = f['screen_name']
			dUser['id'] = f['id']

			# je parcour les amis des amis
			try:
				friendsOfFriends = []

				for fof in t.findFriendsWithId(f['id']):
					friendsOfFriends.append(fof['screen_name'])
			
				dUser['friends'] = friendsOfFriends
			except Exception as e:
				print(e)

			friends.append(dUser)
		d[t.check()['id']] = friends

	print(json.dumps(d))
