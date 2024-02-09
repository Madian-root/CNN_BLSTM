from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from GUI import Ui_MainWindow, Ui_RegistWindow, Ui_VerifWindow

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Run main loop
sys.exit(app.exec_())
