import random

class Word:

    def __init__(self, filename):

        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip() #공백, Tab, 개행문자를 모두 없애주기 위함.
            self.words.append(word) #words 리스트에 단어들을 담음.
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):

        r = random.randrange(self.count)
        return self.words[r]
