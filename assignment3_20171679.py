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
        scdb = pickle.load(fH)
        for p in scdb:
            p["Score"] = int(p["Score"])
            p["Age"] = int(p["Age"])

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
    while (True):
        inputstr = (input("Score DB > "))
        if not inputstr: continue
        parse = inputstr.split(" ")

        try:
            if parse[0] == 'add':
                # 변환 시 오류 체크
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]
            elif parse[0] == 'del':
                delDB(scdb,parse[1])
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'find':
                findDB(scdb, parse[1])
            elif parse[0] == 'inc':
                incDB(scdb, parse[1], parse[2])
            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])
        except (IndexError, ValueError):
            print("Parameter error. EX : add Lee 22 100")
        #except:
        #    print("\nError! Please check your command")



def delDB(scdb, name):
    # 리스트를 복사해야함. scdb에서 remove(p)를 사용하면 리스트의 길이가 줄어들어서 마지막 한개의 값을 검증하지 않음.
    tmp = scdb[:]
    delete_complete = False
    for p in tmp:
        if p['Name'] == name:
            scdb.remove(p)
            delete_complete = True

    if delete_complete == False:
        print("This name does not exist.")

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()

# 아래 부터 새로 짠 코드

def findDB(scdb, name):
    find_complete = False
    print(scdb)
    for p in scdb:
        print(p)

    for p in scdb:
        if p['Name'] == name:
            for attr in p:
                print(attr + "=" + p[attr], end=' ')
            find_complete = True
            print()

    if find_complete == False:
        print("This name does not exist.")

def incDB(scdb, name, amount):
    inc_complete = False
    for i in range(len(scdb)):
        if scdb[i]['Name'] == name:
            for attr in scdb[i]:
                print(attr + "=" + str(scdb[i][attr]), end=' ')
            # 처리
            scdb[i]['Score'] = scdb[i]['Score'] + int(amount)
            inc_complete = True
            # 결과
            print(" up score :", scdb[i]['Score'])

    if inc_complete == False:
        print("This name does not exist.")

if __name__ == "__main__":
    scoredb = readScoreDB()
    doScoreDB(scoredb)
    writeScoreDB(scoredb)
