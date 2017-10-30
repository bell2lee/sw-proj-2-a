import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        hbox = QHBoxLayout()

        label_Name = QLabel("Name:", self)
        self.lineedit_Name = QLineEdit()
        label_Age = QLabel("Age:", self)
        self.lineedit_Age = QLineEdit()
        label_Score = QLabel("Score:", self)
        self.lineedit_Score = QLineEdit()
        label_Amount = QLabel("Amount: ", self)
        self.lineedit_Amount = QLineEdit()
        label_Key = QLabel("Key:", self)
        self.combobox_KeyCombo = QComboBox()
        self.combobox_KeyCombo.addItems(["Name", "Age", "Score"])
        hbox.addStretch(1)
        hbox.addWidget(label_Name)
        hbox.addWidget(self.lineedit_Name)
        hbox.addWidget(label_Age)
        hbox.addWidget(self.lineedit_Age)
        hbox.addWidget(label_Score)
        hbox.addWidget(self.lineedit_Score)
        hbox.addWidget(label_Amount)
        hbox.addWidget(self.lineedit_Amount)
        hbox.addWidget(label_Key)
        hbox.addWidget(self.combobox_KeyCombo)



        xbox = QHBoxLayout()

        Add = QPushButton('Add', self)
        Add.clicked.connect(self.do_add)
        Del = QPushButton('Del', self)
        Del.clicked.connect(self.do_del)
        Find = QPushButton('Find', self)
        Find.clicked.connect(self.do_find)
        Inc = QPushButton('Inc', self)
        Inc.clicked.connect(self.do_inc)
        Show = QPushButton('Show', self)
        Show.clicked.connect(self.do_show)
        xbox.addWidget(Add)
        xbox.addWidget(Del)
        xbox.addWidget(Find)
        xbox.addWidget(Inc)
        xbox.addWidget(Show)



        nbox = QHBoxLayout()
        Result = QLabel("Result:", self)
        nbox.addWidget(Result)



        lbox = QHBoxLayout()

        xx = QLabel("", self)
        lbox.addWidget(xx)



        mbox = QHBoxLayout()
        self.textedit_Result = QTextEdit(self)
        mbox.addWidget(self.textedit_Result)



        vbox = QVBoxLayout()

        vbox.addLayout(hbox)
        vbox.addLayout(xbox)
        vbox.addLayout(lbox)
        vbox.addLayout(nbox)
        vbox.addLayout(mbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname="Name"):
        string = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                string += attr + "=" + str(p[attr]) + '\t'
            string += "\n"
        self.textedit_Result.setText(string)

    def do_add(self):
        name = self.lineedit_Name.text()
        age = self.lineedit_Age.text()
        score = self.lineedit_Score.text()
        record = {'Name': name, 'Age': int(age), 'Score': int(score)}
        self.scoredb += [record]
        self.showScoreDB()

    def do_del(self):
        name = self.lineedit_Name.text()
        a = self.scoredb[:]
        for p in a:
            if p['Name'] == name:
                self.scoredb.remove(p)
        self.showScoreDB()

    def do_find(self):
        name = self.lineedit_Name.text()
        string = ""
        for a in self.scoredb:
            if a['Name'] == name:
                string += 'Name=' + str(a['Name']) + "\t" + 'Age=' + str(a["Age"]) + "\t" + 'Score=' + str(a['Score'])
                string += '\n'
        self.textedit_Result.setText(string)

    def do_inc(self):
        name = self.lineedit_Name.text()
        score = self.lineedit_Amount.text()
        for i in self.scoredb:
            if i['Name'] == name:
                i['Score']= int(i['Score'])+int(score)
        self.showScoreDB()

    def do_show(self):
        self.showScoreDB(self.combobox_KeyCombo.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
