from os import path
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys,sqlite3

# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname('untitled.ui'),'untitled.ui'))

class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        # btn = QPushButton()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.controllers()
        self.fill_table()
        self.menuBar.setVisible(False)
        self.pushButton_6.setVisible(False)
        global n
        self.n = 0

    def controllers(self):
        self.pushButton_4.clicked.connect(self.pin_btn)
        self.pushButton.clicked.connect(self.min_btn)
        self.pushButton_2.clicked.connect(self.max_btn)
        self.pushButton_3.clicked.connect(self.close_btn)

        self.pushButton_15.clicked.connect(self.add_name)
        self.pushButton_16.clicked.connect(self.delete)

        self.pushButton_18.clicked.connect(self.login)
        self.pushButton_19.clicked.connect(self.signup)
        self.lineEdit_4.textChanged.connect(self.check_text)
        self.pushButton_5.clicked.connect(self.show_menubar)
        self.pushButton_6.clicked.connect(self.back)

        # menuBar_themes
        self.menuThemes.triggered[QAction].connect(self.MenuBar_actions)

    def click_voice(self):
        # produce sound when click
        url = QtCore.QUrl.fromLocalFile(r"voices\click-voice.wav")
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer(self)  # its is important to put self inside, does not work without
        player.setMedia(content)
        player.setVolume(100)
        player.play()

    ############################################################################################
    ########Themes
    def MenuBar_actions(self, q):
        if q.text() == 'Original Theme':
            self.setStyleSheet('''''')

        if q.text() == 'Theme_1':
            with open('stylesheetes\dark_blue.txt', 'r') as f:
                a = f.read()
                self.setStyleSheet('''{}'''.format(a))

        if q.text() == 'Theme_2':
            with open('stylesheetes\dark_orange.txt', 'r') as f:
                a = f.read()
                self.setStyleSheet('''{}'''.format(a))

        if q.text() == 'Theme_3':
            with open('stylesheetes\stylesheet.txt', 'r') as f:
                a = f.read()
                self.setStyleSheet('''{}'''.format(a))

