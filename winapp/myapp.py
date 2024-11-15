import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QApplication,QDialog, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout, QMessageBox,QTextEdit, QGridLayout
import sqlite3
import mysql.connector
from mysql.connector import Error
from datetime import datetime



# Admin Panel Feature #1 : Create User Dialog box
class create_user_dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create User")
        # setGeometry(left, top, width, height) 
        self.setGeometry(450, 350, 300, 150) 
        #self.move(380,170)
        #self.move(200,350)
        bold_font = QFont("Arial",10,QFont.Weight.Bold)
        layout = QVBoxLayout()
        
        self.label_username = QLabel('Username')
        #label_username.move(175,200)
        self.label_username.setFont(bold_font)
        self.label_username.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_username)


        self.input_username = QLineEdit()
        layout.addWidget(self.input_username)

        self.label_password = QLabel('Password')
        self.label_password.setFont(bold_font)
        self.label_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_password)

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password)

        button_layout = QHBoxLayout()

        self.button_create = QPushButton('Create')
        self.button_create.clicked.connect(self.create_user_dialog_button)
        #self.button_create.clicked.connect(self.reject)

        button_layout.addWidget(self.button_create)

        self.button_cancel = QPushButton('Cancel')
        self.button_cancel.clicked.connect(self.reject)
        #self.button_cancel.clicked.connect(self.create_user_dialog_button)
        button_layout.addWidget(self.button_cancel)


        layout.addLayout(button_layout)        
        self.setLayout(layout)



        '''
        QBtn = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("check")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    '''

    def create_user_dialog_button(self):

        username = self.input_username.text()
        password = self.input_password.text()

        if username and password:
            print(f'{username},{password}')
            self.accept()

        else: 
            print("please fill both fields")



class UserWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Panel")
        # setGeometry(left, top, width, height) 
        self.setGeometry(0, 0, 500, 200) 
        bold_font = QFont("Arial",12,QFont.Weight.Bold)

        layout = QVBoxLayout()

        self.label = QLabel('Welcome To The User Panel',self)
        self.label.setFont(bold_font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        #self.label.setAlignment

        self.setLayout(layout)

class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Panel")
        # setGeometry(left, top, width, height) 
        #self.setGeometry(100, 200, 500, 200) 
        self.move(0,0)
        #self.resize(500,200)
        self.setFixedWidth(600)
        self.setFixedHeight(700)

        bold_font = QFont("Arial",12,QFont.Weight.Bold)

        self.AdminUiComponents()

        #self.show()

    def AdminUiComponents(self):

        bold_font = QFont("Arial",12,QFont.Weight.Bold)

        #layout = QVBoxLayout()
        label = QLabel('Welcome To The Admin Panel',self)
        label.setFont(bold_font)
        # setGeometry(left, top, width, height)
        label.move(180,10)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(self.label)

        login_button = QPushButton('Create User',self)
        login_button.setFont(bold_font)
        # setGeometry(left, top, width, height)
        login_button.setGeometry(220,50,10,20)
        login_button.resize(150,50)

        login_button.clicked.connect(self.create_user_button)

    def on_click(self):
        self.hide()
        self.admin_window = AdminWindow()
        self.admin_window.show()
        print("Button is Clicked")

    def create_user_button(self):
        self.custom_dialog = create_user_dialog()
        self.custom_dialog.show()

        #layout.addWidget(layout.login_button)
        #self.label.setAlignment
        #self.setLayout(layout)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        #self.setWindowIcon()
        #self.move(0,0)
        #self.resize(500,200)
        self.setFixedWidth(600)
        self.setFixedHeight(700)
        
        #self.setGeometry(10, 10, 500, 200) # setGeometry(left, top, width, height)
        #bold_font = QFont("Ubuntu Regular",20,QFont.Weight.Bold)

        #self.LoginFormUiComponents()

    #def LoginFormUiComponents(self):

        #layout = QVBoxLayout()
        bold_font = QFont("Roboto",30,QFont.Weight.Bold)
        label_username = QLabel('USERNAME',self)
        label_username.move(175,200)
        label_username.setFont(bold_font)
        label_username.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(self.label_username)

        image_label = QLabel(self)
        pixmap = (QPixmap('plane_guidance.png'))
        image_label.setPixmap(pixmap)
        image_label.setGeometry(30,0,450,180)
        #image_label.move(0,0)
        #self.setCentralWidget(image_label)
        #self.resize(pixmap.width(),pixmap.height())

        self.input_username = QLineEdit(self)
        # setGeometry(left, top, width, height)
        self.input_username.setGeometry(100,280,400,60)
        #input_username.move(170,150)
        #layout.addWidget(self.input_username)

        label_password = QLabel('PASSWORD',self)
        label_password.move(175,360)
        label_password.setFont(bold_font)
        label_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(self.label_password)


        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setGeometry(100,430,400,60)
        #layout.addWidget(self.input_password)

        login_button = QPushButton('LOGIN',self)
        login_button.setFont(bold_font)
        login_button.setGeometry(100,550,400,72)
        login_button.setStyleSheet("background-color: green")
        #self.login_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        login_button.clicked.connect(self.open_user_window)
        #layout.addWidget(self.login_button)


        #self.setLayout(layout)



    def on_click(self):
        print("Button is Clicked")

    def open_user_window(self):

        # Connect with Database

        conn = sqlite3.connect('Event_log.db')
        cur = conn.cursor()

        username = self.input_username.text()
        password = self.input_password.text()



        if username == "admin" and password == "admin":
            self.hide()
            self.admin_window = AdminWindow()
            self.admin_window.show()
            self.trigger_activity("admin_login")
        
        else:
            cur.execute("SELECT * FROM user_login_info WHERE username = ? AND password = ?",(username,password))
            result = cur.fetchone()
            conn.close()

            if result:
                self.hide()
                self.UserWindow = UserWindow()
                self.UserWindow.show()
                self.trigger_activity(f"user_login: {username}")

            else:
                QMessageBox.warning(self,'Error:','Invalid Username and Password')
                self.hide()
                window = LoginForm()
                window.show() 


    def AdminUiComponents(self):

        bold_font = QFont("Arial",12,QFont.Weight.Bold)

        #layout = QVBoxLayout()
        label = QLabel('Welcome To The Admin Panel',self)
        label.setFont(bold_font)
        # setGeometry(left, top, width, height)
        label.move(150,10)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(self.label)

        login_button = QPushButton('Create User',self)
        login_button.setFont(bold_font)
        # setGeometry(left, top, width, height)
        login_button.setGeometry(170,50,10,20)
        login_button.resize(150,50)

        login_button.clicked.connect(self.create_user_button)

    def on_click(self):
        self.hide()
        self.admin_window = AdminWindow()
        self.admin_window.show()
        print("Button is Clicked")

    def create_user_button(self):
        self.custom_dialog = create_user_dialog()
        self.custom_dialog.show()



        '''
        self.hide()
        self.user_window = UserWindow()
        self.user_window.show()
        
        '''

#sql work
################################################################
##################################################################
####################################################################



conn = sqlite3.connect('Event_log.db')
cur = conn.cursor()

#id INTEGER PRIMARY KEY AUTOINCREMENT,

cur.execute('''CREATE TABLE IF NOT  EXISTS user_activity (
	date TEXT NOT NULL,
	time TEXT NOT NULL,
	action TEXT NOT NULL)''')

cur.execute('''CREATE TABLE IF NOT  EXISTS user_login_info (
	username TEXT PRIMARY KEY,
	password TEXT NOT NULL)''')


def trigger_activity(triggered_action):

	current_date = datetime.now().strftime('%Y-%m-%d')
	current_time = datetime.now().strftime('%H:%M:%S')
	user_action = triggered_action


	cur.execute('''INSERT INTO user_activity (date,time,action) VALUES (?,?,?)''',
		(current_date,current_time,user_action))

	#print("Action Logged")

	conn.commit()
	conn.close()

def create_user(username,password):
	cur.execute('''INSERT INTO user_login_info (username,password) VALUES (?,?)''',
	(username,password))

	print("User Added")

	conn.commit()
	conn.close()






#trigger_activity("admin_login")


'''
table = """ CREATE TABLE Events (
			Event_Date DATE NOT NULL,
			Event_Time TIME NOT NULL,
			Event_Action CHAR(25)
		); """

cursor_obj.execute(table)

'''

##########################################################################################
#################################################################################
###############################################################################################


#main fuction calling 
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #window= AdminWindow()
    window = LoginForm()
    #create_user_dialog = create_user_dialog()
    #create_user_dialog.move(380,190)
    window.move(380,170)
    window.show() 

    sys.exit(app.exec())
