from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QTabWidget, QWidget, QPushButton
from PySide6.QtCore import Qt

import english_script, french_script, spanish_script

# Customize window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize/customize window gui
        self.setWindowTitle('Simple GUI')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Layout the three tabs
        self.tab_widget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        self.layout.addWidget(self.tab_widget)

        self.initTab1()
        self.initTab2()
        self.initTab3()
    
    def initTab1(self):
        layout = QVBoxLayout(self.tab1)

        self.label1 = QLabel("")
        self.label1.setStyleSheet("font-size: 16px;")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button1 = QPushButton("Run Script 1")
        button1.setFixedSize(150, 40)
        button1.clicked.connect(lambda: self.label1.setText(english_script.run()))
        
        layout.addWidget(button1)
        layout.addWidget(self.label1)

    def initTab2(self):
        layout = QVBoxLayout(self.tab2)

        self.label2 = QLabel("")
        self.label2.setStyleSheet("font-size: 16px;")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button2 = QPushButton("Run Script 2")
        button2.setFixedSize(150, 40)
        button2.clicked.connect(lambda: self.label2.setText(french_script.run()))
        
        layout.addWidget(button2)
        layout.addWidget(self.label2)

    def initTab3(self):
        layout = QVBoxLayout(self.tab3)

        self.label3 = QLabel("")
        self.label3.setStyleSheet("font-size: 16px;")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button3 = QPushButton("Run Script 3")
        button3.setFixedSize(150, 40)
        button3.clicked.connect(lambda: self.label3.setText(spanish_script.run()))
        
        layout.addWidget(button3)
        layout.addWidget(self.label3)

app = QApplication([])

# Our window
window = MainWindow()
window.show()

app.exec()