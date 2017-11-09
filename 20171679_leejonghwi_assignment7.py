from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,\
    QToolButton, QSizePolicy, QLayout, QGridLayout
from decimal import Decimal


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
        self.display.setMaxLength(15)

        self.operator = ['*', '/', '+', '-', '(', ')', 'C']
        self.pOper = ['.', '=']
        self.operator_inst = {}
        self.pOper_inst = {}
        # Digit Buttons
        self.digitButton = [Button(str(i), self.buttonClicked) for i in range(11)]

        # Operator instances
        for each in self.operator:
            self.operator_inst[each] = Button(each, self.buttonClicked)
        for each in self.pOper:
            self.pOper_inst[each] = Button(each, self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        numLayout = QGridLayout()
        opLayout = QGridLayout()

        # number btn add to num layout
        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], int(((10 - i) - 1) / 3), (i - 1) % 3)
        numLayout.addWidget(self.digitButton[0], 3, 0)

        # pOper btn add to main layout
        for i, x in enumerate(self.pOper):
            numLayout.addWidget(self.pOper_inst[self.pOper[i]], 3, i + 1)

        # Operator add to layout
        for i, x in enumerate(self.operator):
            opLayout.addWidget(self.operator_inst[x], int(i / 2), i % 2)

        # Setting Layout
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        key = self.sender().text()

        try:
            if key == '=':
                result = str(eval(self.display.text()))
                self.display.setText(result)
            elif key == 'C':
                self.display.setText('')
            else:
                self.display.setText(key if self.display.text() == '0' else self.display.text() + key)
        except:
            pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
