# Form implementation generated from reading ui file 'wizard.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, uic


class MetadataCertification(QtWidgets.QWizard):
    def __init__(self, *args, **kwargs):
        super(MetadataCertification, self).__init__(*args, **kwargs)
        uic.loadUi("wizard.ui", self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MetadataCertification()
    MainWindow.show()
    sys.exit(app.exec())
