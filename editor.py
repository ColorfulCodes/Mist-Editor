import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        # width and height
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Mist")

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

def initToolbar(self):
    self.toolbar = self.addToolBar("options")
    # This makes the next toolbar appear underneath the one above
    self.addToolBarBreak

def initFormatbar(self):
    self.formatbar = self.addToolBar("Format")

def initMenubar(self):
    menubar = self.menubar()
    file = menubar.addMenu("File")
    edit = menubar.addMenu("Edit")
    view = menubar.addMenu("View")

def initUI(self):
    self.text = QtGui.QTextEdit(self)
    self.setCentralWidget(self.text)
    self.initToolbar()
    self.initFormatbar()
    self.initMenubar()

    # Initialize a status bar for the window
    self.statusbar = self.statusBar()
    self.setGeometry(100,100,1030,800)
    self.setWindowTitle("Mist")
