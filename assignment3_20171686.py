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

#각 명령어마다 예외처리 넣어줌.
def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			if not parse[1].isalpha():
				print("Error! 정확한 값을 입력해 주세요")
				continue
			elif len(parse[2]) < 1 or len(parse[3]) < 1:
				print("정확한 값을 입력해 주세요")
				continue
			else:
				record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
				scdb += [record]
		#'del'처리 수정o
		elif parse[0] == 'del':
			if len(parse[1] <1):
				print("이름을 입력해 주세요")
				continue
			else:
				a = scdb[:]
				for p in a:
					if p['Name'] == parse[1]:
						scdb.remove(p)
		elif parse[0] == 'find':
			if not parse[1].isalpha():
				print("정확한 이름을 입력해 주세요")
				continue
			else:
				findname(scdb, parse[1])
		elif parse[0] == 'inc':
			if not parse[1].isalpha():
				print("정확한 이름을 입력해 주세요")
				continue
			elif len(parse[2]) <1:
				print("정확한 숫자를 입력해 주세요")
				continue
			elif not parse[2].isdigit():
				print("문자가 아닌 숫자를 입력해 주세요")
				continue
			elif len(parse[1] <1) or len(parse[2] <1):
				print("이름 또는 점수가 입력되지 않았습니다.")
				continue
			else:
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

