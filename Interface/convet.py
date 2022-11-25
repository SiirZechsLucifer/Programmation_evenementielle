import sys


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()

        widget.setLayout(grid)

        self.__lab1 = QLabel("température")
        self.__text = QLineEdit("")
        self.__lab2 = QLabel("°C")
        self.__cb = QComboBox()
        self.__cb.addItem("K")
        self.__cb.addItem("°C")
        conver = QPushButton("Convertir")
        #self.__cb.currentIndexChanged.connect(self.__selectionchange)
        self.__lab3 = QLabel("conversion")
        self.__lab4 = QLabel("K")
        grid.addWidget(self.__lab1, 0, 0)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(self.__lab2, 0, 2)
        grid.addWidget(conver, 1, 1)
        grid.addWidget(self.__cb, 1, 3)
        grid.addWidget(self.__lab3, 2, 0)
        grid.addWidget(self.__lab4, 2, 3)

    '''def __selectionchange(self):

        if self.__cb.currentIndexChanged:
            self.__cb.setText("K")
            self.__cb.setText("°C")
        else:
            self.__cb.setText("°C")
            self.__cb.setText("K")'''




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()