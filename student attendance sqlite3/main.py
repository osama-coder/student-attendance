# import Important modules
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.uic import loadUiType
from os import path
import pandas as pd
import sys,sqlite3

# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname('untitled.ui'),'untitled.ui'))
class mainApp(QWidget, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.ui_changes()
        self.controllers()
        self.fill_table_7()
        self.fill_table_6()
        self.fill_table_8()

    def ui_changes(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.frame_5.hide()
        self.tableWidget_7.resizeColumnsToContents()
        self.tableWidget_6.resizeColumnsToContents()
        self.tableWidget_8.verticalHeader().setFixedWidth(20)
        header = self.tableWidget_7.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        ## intial values

    def controllers(self):
        #### title left buttons actions
        self.pushButton.clicked.connect(self.pin_btn)
        self.pushButton_2.clicked.connect(self.min_btn)
        self.pushButton_3.clicked.connect(self.max_btn)
        self.pushButton_4.clicked.connect(self.close_btn)
        ### sideMenu animation
        self.pushButton_5.clicked.connect(self.doAnimation)
        ### sideMenu actions
        self.pushButton_13.clicked.connect(self.btn0)
        self.pushButton_7.clicked.connect(self.btn1)
        self.pushButton_6.clicked.connect(self.btn2)
        self.pushButton_8.clicked.connect(self.btn4)
        self.pushButton_12.clicked.connect(self.btn5)

        ##login signal button
        self.pushButton_18.clicked.connect(self.loginteacher)
        self.pushButton_9.clicked.connect(self.createaccount)
        self.pushButton_19.clicked.connect(self.loginstudent)

        ##All student page
        self.pushButton_25.clicked.connect(self.addtodatabasefun)
        self.pushButton_26.clicked.connect(self.delete)
        self.lineEdit_9.textChanged.connect(self.check_text)
        self.pushButton_33.clicked.connect(self.updatedatabasefun)
        self.pushButton_27.clicked.connect(self.Export_to_Excel)

        ##todayAttendance
        self.pushButton_22.clicked.connect(self.addtodatabasefuna)
        self.pushButton_34.clicked.connect(self.updatedatabasefuna)
        self.pushButton_24.clicked.connect(self.delete_6)
        self.pushButton_23.clicked.connect(self.Export_to_Excel2)

        ##Weeklyclasses
        self.pushButton_28.clicked.connect(self.addtodatabasefunb)
        self.pushButton_29.clicked.connect(self.updatedatabasefunb)
        self.pushButton_30.clicked.connect(self.delete_8)

        ##
        self.pushButton_31.clicked.connect(self.Export_to_Excel3)

    def click_voice(self):
        # produce sound when click
        url = QtCore.QUrl.fromLocalFile(r"voices\click-voice.wav")
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer(self)  # its is important to put self inside, does not work without
        player.setMedia(content)
        player.setVolume(100)
        player.play()

################################################################################################################
###title_buttons actions
    def close_btn(self):
        self.click_voice()
        sys.close()

    def min_btn(self):
        self.click_voice()
        self.showMinimized()

    def max_btn(self):
        self.click_voice()
        if self.pushButton_3.isChecked():
           self.showFullScreen()
           self.frame_5.setMaximumHeight(574)     ### good_trick
        else:
            self.showNormal()

    def pin_btn(self):
        self.click_voice()
        if self.pushButton.isChecked():
            self.pushButton.setIcon(QIcon(r'images\2.jpg'))
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.pushButton.setIcon(QIcon(r'images\1.png'))
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()

##################################################################################################################
##########################################All students data details###############
##################################################################################################################
    def add_classes(self):
        self.click_voice()
        self.widg = QWidget()
        self.widg.setStyleSheet('''background-color:rgb(73, 69, 200);''')

        self.line1 = QLineEdit(self.widg)
        self.line1.setPlaceholderText('Enter Full name')
        self.line1.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line2 = QLineEdit(self.widg)
        self.line2.setPlaceholderText('Enter Birth day')
        self.line2.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line3 = QLineEdit(self.widg)
        self.line3.setPlaceholderText('Enter Phone')
        self.line3.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line4 = QLineEdit(self.widg)
        self.line4.setPlaceholderText('Enter Email')
        self.line4.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line5 = QLineEdit(self.widg)
        self.line5.setPlaceholderText('Enter Payment')
        self.line5.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line6 = QLineEdit(self.widg)
        self.line6.setPlaceholderText('Enter register date')
        self.line6.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line7 = QLineEdit(self.widg)
        self.line7.setPlaceholderText('Enter Level')
        self.line7.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.btn1 = QPushButton('Add Data',self.widg)
        self.btn1.setStyleSheet('''background-color:green;''')
        self.btn1.clicked.connect(self.adddata_to_database)

        self.btn2 = QPushButton('Update Data', self.widg)
        self.btn2.setStyleSheet('''background-color:green;''')
        self.btn2.clicked.connect(self.updatedatabase)

        self.Vbox = QVBoxLayout(self.widg)
        self.Vbox.addWidget(self.line1)
        self.Vbox.addWidget(self.line2)
        self.Vbox.addWidget(self.line3)
        self.Vbox.addWidget(self.line4)
        self.Vbox.addWidget(self.line5)
        self.Vbox.addWidget(self.line6)
        self.Vbox.addWidget(self.line7)
        self.Vbox.addWidget(self.btn1)
        self.Vbox.addWidget(self.btn2)
        self.Vbox.setSpacing(3)

        self.widg.setLayout(self.Vbox)
        self.widg.resize(500, 300)
        self.widg.show()

    def addtodatabasefun(self):
        self.add_classes()
        self.btn2.setVisible(False)

    def updatedatabasefun(self):
        self.add_classes()
        self.btn1.setVisible(False)

        item = self.tableWidget_7.currentItem().text()
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM students WHERE Full_name=?''', (item,))
        data= cr.fetchall()
        db.commit()
        db.close()

        self.line1.setText(data[0][0])
        self.line2.setText(data[0][1])
        self.line3.setText(data[0][2])
        self.line4.setText(data[0][3])
        self.line5.setText(data[0][4])
        self.line6.setText(data[0][5])
        self.line7.setText(data[0][6])

    def updatedatabase(self):
        try:
            level = self.line1.text()
            subject = self.line2.text()
            teacher = self.line3.text()
            day = self.line4.text()
            date = self.line5.text()
            long = self.line6.text()
            from_time = self.line7.text()

            item = self.tableWidget_7.currentItem().text()
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute(
                '''UPDATE students SET Full_name='{}',Birth_date='{}',Phone='{}',Email='{}',Payment='{}',Register_date='{}',Level='{}'  WHERE Full_name LIKE'%{}%' '''.format(
                    level, subject, teacher, day, date, long, from_time,item))
            db.commit()
            db.close()
            self.fill_table_7()
            self.widg.close()

        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from tabk')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def adddata_to_database(self):
        self.click_voice()
        ### get data from linesEdits
        level = self.line1.text()
        subject = self.line2.text()
        teacher = self.line3.text()
        day = self.line4.text()
        date = self.line5.text()
        long = self.line6.text()
        from_time = self.line7.text()

        ### connecting to database and insert
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''INSERT INTO students VALUES('{}','{}','{}','{}','{}','{}','{}')'''
                   .format(level,subject,teacher,day,date,long,from_time))
        db.commit()
        db.close()

        ###insert int tablewidget
        self.fill_table_7()

        ### clear line edits after data dentry process
        self.line1.setText('')
        self.line2.setText('')
        self.line3.setText('')
        self.line4.setText('')
        self.line5.setText('')
        self.line6.setText('')
        self.line7.setText('')

    def fill_table_7(self):
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM students''')
        data = cr.fetchall()
        db.commit()
        db.close()

        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableWidget_7.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

    def delete(self):
        self.click_voice()
        try:
            item = self.tableWidget_7.currentItem().text()
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''DELETE FROM students WHERE Full_name=?''', (item,))
            db.commit()
            db.close()
            self.fill_table_7()
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from tabk')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def check_text(self):
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM students WHERE Full_name LIKE '{}%' '''.format(self.lineEdit_9.text()))
        data = cr.fetchall()
        db.commit()
        db.close()

        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableWidget_7.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

##################################################################################################################
##########################################Today attendance###############
##################################################################################################################
    def add_student_attendance(self):
        self.click_voice()
        self.widga = QWidget()
        # self.widga.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.widga.setStyleSheet('''background-color:rgb(73, 69, 200);''')

        self.line1a = QLineEdit(self.widga)
        self.line1a.setPlaceholderText('Enter full name')
        self.line1a.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line2a = QLineEdit(self.widga)
        self.line2a.setPlaceholderText('Level')
        self.line2a.setPlaceholderText('Enter Level')
        self.line2a.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line3a = QLineEdit(self.widga)
        self.line3a.setPlaceholderText('Class')
        self.line3a.setPlaceholderText('Enter class')
        self.line3a.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.btn1a = QPushButton('Add Data', self.widga)
        self.btn1a.setStyleSheet('''background-color:green;''')
        self.btn1a.clicked.connect(self.adddata_to_databasea)

        self.btn2a = QPushButton('Update Data', self.widga)
        self.btn2a.setStyleSheet('''background-color:green;''')
        self.btn2a.clicked.connect(self.updatedatabasea)

        self.Vboxa = QVBoxLayout(self.widga)
        self.Vboxa.addWidget(self.line1a)
        self.Vboxa.addWidget(self.line2a)
        self.Vboxa.addWidget(self.line3a)
        self.Vboxa.addWidget(self.btn1a)
        self.Vboxa.addWidget(self.btn2a)

        self.Vboxa.setSpacing(3)
        self.widga.setLayout(self.Vboxa)
        self.widga.resize(500, 300)
        self.widga.show()

    def addtodatabasefuna(self):
        self.add_student_attendance()
        self.btn2a.setVisible(False)

    def updatedatabasefuna(self):
        self.add_student_attendance()
        self.btn1a.setVisible(False)

        self.iteming = self.tableWidget_6.currentItem().text()
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM attendance WHERE Full_name=?''', (self.iteming,))
        data = cr.fetchall()
        db.commit()
        db.close()

        self.line1a.setText(data[0][0])
        self.line2a.setText(data[0][1])
        self.line3a.setText(data[0][2])

    def updatedatabasea(self):
        try:
            name = self.line1a.text()
            level = self.line2a.text()
            classes = self.line3a.text()

            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute(
                '''UPDATE attendance SET Full_name='{}',Level='{}',Class='{}' WHERE Full_name='{}' '''
                    .format(name, level, classes, self.iteming))
            db.commit()
            db.close()
            self.widga.close()
            self.fill_table_6()
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from table')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def adddata_to_databasea(self):
        self.click_voice()
        ### get data from linesEdits
        name = self.line1a.text()
        level = self.line2a.text()
        classes = self.line3a.text()

        ### connecting to database and insert
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''INSERT INTO attendance VALUES('{}','{}','{}')'''.format(name, level, classes))
        db.commit()
        db.close()

        ###insert int tablewidget
        self.fill_table_6()

        ### clear line edits after data dentry process
        self.line1a.setText('')
    def delete_6(self):
        self.click_voice()
        try:
            item = self.tableWidget_6.currentItem().text()
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''DELETE FROM attendance WHERE Full_name=?''', (item,))
            db.commit()
            db.close()
            self.fill_table_6()
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from tabk')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
    def fill_table_6(self):
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM attendance''')
        data = cr.fetchall()
        db.commit()
        db.close()
        self.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableWidget_6.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

##################################################################################################################
##########################################Table Teachers weekly classes###############
##################################################################################################################
    def add_studentb(self):
        self.click_voice()
        self.widgb = QWidget()
        # self.widg.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.widgb.setStyleSheet('''background-color:rgb(73, 69, 200);''')

        self.line1b = QLineEdit(self.widgb)
        self.line1b.setPlaceholderText('Enter Level')
        self.line1b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line2b = QLineEdit(self.widgb)
        self.line2b.setPlaceholderText('Enter Subject name')
        self.line2b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line3b = QLineEdit(self.widgb)
        self.line3b.setPlaceholderText('Enter Teacher name')
        self.line3b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line4b = QLineEdit(self.widgb)
        self.line4b.setPlaceholderText('Enter Day name')
        self.line4b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line5b = QLineEdit(self.widgb)
        self.line5b.setPlaceholderText('Enter Day date')
        self.line5b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line6b = QLineEdit(self.widgb)
        self.line6b.setPlaceholderText('Enter Long')
        self.line6b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line7b = QLineEdit(self.widgb)
        self.line7b.setPlaceholderText('Enter From')
        self.line7b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line8b = QLineEdit(self.widgb)
        self.line8b.setPlaceholderText('Enter To')
        self.line8b.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.btn1b = QPushButton('Add Data', self.widgb)
        self.btn1b.setStyleSheet('''background-color:green;''')
        self.btn1b.clicked.connect(self.adddata_to_databaseb)

        self.btn2b = QPushButton('Update Data', self.widgb)
        self.btn2b.setStyleSheet('''background-color:green;''')
        self.btn2b.clicked.connect(self.updatedatabaseb)

        self.Vboxb = QVBoxLayout(self.widgb)
        self.Vboxb.addWidget(self.line1b)
        self.Vboxb.addWidget(self.line2b)
        self.Vboxb.addWidget(self.line3b)
        self.Vboxb.addWidget(self.line4b)
        self.Vboxb.addWidget(self.line5b)
        self.Vboxb.addWidget(self.line6b)
        self.Vboxb.addWidget(self.line7b)
        self.Vboxb.addWidget(self.line8b)
        self.Vboxb.addWidget(self.btn1b)
        self.Vboxb.addWidget(self.btn2b)
        self.Vboxb.setSpacing(3)

        self.widgb.setLayout(self.Vboxb)
        self.widgb.resize(500, 300)
        self.widgb.show()

    def addtodatabasefunb(self):
        self.add_studentb()
        self.btn2b.setVisible(False)

    def updatedatabasefunb(self):
        self.add_studentb()
        self.btn1b.setVisible(False)

        item = self.tableWidget_8.currentItem().text()
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM WeeklyTable WHERE id=?''',(item,))
        data = cr.fetchall()
        db.commit()
        db.close()
        self.line1b.setText(data[0][1])
        self.line2b.setText(data[0][2])
        self.line3b.setText(data[0][3])
        self.line4b.setText(data[0][4])
        self.line5b.setText(data[0][5])
        self.line6b.setText(data[0][6])
        self.line7b.setText(data[0][7])
        self.line8b.setText(data[0][8])

    def updatedatabaseb(self):
        self.click_voice()
        level = self.line1b.text()
        subject = self.line2b.text()
        teacher = self.line3b.text()
        day = self.line4b.text()
        date = self.line5b.text()
        long = self.line6b.text()
        from_1 = self.line7b.text()
        to_1 = self.line8b.text()
        try:
            item = self.tableWidget_8.currentItem().text()
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''UPDATE WeeklyTable SET Subject_name=?,Teacher_name=?,Day=?,Date=?,Long=?,From_1=?,To_1=?,Level=?  WHERE id=?''',(
            subject,teacher,day,date,long,from_1,to_1,level,item,))
            db.commit()
            db.close()
            self.fill_table_8()
            self.widgb.close()

        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from tabk')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

    def adddata_to_databaseb(self):
        self.click_voice()
        level = self.line1b.text()
        subject = self.line2b.text()
        teacher = self.line3b.text()
        day = self.line4b.text()
        date = self.line5b.text()
        long = self.line6b.text()
        from_1 = self.line7b.text()
        to_1 = self.line8b.text()

        ### connecting to database and insert
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''INSERT INTO WeeklyTable(Level,Subject_name,Teacher_name,Day,Date,Long,From_1,To_1) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(level, subject, teacher, day, date, long,from_1,to_1))
        db.commit()
        db.close()

        ###insert int tablewidget
        self.fill_table_8()

        ### clear line edits after data dentry process
        self.line1b.setText('')
        self.line2b.setText('')
        self.line3b.setText('')
        self.line4b.setText('')
        self.line5b.setText('')
        self.line6b.setText('')
        self.line7b.setText('')
        self.line8b.setText('')
    def delete_8(self):
        self.click_voice()
        try:
            item = int(self.tableWidget_8.currentItem().text())
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''DELETE FROM WeeklyTable WHERE id=?''',(item,))
            db.commit()
            db.close()
            self.fill_table_8()
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Information')
            msg.setInformativeText('Choose Row from tabk')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
    def fill_table_8(self):
        db = sqlite3.connect('realdatabase.db')
        cr = db.cursor()
        cr.execute('''SELECT * FROM WeeklyTable''')
        data = cr.fetchall()
        db.commit()
        db.close()
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableWidget_8.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
##################################################################################################################
##########################################Student Dashboard###############
##################################################################################################################

