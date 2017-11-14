from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy, QLayout, QGridLayout, QLineEdit, QToolButton

from keypad import numPadList, operatorList, constantList, functionList


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
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(25)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }



        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

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

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
                if '.' in result:
                    # 소수 일 경우
                    a = result.split('.')
                    result = a[0] + "." + str(round(float("0." + a[1]), 14)).replace("0.", "")
            except:
                result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()
        elif key in constantList.keys():
            self.display.setText(self.display.text() + constantList[key])
        elif key in functionList:
            n = self.display.text()
            value = functionList[key](eval(n))
            self.display.setText(str(value))
        elif key == '0' and self.display.text() == '0':
            pass
        elif key == '.' and (self.display.text().find(".") != -1 or not self.display.text()):
            pass
        elif key == '◀':

            re = self.display.text()
            if len(re) != 0:
                self.display.setText(re[:len(re)-1])
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())