class Guess:
    guessedChars = set([])
    numTries = 0

    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(word)

    def display(self):
        print("Current :", self.currentStatus)
        print("Tries :", self.numTries)

    def guess(self, character):
        self.guessedChars.add(character)
        changed = False
        for i in range(len(self.currentStatus)):
            if self.secretWord[i] == character and self.currentStatus[i] == '_':
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
                changed = True

        if not changed:
            self.numTries += 1
        return not ('_' in self.currentStatus)
