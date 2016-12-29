from Token import Token, LoadToken
from TwitterApi import TwitterApi
from Database import DB
from User import User
import json


if __name__ == '__main__':
	l = LoadToken()
	lesTokens = l.load("token.json")

	dicoUsers = {}
	listeUtilisateurs = []

	for tokens in l.createToken(lesTokens):
		try:
		
			t = TwitterApi(tokens)

			dUser = {}
			dUser["id"] = t.check()['id']
			dUser["name"] = t.check()['screen_name']

			lesAmis = []

			for friends in t.findFriends():
				dicoLesAmis = {}

				u = User(friends['id'], friends['screen_name'])
				dicoLesAmis['id'] = u.getId()
				dicoLesAmis['name'] = u.getName()

				lesAmis.append(dicoLesAmis)

			dUser["friends"] = lesAmis

			listeUtilisateurs.append(dUser)
			dicoUsers["users"] = listeUtilisateurs

		except Exception as e:
			print(e, tokens)
			
	print(json.dumps(dicoUsers))