###################################################################################
    def loginteacher(self):
        self.click_voice()
        ##fetch lineEdits data
        user_name = self.lineEdit.text()
        user_password = self.lineEdit_5.text()

        try:
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''SELECT * FROM teachers WHERE name=? AND password=?''',(user_name, user_password,))
            data = cr.fetchall()
            db.commit()
            db.close()
            if data[0][0]==user_name and data[0][1]==user_password:
                self.stackedWidget.setCurrentIndex(1)
                self.frame_5.show()
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Authentification')
            msg.setInformativeText('the password or name is wrong')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()

        self.lineEdit.setText('')
        self.lineEdit_5.setText('')

    def loginstudent(self):
        self.click_voice()
        ##fetch lineEdits data
        user_name = self.lineEdit_4.text()
        user_password = self.lineEdit_7.text()

        try:
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''SELECT * FROM staccounts WHERE name='{}' AND password='{}' '''.format(user_name,user_password))
            data = cr.fetchall()
            db.commit()
            db.close()
            if data[0][0]==user_name and data[0][1]==user_password:
                self.stackedWidget.setCurrentIndex(4)
                self.frame_5.show()
                self.label_9.setText(data[0][2])

                self.pushButton_8.setChecked(True)
                self.pushButton_13.setChecked(False)

                self.pushButton_13.setEnabled(False)
                self.pushButton_7.setEnabled(False)
                self.pushButton_12.setEnabled(False)
                self.pushButton_6.setEnabled(False)

                self.pushButton_28.setVisible(False)
                self.pushButton_29.setVisible(False)
                self.pushButton_30.setVisible(False)
        except:
            msg = QMessageBox(self)
            msg.setWindowTitle('Authentification')
            msg.setInformativeText('the password or name is wrong')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            self.lineEdit_4.setText('')
            self.lineEdit_7.setText('')

    def createaccount(self):
        self.click_voice()
        self.widg1 = QWidget()
        self.widg1.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.widg1.setStyleSheet('''background-color:rgb(73, 69, 200);''')

        self.line100 = QLineEdit(self.widg1)
        self.line100.setPlaceholderText('Enter Username')
        self.line100.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line101 = QLineEdit(self.widg1)
        self.line101.setPlaceholderText('Enter Password')
        self.line101.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.line102 = QLineEdit(self.widg1)
        self.line102.setPlaceholderText('Enter Password Again')
        self.line102.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.combo = QComboBox(self.widg1)
        self.fill_level_combo()
        self.combo.setItemText(0,'Enter Choose you level')
        self.combo.setStyleSheet('''QLineEdit{background-color:white;}''')

        self.btn100 = QPushButton('Add Data',self.widg1)
        self.btn100.setStyleSheet('''background-color:green;''')
        self.btn100.clicked.connect(self.signup)

        self.Vbox1 = QVBoxLayout(self.widg1)
        self.Vbox1.addWidget(self.line100)
        self.Vbox1.addWidget(self.line101)
        self.Vbox1.addWidget(self.line102)
        self.Vbox1.addWidget(self.combo)

        self.Vbox1.addWidget(self.btn100)
        self.Vbox1.setSpacing(3)

        self.widg1.setLayout(self.Vbox1)
        self.widg1.resize(400, 200)
        self.widg1.show()

    def signup(self):
        self.click_voice()
        ##fetch lineEdits data
        user_name = self.line100.text()
        user_password = self.line101.text()
        password_again = self.line102.text()
        level_n = self.combo.currentText()
        ##check password and save in database
        if user_password == password_again:
            db = sqlite3.connect('realdatabase.db')
            cr = db.cursor()
            cr.execute('''INSERT INTO staccounts(name, password,level) VALUES('{}','{}','{}')'''.format(user_name, user_password,level_n))
            db.commit()
            db.close()
            self.widg1.close()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle('Authentification')
            msg.setInformativeText('the two password does not match')
            msg.setIcon(QMessageBox.Information)
            msg.exec()

        self.line100.setText('')
        self.line101.setText('')
        self.line102.setText('')

