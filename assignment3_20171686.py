import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			scdb += [record]
		elif parse[0] == 'del':
			for p in scdb:
				if p['Name'] == parse[1]:
					scdb.remove(p)
					break
		elif parse[0] == 'find':
			findname(scdb, parse[1])
		elif parse[0] == 'inc':
			incscore(scdb,parse[1],parse[2])
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()

#find 명령 소스 코드
def findname(scdb,name):
	for a in scdb:
		if a['Name'] == name:
			print(a['Name'], a['Age'], a['Score'])

#inc 명령 소스 코드
def incscore(scdb, name, score):
	for i in scdb:
		if i['Name'] == name:
			i['Score'] = str(int(i['Score'])+ int(score))

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

