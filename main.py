import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.display = QLabel()
        self.display.setStyleSheet("font-family: Arial; font-size: 30px; color: white; background-color: black; padding: 10px;")

        layout.addWidget(self.display)
        main_buttons_color = "#282929"
        top_buttons_color = "#a5a5a5"
        side_buttons_color = "#d17402"

        grid = QGridLayout()
        buttons = [
            ('C', 0, 0, top_buttons_color), ('+/-', 0, 1, top_buttons_color), ('%', 0, 2, top_buttons_color), ('/', 0, 3, side_buttons_color),
            ('7', 1, 0, main_buttons_color), ('8', 1, 1, main_buttons_color), ('9', 1, 2, main_buttons_color), ('*', 1, 3, side_buttons_color),
            ('4', 2, 0, main_buttons_color), ('5', 2, 1, main_buttons_color), ('6', 2, 2, main_buttons_color), ('-', 2, 3, side_buttons_color),
            ('1', 3, 0, main_buttons_color), ('2', 3, 1, main_buttons_color), ('3', 3, 2, main_buttons_color), ('+', 3, 3, side_buttons_color),
            ('0', 4, 0, main_buttons_color), ('00', 4,1,main_buttons_color),('.', 4, 2, main_buttons_color), ('=', 4, 3, side_buttons_color)
        ]

        for text,row,col,color in buttons:
            button = QPushButton(text)
            button.setStyleSheet(f"background-color: {color};color: white; width: 60px; height: 60px; font-size: 20px; border-radius: 30px;")
            button.clicked.connect(self.buttonClicked)
            grid.addWidget(button, row, col)

        layout.addLayout(grid)
        self.setStyleSheet("background-color: black;")
    
    def buttonClicked(self):
        button = self.sender().text()
        self.display.setText(self.display.text() + button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())