######################################################################################################
####sideMenu_buttons actions
    def btn0(self):
        self.click_voice()
        self.stackedWidget.setCurrentIndex(1)
        if self.pushButton_13.isChecked():
            self.pushButton_7.setChecked(False)
            self.pushButton_6.setChecked(False)
            self.pushButton_8.setChecked(False)
            self.pushButton_12.setChecked(False)

    def btn1(self):
        self.click_voice()
        self.stackedWidget.setCurrentIndex(2)
        if self.pushButton_7.isChecked():
            self.pushButton_13.setChecked(False)
            self.pushButton_6.setChecked(False)
            self.pushButton_8.setChecked(False)
            self.pushButton_12.setChecked(False)

    def btn2(self):
        self.click_voice()
        self.stackedWidget.setCurrentIndex(3)
        if self.pushButton_6.isChecked():
            self.pushButton_13.setChecked(False)
            self.pushButton_7.setChecked(False)
            self.pushButton_8.setChecked(False)
            self.pushButton_12.setChecked(False)

    def btn4(self):
        self.click_voice()
        self.stackedWidget.setCurrentIndex(4)
        if self.pushButton_8.isChecked():
            self.pushButton_13.setChecked(False)
            self.pushButton_7.setChecked(False)
            self.pushButton_6.setChecked(False)
            self.pushButton_12.setChecked(False)

    def btn5(self):
        self.click_voice()
        self.stackedWidget.setCurrentIndex(5)
        if self.pushButton_12.isChecked():
            self.pushButton_13.setChecked(False)
            self.pushButton_7.setChecked(False)
            self.pushButton_6.setChecked(False)
            self.pushButton_8.setChecked(False)

