from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from keypad import operatorList, constantList, functionList
import calcFunctions
import math

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        #숫자버튼 생성하기
        for i in range(0,10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()
        numLayout = QGridLayout()

        buttonGroups = {
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }


        # Operator Buttons, Function Buttons, Constant Buttons
        for label in buttonGroups.keys():
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # 숫자버튼 배열하기(버튼 0은 따로 처리함)
        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], (8 - (i - 1)) / 3, (i - 1) % 3)

        numLayout.addWidget(self.digitButton[0], 3, 0)

        # . and = Buttons (따로 처리해줌)
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)
        # '.' , '='
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        try:

            if self.display.text() == 'Error!':
                self.display.setText('')

            button = self.sender()
            key = button.text()

            if key == '=':
                result = str(eval(self.display.text()))
                # 부동소수를 처리해준 값을 리턴해줍니다!
                self.display.setText(calcFunctions.floatPoint(result))

            elif key == 'C':
                self.display.setText('')

            elif key == constantList[0]: # Pi
                self.display.setText(self.display.text() + '3.141592')

            elif key == constantList[1]: # 빛의 이동 속도
                self.display.setText(self.display.text() + '3E+8')

            elif key == constantList[2]: # 소리의 이동 속도
                self.display.setText(self.display.text() + '340')

            elif key == constantList[3]: # 태양과의 평균 거리
                self.display.setText(self.display.text() + '1.5E+8')

            elif key == functionList[0]: # Factorial
                n = self.display.text()
                value = calcFunctions.factorial(n)
                self.display.setText(str(value))

            elif key == functionList[1]: # dec -> binary
                n = self.display.text()
                value = calcFunctions.decToBin(n)
                self.display.setText(str(value))

            elif key == functionList[2]: # binary -> dec
                n = self.display.text()
                value = calcFunctions.binToDec(n)
                self.display.setText(str(value))

            elif key == functionList[3]: # dec -> roman
                n = self.display.text()
                value = calcFunctions.decToRoman(n)
                self.display.setText(str(value))
            else:
                self.display.setText(self.display.text() + key)
        except:
            pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())






# calcFunctions 소스 코드
'''
from math import factorial as fact
def factorial(numStr):
    try:
        n = int(eval(numStr)) #괄호안의 값 먼저 처리
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(eval(numStr)) #이것또한 마찬가지
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'

#부동소수를 처리하기 위한 함수
def floatPoint(result):
    a = float(result)
    intA = int(a)
    floatA = a - intA
    strfloatA = str(floatA)
    for i in range(len(strfloatA)-2):
        if strfloatA[i] == strfloatA[i+1] == strfloatA[i+2]:
            b = round(floatA,14)
    r = str(intA + b)
    return r
'''
