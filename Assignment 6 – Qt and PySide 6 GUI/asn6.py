import sys
import random

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox,)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Window Setup
        self.setWindowTitle("Assignment 6")
        self.setGeometry(100, 100, 400, 300)
        
        #Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        #Help Label
        self.lblHelp = QLabel("Enter a interger greater than 2:")
        self.lblHelp.setAlignment(Qt.AlignCenter)
        self.lblHelp.setStyleSheet("background-color: lightgreen; font-size: 25px")
        

        #Input Box
        self.input = QLineEdit()
        self.input.setAlignment(Qt.AlignCenter)

        #Output Label
        self.lblOutput = QLabel("")
        self.lblOutput.setAlignment(Qt.AlignCenter)
        self.lblOutput.setStyleSheet("background-color: lightblue; font-size: 25px")

        #Button
        self.btnCheck = QPushButton("Random Number")
    
        #Widgets
        self.layout.addWidget(self.lblHelp)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.lblOutput)
        self.layout.addWidget(self.btnCheck)

        #Connet Button to Function
        self.btnCheck.clicked.connect(self.update_label)

    def update_label(self):
        text = self.input.text()
        try:
            number = int(text)
            if number <= 2:
                QMessageBox.warning(self, "Invalid Input", "Please enter a number greater than 2")
                return
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number")
            return
        
        #Generate a random number
        rand_num = random.randint(1, number)

        #Display the random number
        self.lblOutput.setText(str(rand_num))

#Application Main Loop
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())    