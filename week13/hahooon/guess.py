class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.answer =''
        self.currentStatus = '*'*len(self.secretWord)

    def display(self):
        print('It is your guessed spell :', self.guessedChars)
        print('Current : ', self.currentStatus)
        print('Tries : ',self.numTries)
        print('Life : %d' %(6-self.numTries) )

    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord:
            if character not in self.answer:
                self.answer += character
            for i in range(len(self.secretWord)):
                if character == self.secretWord[i]:
                    self.currentStatus = self.currentStatus[:i] + character +\
                                         self.currentStatus[i+1:]
            return self.currentStatus == self.secretWord

        else:
            self.numTries += 1