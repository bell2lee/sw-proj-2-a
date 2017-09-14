
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


        if inputstr == "": continue
        parse = inputstr.split(" ")


        try:
            ((parse[0] =="del") and (len(parse[1])< 1)) or ((parse[0] =="add") and (len(parse[1])< 1)) or ((parse[0] =="inc") and (len(parse[1])< 1)) or ((parse[0] =="find") and (len(parse[1])< 1))

        except IndexError:
            print("값을 입력하시요 ")
            continue

        try:
            (parse[0]=="inc") and (len(parse[2])<1) or (parse[0]=="add") and (len(parse[2])<1)


        except IndexError:
            print("두번째 값을 입력하시요 ")
            continue

        try:
            (parse[0]=="add") and (len(parse[3])<1)


        except IndexError:
            print("세번째 값을 입력하시요 ")
            continue






        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            scdb += [record]



        elif parse[0] == 'del':



            for p in scdb:
                for i in p:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                    break

        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break


        elif parse[0] == "find":
            for p in scdb:

                for attr in p:
                    if p['Name'] == parse[1]:
                        print(attr + "=" + p[attr], end=' ')

        elif parse[0] == "inc":
            for ssa in scdb:
                for attaa in ssa:
                    if ssa['Name'] == parse[1]:

                        if attaa == "Score":
                            ssa[attaa]= int(ssa[attaa])+int((parse[2]))
                            ssa[attaa]= str(ssa[attaa])
                            print(attaa + "=" + ssa[attaa], end=' ')
                        else:
                            print(attaa + "=" + ssa[attaa], end=' ')




        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)


