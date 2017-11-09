import pickle, sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QMessageBox)
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
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        self.label_list = ["Name", "Age", "Score", "Amount"]
        self.button_list = ["Add", "Del", "Find", "Inc", "Show"]
        self.text_inst = {}
        self.button_inst = {}

        hbox = [QHBoxLayout() for x in range(5)]

        # 텍스트박스 설정
        for i in range(len(self.label_list)):
            tmp_label = QLabel(self.label_list[i] + " : ", self)
            self.text_inst[self.label_list[i]] = QLineEdit()
            if not i == (len(self.label_list) - 1) :
                hbox[0].addWidget(tmp_label)
                hbox[0].addWidget(self.text_inst[self.label_list[i]])
            else:
                hbox[1].addStretch(1)
                hbox[1].addWidget(tmp_label)
                hbox[1].addWidget(self.text_inst[self.label_list[i]])

        # 콤보박스 설정
        key_option_label = QLabel("Key : ", self)
        self.key_option = QComboBox(self)
        self.key_option.addItems(["Name", "Age", "Score"])
        hbox[1].addWidget(key_option_label)
        hbox[1].addWidget(self.key_option)

        # 2레이아웃 공백 설정
        hbox[2].addStretch(1)

        # 버튼 만들기
        for i in range(len(self.button_list)):
            self.button_inst[self.button_list[i]] = QPushButton(self.button_list[i])
            self.button_inst[self.button_list[i]].clicked.connect(self.pushButtonClicked)
            hbox[2].addWidget(self.button_inst[self.button_list[i]])

        # result 라벨 추가
        hbox[3].addWidget(QLabel("Result : "))
        hbox[3].addStretch(1)

        # result 창 설정
        self.result_edit = QTextEdit()
        hbox[4].addWidget(self.result_edit)

        # 최상단 레이아웃 선언
        vbox = QVBoxLayout()

        for i in range(len(hbox)):
            vbox.addLayout(hbox[i])

        self.setLayout(vbox)
        self.show()

    def pushButtonClicked(self):
        sender = self.sender().text()
        if sender == "Add":
            try:
                record = {'Name': self.text_inst["Name"].text(), 'Age': int(self.text_inst["Age"].text()), 'Score': int(self.text_inst["Score"].text())}
                self.scoredb += [record]
                self.showScoreDB()
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Name, age, score Please check the value.")
                msg.setWindowTitle("warning")
                msg.exec_()

        elif sender == "Del":
            try:
                tmp = self.scoredb[:]
                for p in tmp:
                    if p['Name'] == self.text_inst["Name"].text():
                        self.scoredb.remove(p)
                self.showScoreDB()
            except:
                self.msg_show("Name Please check the value.", "warning")
        elif sender == "Find":
            try:
                re = ""
                for p in sorted(self.scoredb, key=lambda x: x["Score"]):
                    for attr in sorted(p):
                        if p['Name'] == self.text_inst["Name"].text():
                            re += attr + "=" + str(p[attr]) + "\t"
                    else:
                        if p['Name'] == self.text_inst["Name"].text():
                            re += "\n"

                self.result_edit.setText(re)
            except:
                pass
        elif sender == "Inc":
            for i in range(len(self.scoredb)):
                if self.scoredb[i]['Name'] == self.text_inst["Name"].text():
                    self.scoredb[i]['Score'] = self.scoredb[i]['Score'] + int(self.text_inst["Amount"].text())

            self.showScoreDB()
        elif sender == "Show":
            self.showScoreDB(self.key_option.currentText())

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
        re = ""
        for p in sorted(self.scoredb, key=lambda x: x[keyname]):
            for attr in sorted(p):
                re += attr + "=" + str(p[attr]) + "\t"
            re += "\n"
        self.result_edit.setText(re)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