######################################################################################################
#### move_window
    def mousePressEvent(self, QMouseEvent):
        self.old_position = QMouseEvent.globalPos()

    def mouseMoveEvent(self, QMouseEvent):
        self.new_position = QMouseEvent.globalPos()
        delta = self.new_position - self.old_position
        self.move(self.x()+delta.x(), self.y()+delta.y())
        self.old_position = self.new_position

######################################################################################################
#### animate_sideMenu
    def doAnimation(self):
        self.click_voice()
        if self.pushButton_5.isChecked():
            self.animate = QPropertyAnimation(self.frame_5,b'maximumWidth')
            self.animate.setDuration(5000)
            self.animate.setStartValue(50)
            self.animate.setEndValue(225)
            self.animate.start()

            self.pushButton_5.setText('Dashboard            ')
            self.pushButton_13.setText('All student         ')
            self.pushButton_7.setText('Today Attendance   ')
            self.pushButton_6.setText('Weekly classes     ')
            self.pushButton_8.setText('Student Dashboard   ')
            self.pushButton_12.setText('Settings             ')

        else:
            self.animate = QPropertyAnimation(self.frame_5, b'maximumWidth')
            self.animate.setDuration(5000)
            self.animate.setStartValue(225)
            self.animate.setEndValue(50)
            self.animate.start()

            self.pushButton_5.setText('')
            self.pushButton_13.setText('')
            self.pushButton_7.setText('')
            self.pushButton_6.setText('')
            self.pushButton_8.setText('')
            self.pushButton_12.setText('')
