import sys

from PyQt5.QtCore import QCoreApplication
import PyQt5.QtWidgets


class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #

        #
        widget = PyQt5.QtWidgets.QWidget()
        self.setCentralWidget(widget)
        grid = PyQt5.QtWidgets.QVBoxLayout()
        widget.setLayout(grid)
        lab = PyQt5.QtWidgets.QLabel("Saisir votre nom")
        self.__text = PyQt5.QtWidgets.QLineEdit("")
        self.__repons = PyQt5.QtWidgets.QLabel("")
        ok = PyQt5.QtWidgets.QPushButton("Ok")
        quit = PyQt5.QtWidgets.QPushButton("Quitter")
        # Ajouter les composants au grid ayout
        grid.addWidget(lab)
        grid.addWidget(self.__text)
        grid.addWidget(ok)
        grid.addWidget(self.__repons)

        grid.addWidget(quit)

        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("welcome")

    def __actionOk(self):
        self.__repons.setText(f"bonjour,{self.__text.text()}")


    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()