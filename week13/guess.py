class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = '_' * len(word)


    def display(self):
        print("Current: " + self.currentStatus)
        print("Tries: " + str(self.numTries))
        print("guessedChars: ", self.guessedChars)


    def guess(self, character):
        self.guessedChars.append(character)
        if character not in self.secretWord:
            self.numTries += 1
            return False
        else:
            currentStatus = ''
            for character in self.secretWord:
                if character in self.guessedChars:
                    currentStatus += character
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus

            return self.currentStatus == self.secretWord