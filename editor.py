import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.filename = ""
        self.initUI()



    def initToolbar(self):

        self.addToolBarBreak()
        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create a new document.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"), "Open File",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)
        # This makes the next toolbar appear underneath the one above
        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addSeparator()

          # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()



        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()




    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        menubar = self.menubar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)






    def initUI(self):
        self.text = QtGui.QTextEdit(self)

        self.setCentralWidget(self.text)
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        # Initialize a status bar for the window
        self.statusbar = self.statusBar()
        # width and height
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Mist")

    def preview(self):
        # open preview dialog
        preview = QtGui.QPrintPreviewDialog()
        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()



    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):

        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.Mist)")

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        if not self.filename.endswith(".Mist"):
            self.filename += ".Mist"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())


def main():

    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
