import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Temperature")

        self.__cb = PyQt5.QComboBox()
        self.__cb.addItem("°C")
        self.__cb.addItem("K")


        self.__text = QLineEdit("")
        self.__repons = QLabel("")
        lab3 = QLabel("°C")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        # Ajouter les composants au grid ayout
        grid.addWidget(lab,0,1)
        grid.addWidget(self.__text,0,2)
        grid.addWidget(lab3, 0, 3)
        grid.addWidget(ok)
        grid.addWidget(self.__repons)

        grid.addWidget(quit)

        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("hahahahahaha")

    def __actionOk(self):
        self.__repons.setText(f"bonjour,{self.__text.text()}")


    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()