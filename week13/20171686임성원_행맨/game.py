from hangman import Hangman
from guess import Guess
from word import Word
import re

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

        guessedChar = input('Select a letter: ').lower() # 대문자가 들어와도 소문자로 취급
        # []안의 내용을 컴파일하여 정규식 객체를 반환
        r = re.compile('[^ ㄱ-ㅣ가-힣]+')
        #guessedChar에서 공백을 제외한 문자들을 문자열로 반환
        result = r.sub('',guessedChar)

        if guessedChar.isdigit():
            print("알파벳을 입력해 주세요.")
            continue
        elif guessedChar in result:
            print("알파벳을 입력해 주세요.")
            continue
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