######################################################################################################
####export to excel
    def Export_to_Excel(self):
        columnHeaders = []
        ##### create column header list in excel file
        for j in range(self.tableWidget_7.model().columnCount()):
            columnHeaders.append(self.tableWidget_7.horizontalHeaderItem(j).text())
        df = pd.DataFrame(columns=columnHeaders)
        ##### create dataframe object recordset
        for row in range(self.tableWidget_7.rowCount()):
            for col in range(self.tableWidget_7.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget_7.item(row, col).text()
        df.to_excel(r'Excel files\All student data details.xlsx', index=False)

    def Export_to_Excel2(self):
        columnHeaders = []
        ##### create column header list in excel file
        for j in range(self.tableWidget_6.model().columnCount()):
            columnHeaders.append(self.tableWidget_6.horizontalHeaderItem(j).text())
        df = pd.DataFrame(columns=columnHeaders)
        ##### create dataframe object recordset
        for row in range(self.tableWidget_6.rowCount()):
            for col in range(self.tableWidget_6.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget_6.item(row, col).text()
        df.to_excel(r'Excel files\Today Attendance.xlsx', index=False)

    def Export_to_Excel3(self):
        columnHeaders = []
        ##### create column header list in excel file
        for j in range(self.tableWidget_9.model().columnCount()):
            columnHeaders.append(self.tableWidget_9.horizontalHeaderItem(j).text())
        df = pd.DataFrame(columns=columnHeaders)
        ##### create dataframe object recordset
        for row in range(self.tableWidget_9.rowCount()):
            for col in range(self.tableWidget_9.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget_9.item(row, col).text()
        df.to_excel(r'Excel files\My classes table.xlsx', index=False)

    # fill combo with available classses
    def fill_level_combo(self):
        row_number = self.tableWidget_7.rowCount()
        data = []
        for row in range(row_number):
            items = self.tableWidget_7.item(row, 6)
            data.append(items.text())
        mylist = sorted(set(data))
        self.combo.addItems(mylist)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()