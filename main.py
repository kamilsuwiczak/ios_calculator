import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.display = QLineEdit()

        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ('C', 0, 0, "gray"), ('+/-', 0, 1, "gray"), ('%', 0, 2, "gray"), ('/', 0, 3, "orange"),
            ('7', 1, 0, "dark"), ('8', 1, 1, "dark"), ('9', 1, 2, "dark"), ('*', 1, 3, "orange"),
            ('4', 2, 0, "dark"), ('5', 2, 1, "dark"), ('6', 2, 2, "dark"), ('-', 2, 3, "orange"),
            ('1', 3, 0, "dark"), ('2', 3, 1, "dark"), ('3', 3, 2, "dark"), ('+', 3, 3, "orange"),
            ('0', 4, 0, "dark_large"), ('.', 4, 2, "dark"), ('=', 4, 3, "orange")
        ]

        for text,row,col,color in buttons:
            button = QPushButton(text)
            button.setStyleSheet(f"background-color: {color}")
            # button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, row, col)

        layout.addLayout(grid)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())