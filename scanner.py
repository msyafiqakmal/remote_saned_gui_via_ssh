
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import subprocess, yaml, os


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path+'/config.yaml') as file:
            defaultConn = yaml.load(file, Loader=yaml.FullLoader)

        #set home directory if value missing
        if defaultConn["default_save_location"] == "":
            home_dir = str(Path.home())+"/"
            defaultConn["default_save_location"] = home_dir
            with open(path+'/config.yaml', 'w') as f:
                yaml.safe_dump(defaultConn, f, default_flow_style=False)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.savelocation = QtWidgets.QLineEdit(self.centralwidget)
        self.savelocation.setEnabled(False)
        self.savelocation.setGeometry(QtCore.QRect(50, 240, 411, 25))
        self.savelocation.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.savelocation.setObjectName("savelocation")
        self.browsedialog = QtWidgets.QPushButton(self.centralwidget, clicked = self.dialogfind)
        self.browsedialog.setGeometry(QtCore.QRect(490, 240, 101, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.browsedialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.browsedialog.setFont(font)
        self.browsedialog.setMouseTracking(False)
        self.browsedialog.setObjectName("browsedialog")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.hostname = QtWidgets.QLineEdit(self.centralwidget)
        self.hostname.setEnabled(True)
        self.hostname.setGeometry(QtCore.QRect(50, 90, 351, 25))
        self.hostname.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.hostname.setObjectName("hostname")
        self.hostname.setText(defaultConn['default_hostname'])
        self.sshportnumber = QtWidgets.QLineEdit(self.centralwidget)
        self.sshportnumber.setEnabled(True)
        self.sshportnumber.setGeometry(QtCore.QRect(430, 90, 161, 25))
        self.sshportnumber.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.sshportnumber.setObjectName("sshportnumber")
        self.sshportnumber.setText(defaultConn['default_port'])
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scanbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.triggerscanjob(self.hostname.text(),self.sshportnumber.text(),defaultConn["default_username"],self.savelocation.text()))
        self.scanbutton.setGeometry(QtCore.QRect(260, 330, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.scanbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.scanbutton.setFont(font)
        self.scanbutton.setMouseTracking(False)
        icon = QtGui.QIcon.fromTheme("scanner")
        self.scanbutton.setIcon(icon)
        self.scanbutton.setObjectName("scanbutton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(50, 290, 291, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.printerstatus = QtWidgets.QLabel(self.centralwidget)
        self.printerstatus.setGeometry(QtCore.QRect(50, 160, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.printerstatus.setFont(font)
        self.printerstatus.setObjectName("printerstatus")


        # self.browsedialog = QtWidgets.QPushButton(self.centralwidget, clicked = self.dialogfind)

        self.manualcheckprinter = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.getprinterstatus(self.hostname.text(),self.sshportnumber.text(),defaultConn["default_username"]))
        self.manualcheckprinter.setGeometry(QtCore.QRect(430, 160, 71, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.manualcheckprinter.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.manualcheckprinter.setFont(font)
        self.manualcheckprinter.setMouseTracking(False)
        self.manualcheckprinter.setObjectName("manualcheckprinter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.retranslateUi(MainWindow)

        if((defaultConn["default_hostname"] != "") and (defaultConn["default_port"] != "")) :
            self.getprinterstatus(defaultConn['default_hostname'],defaultConn['default_port'],defaultConn['default_username']) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browsedialog.setText(_translate("MainWindow", "Browse ..."))
        self.label.setText(_translate("MainWindow", "Scan via remote scanner"))
        self.label_2.setText(_translate("MainWindow", "Save Location / Filename"))
        self.label_3.setText(_translate("MainWindow", "Server Hostname/ IP Address"))
        self.label_4.setText(_translate("MainWindow", "SSH Port"))
        self.scanbutton.setText(_translate("MainWindow", " Scan Now"))
        self.checkBox.setText(_translate("MainWindow", "I would like to save current configuration"))
        self.label_5.setText(_translate("MainWindow", "Available Scanner"))
        # self.printerstatus.setText(_translate("MainWindow", " "))
        self.manualcheckprinter.setText(_translate("MainWindow", "recheck"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def dialogfind(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path+'/config.yaml') as file:
            defaultConn = yaml.load(file, Loader=yaml.FullLoader)

        self.dialog = QtWidgets.QFileDialog()
        foo_dir = self.dialog.getSaveFileName(self.dialog, 'Open file', 
        defaultConn["default_save_location"],"Image files (*.png *.jpeg *.tiff)")
        print(str(foo_dir[0]))
        self.savelocation.setText('{0}'.format(foo_dir[0]))

    def getprinterstatus(self,serverhostname,serverport,serverusername):
        result = subprocess.run('ssh -p '+serverport+' '+serverusername+'@'+serverhostname+' scanimage -L',shell=True, stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        self.printerstatus.setText(output)
    
    def triggerscanjob(self,serverhostname,serverport,serverusername,savedir):
        self.label.setText("⏳ Printing is underway, Please Wait")
        self.label.show()
        self.label.repaint()
        
        if self.checkBox.isChecked():
            path = os.path.dirname(os.path.abspath(__file__))
            with open(path+'/config.yaml') as file:
                defaultConn = yaml.load(file, Loader=yaml.FullLoader)

            defaultConn["default_hostname"] = serverhostname
            defaultConn["default_port"] = serverport
            defaultConn["default_save_location"] = savedir
            
            with open(path+'/config.yaml', 'w') as f:
                yaml.safe_dump(defaultConn, f, default_flow_style=False)

        if((serverhostname != "") and (serverport != "") and(savedir != "") ):
            process = subprocess.Popen("ssh -p "+serverport+" "+serverusername+"@"+serverhostname+" scanimage >\'"+savedir+"\' --format jpeg -p", shell=True, stdout=subprocess.PIPE)
            process.wait()
            self.label.setText("⌛Printing Completed")
        else:
            self.label.setText("Please ensure all parameters are filled")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

