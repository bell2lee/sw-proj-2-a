class Guess:
    guessedChars = []
    def __init__(self, word):

        self.secretWord = word
        self.currentStatus = "_" * len(word)
        #시도 횟수 초기화
        self.numTries = 0


    def display(self):

        print("Current: ",self.currentStatus)
        print("Tries: ",self.numTries)

    def guess(self, character):
        self.guessedChars.append(character)

        if not (character in self.secretWord):
            self.numTries += 1

        #인자값이 배열이나 스트링이면 x값이 실제로 들어가고 i값이 카운트가 됨.
        for i, x in enumerate(self.secretWord):
            if character == x:
                frontslice = self.currentStatus[:i]
                backslice = self.currentStatus[i+1:]
                self.currentStatus = frontslice + character + backslice

        if '_' in self.currentStatus:
            return False
        else:
            return True