###############################################################################################
    def login(self):
        self.click_voice()

        ##fetch lineEdits data
        user_name = self.lineEdit.text()
        user_password = self.lineEdit_5.text()

        try:
            db = sqlite3.connect('database.db')
            cr = db.cursor()
            cr.execute('''SELECT * FROM users WHERE name=? AND password=?''',(user_name, user_password,))
            data = cr.fetchall()
            db.commit()
            db.close()
            if data[0][0]==user_name and data[0][1]==user_password:
                self.stackedWidget.setCurrentIndex(1)
                self.pushButton_6.setVisible(True)
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Authentification')
            msg.setInformativeText('the password or name is wrong')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

        self.lineEdit.setText('')
        self.lineEdit_5.setText('')

    def signup(self):
        self.click_voice()
        ##fetch lineEdits data
        user_name = self.lineEdit_7.text()
        user_password = self.lineEdit_6.text()
        password_again = self.lineEdit_8.text()

        ##check password and save in database
        if user_password==password_again:
            db = sqlite3.connect('database.db')
            cr = db.cursor()
            cr.execute('''INSERT INTO users(name, password) VALUES('{}','{}')'''.format(user_name, user_password))
            db.commit()
            db.close()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle('Authentification')
            msg.setInformativeText('the two password does not match')
            msg.setIcon(QMessageBox.Information)
            msg.exec()
        self.lineEdit_7.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_8.setText('')

    def back(self):
        self.click_voice()
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_6.setVisible(False)

    def check_text(self):
            db = sqlite3.connect('database.db')
            cr = db.cursor()
            cr.execute('''SELECT * FROM workers WHERE name LIKE '{}%' '''.format(self.lineEdit_4.text()))
            data = cr.fetchall()
            db.commit()
            db.close()

            self.tableWidget_3.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget_3.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

    def delete(self):
        self.click_voice()
        try:
            item = self.tableWidget_3.currentItem().text()
            db = sqlite3.connect('database.db')
            cr = db.cursor()
            cr.execute('''DELETE FROM workers WHERE name=?''', (item,))
            db.commit()
            db.close()
            self.fill_table()
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from tabk')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def add_name(self):
        self.click_voice()
        self.widg = QWidget()
        self.widg.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.widg.setStyleSheet('''background-color:rgb(73, 69, 200);''')

        self.line1 = QLineEdit(self.widg)
        self.line1.setPlaceholderText('Enter Name')
        self.line1.setStyleSheet('''background-color:white;''')

        self.line2 = QLineEdit(self.widg)
        self.line2.setPlaceholderText('Enter Job')
        self.line2.setStyleSheet('''background-color:white;''')

        self.line3 = QLineEdit(self.widg)
        self.line3.setPlaceholderText('Enter Section')
        self.line3.setStyleSheet('''background-color:white;''')

        self.line4 = QLineEdit(self.widg)
        self.line4.setPlaceholderText('Enter Phone')
        self.line4.setStyleSheet('''background-color:white;''')

        self.line5 = QLineEdit(self.widg)
        self.line5.setPlaceholderText('Enter Salary')
        self.line5.setStyleSheet('''background-color:white;''')

        self.line6 = QLineEdit(self.widg)
        self.line6.setPlaceholderText('Enter Address')
        self.line6.setStyleSheet('''background-color:white;''')

        self.btn = QPushButton('Add Data',self.widg)
        self.btn.setStyleSheet('''background-color:green;''')
        self.btn.clicked.connect(self.adddata_to_database)

        self.Vbox = QVBoxLayout(self.widg)
        self.Vbox.addWidget(self.line1)
        self.Vbox.addWidget(self.line2)
        self.Vbox.addWidget(self.line3)
        self.Vbox.addWidget(self.line4)
        self.Vbox.addWidget(self.line5)
        self.Vbox.addWidget(self.line6)
        self.Vbox.addWidget(self.btn)

        self.widg.setLayout(self.Vbox)

        self.widg.resize(400, 170)
        self.widg.show()


    def adddata_to_database(self):
        self.click_voice()

        #fetch data from lineEdits
        Enter_Name=self.line1.text()
        Enter_Job=self.line2.text()
        Enter_Section=self.line3.text()
        Enter_Phone=self.line4.text()
        Enter_Salary=self.line5.text()
        Enter_Address=self.line6.text()

        db = sqlite3.connect('database.db')
        cr = db.cursor()
        cr.execute('''INSERT INTO workers(name, job, section, phone, salary, address) VALUES(?,?,?,?,?,?)''',(Enter_Name, Enter_Job, Enter_Section, Enter_Phone, Enter_Salary, Enter_Address,))
        db.commit()
        db.close()
        self.fill_table()
        self.widg.close()

    def fill_table(self):
        db = sqlite3.connect('database.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM workers''')
        data = cr.fetchall()
        db.commit()
        db.close()

        self.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableWidget_3.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

    def close_btn(self):
        self.click_voice()
        sys.close()

    def min_btn(self):
        self.click_voice()
        self.showMinimized()

    def max_btn(self):
        self.click_voice()
        if self.n%2 == 0:
           self.showFullScreen()
        if self.n%2 != 0:
            self.showNormal()
        self.n += 1

    def show_menubar(self):
        self.click_voice()
        if self.pushButton_5.isChecked():
            self.menuBar.setVisible(True)
        else:
            self.menuBar.setVisible(False)

    def pin_btn(self):
        self.click_voice()
        if self.pushButton_4.isChecked():
            self.pushButton_4.setIcon(QIcon('images/pin_1.png'))
            self.setWindowFlags(self.windowFlags()|Qt.WindowStaysOnTopHint)
        else:
            self.pushButton_4.setIcon(QIcon('images/pin_2.png'))
            self.setWindowFlags(self.windowFlags()&~Qt.WindowStaysOnTopHint)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()