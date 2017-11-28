from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:
        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()
        guessedChar = input('Select a letter: ')
        if guessedChar.isalpha():
            if len(guessedChar) != 1:
                print('One character at a time!')
                continue
            if guessedChar in guess.guessedChars:
                print('You already guessed \"' + guessedChar + '\"')
                continue
            finished = guess.guess(guessedChar)
            if finished == True:
                break
        else:
            print('You must input Alphabet!!!')
            continue

    if finished == True:
        print('Success!! The answer is %s!!' %guess.secretWord)
    else:
        print(hangman.get(0))
        print('It is your guessed spell :', guess.guessedChars)
        print('Current : ', guess.currentStatus)
        print('Your Last Chance!! Insert Full Word!!')
        lastanswer = input('>>>>>>>> ')
        if lastanswer == guess.secretWord:
            print('Success!!')
        else:
            guess.answer = lastanswer
            print('word [' + guess.secretWord + ']')
            print('guess [' + guess.answer + ']')
            print('Fail')


if __name__ == '__main__':
    gameMain()
