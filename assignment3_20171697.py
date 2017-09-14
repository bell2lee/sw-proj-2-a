import pickle
import math

dbfilename = 'assignment3_20171697.dat'

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
	inputstr = 0
	while inputstr != 'quit' :                        #while True 지양하기위해 바꿈
		inputstr = (input("Score DB > "))
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			if len(parse) > 4 or parse[1].isalpha() == False or parse[2].isnumeric() == False or parse[3] == False:
				Ele_Error_DB(parse[0])
			else:
				record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
				scdb += [record]
		elif parse[0] == 'del':
			if len(parse) > 2 or parse[1].isalpha() == False:
				Ele_Error_DB(parse[0])
			elif parse[1] not in scdb :
				print(parse[1],'does not exist!')
			else:
				for p in range(int(math.sqrt(len(scdb)))+1):
					for k in scdb :
						if k['Name'] == parse[1]:
							scdb.remove(k)
		elif parse[0] == 'show':
			if len(parse) > 1:
				Ele_Error_DB(parse[0])
			else :
				sortKey ='Name' if len(parse) == 1 else parse[1]
				showScoreDB(scdb, sortKey)
		elif parse[0] == 'find':
			if len(parse) > 1 or parse[1].isalpha() == False :
				Ele_Error_DB(parse[0])
			elif parse[1] not in scdb :
				print(parse[1],'does not exist!')
			else:Find_DB(scdb,parse[1])
		elif parse[0] == 'inc':
			if len(parse) > 3 or parse[1].isalpha() == False or parse[2].isnumeric() == False :
				Ele_Error_DB(parse[0])
			else:
				Inc_DB(scdb,parse[1],parse[2])
		else:
			print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()

#Find 처리 함수
def Find_DB(scdb, keyname) :
	name_lis = []
	for attr in scdb:
		if attr['Name'] == keyname:
			val = ('Name:' + attr['Name'] + ',Age:' + attr['Age'] + ',Score:' + attr['Score'] + '\n')
			name_lis.append(val)
	print("".join(name_lis))

#Inc 처리 함수
def Inc_DB(scdb,keyname,keyscore):
	for attr in scdb:
		if attr['Name'] == keyname:
			attr['Score'] = str(int(attr['Score']) + int(keyscore))

#요소 값 에러처리 함수
def Ele_Error_DB(par) :
	no_ele = ['show','quit']
	one_ele = ['del','find']
	two_ele = ['inc']
	three_ele = ['add']
	if par in no_ele :
		print(par, 'must have no Elements!!')
	elif par in one_ele :
		print(par, 'must have one string Elemnts!!')
	elif par in two_ele :
		print(par, 'must have two Elements!! Two elements are Name and Score!')
	elif par in three_ele :
		print(par, 'must have three Elements!! Three elements are Name, Age and Score! ')

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
