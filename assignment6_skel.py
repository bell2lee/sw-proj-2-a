import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import math


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.dic = {}
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []

        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        vbox = QVBoxLayout()
        hbox = [QHBoxLayout() for x in range(5)]

        labellis = ['Name', 'Age', 'Score', 'Amount']
        for name in labellis:
            label = QLabel(name)
            self.dic[name] = QLineEdit()
            hbox[0].addWidget(label)
            hbox[0].addWidget(self.dic[name])
            vbox.addLayout(hbox[0])

        label = QLabel('Key:')
        self.Combo = QComboBox()
        self.Combo.addItems(['--SECTION--', 'Name', 'Age', 'Score'])
        hbox[1].addWidget(label)
        hbox[1].addWidget(self.Combo)
        hbox[1].addStretch(1)
        vbox.addLayout(hbox[1])


        buttonlis = ['Add', 'Del', 'Find', 'Inc', 'Show']
        for name in buttonlis:
            button = QPushButton(name)
            if name == 'Add':
                button.clicked.connect(self.do_add_act)
            elif name == 'Del':
                button.clicked.connect(self.do_del_act)
            elif name == 'Find':
                button.clicked.connect(self.do_find_act)
            elif name == 'Inc':
                button.clicked.connect(self.do_inc_act)
            else:
                button.clicked.connect(self.do_show_act)
            hbox[2].addWidget(button)
            vbox.addLayout(hbox[2])

        result = QLabel('Result:')
        hbox[3].addWidget(result)
        vbox.addLayout(hbox[3])

        self.Resultedit = QTextEdit()
        hbox[4].addWidget(self.Resultedit)
        vbox.addLayout(hbox[4])


        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
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

    def showScoreDB(self, keyname = 'Name'):
        string = ''
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                string += (attr + "=" + str(p[attr]) + '\t')
            string += '\n'
            self.Resultedit.setText(string)

    def do_add_act(self):
        name =self.dic['Name'].text()
        age = int(self.dic['Age'].text())
        score = int(self.dic['Score'].text())
        record = {'Name':name, 'Age':age, 'Score':score}
        self.scoredb += [record]
        self.showScoreDB()

    def do_del_act(self):
        name = self.dic['Name'].text()
        for p in range(int(math.sqrt(len(self.scoredb)))):
            for i in self.scoredb:
                if i['Name'] == name:
                    self.scoredb.remove(i)
        self.showScoreDB()

    def do_find_act(self):
        name_lis = []
        for i in self.scoredb:
            if i['Name'] == self.dic['Name'].text():
                string = ('Name=' + i['Name'] + ' Age=' + str(i['Age'])
                          + ' Score=' + str(i['Score']) +'\n')
                name_lis.append(string)
        self.Resultedit.setText("".join(name_lis))


    def do_inc_act(self):
        for attr in self.scoredb:
            if attr['Name'] == self.dic['Name'].text():
                attr['Score'] = str(int(attr['Score']) + int(self.dic['Amount'].text()))
        self.showScoreDB()

    def do_show_act(self):
        try:
            string = ''
            keyname = self.Combo.currentText()
            for p in sorted(self.scoredb, key=lambda person: person[keyname]):
                for attr in sorted(p):
                    string += (attr + "=" + str(p[attr]) + '\t')
                string += '\n'
                self.Resultedit.setText(string)
        except KeyError as e:
            pass

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





