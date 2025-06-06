from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QTabWidget,
    QWidget, QPushButton, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

import english_script, french_script, spanish_script

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hana Food Distributor, Inc. Tool')
        self.setGeometry(300, 300, 1000, 800)

        # Main container widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.central_widget.setStyleSheet("background-color: #f5f5f5;")

        # === Sidebar ===
        # Add smoother transition, not pushing against main widget content, and dropping down
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setFixedHeight(600)
        self.sidebar.setStyleSheet("background-color: #d8d8d8;")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.addWidget(QLabel("Tool 1"))
        self.sidebar_layout.addWidget(QLabel("Tool 2"))
        self.sidebar_layout.addWidget(QLabel("Tool 3"))
        self.sidebar.setVisible(False)

        # === Main Content Area ===
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)

        # === Hamburger Button ===
        self.hamburger_button = QPushButton("☰")
        self.hamburger_button.setFixedSize(40, 40)
        self.hamburger_button.setStyleSheet("font-size: 24px; background: #254a9d;")
        self.hamburger_button.clicked.connect(self.toggle_sidebar)
        self.content_layout.addWidget(self.hamburger_button, alignment=Qt.AlignLeft)

        # === Header Layout (Logo + Text) ===
        header_layout = QHBoxLayout()

        logo = QLabel()
        pixmap = QPixmap("media/hana_logo.png")
        pixmap = pixmap.scaledToHeight(500, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        label = QLabel("HANA\nTOOL")
        label.setStyleSheet("color: #1d55b4; font-size: 90px; font-weight: 100;")
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        header_layout.addWidget(logo)
        header_layout.addWidget(label)
        header_layout.setAlignment(Qt.AlignHCenter)

        self.content_layout.addLayout(header_layout)

        # === Add sidebar and content to the main layout ===
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content)

    def toggle_sidebar(self):
        self.sidebar.setVisible(not self.sidebar.isVisible())


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
