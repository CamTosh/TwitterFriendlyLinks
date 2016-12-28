from Token import Token, LoadToken
from TwitterApi import TwitterApi


if __name__ == '__main__':
	l = LoadToken()
	dico = l.load("token.json")

	d = {}

	for i in l.createToken(dico):
		t = TwitterApi(i)
		d[t.check()] = str(t.findFriends())

	print(d)
