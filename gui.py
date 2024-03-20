import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class NetworkMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Network Monitor App')
        layout = QVBoxLayout()

        label = QLabel('Hello World!', self)
        layout.addWidget(label)

        button = QPushButton('Click Me!', self)
        button.clicked.connect(self.click_button)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    def click_button(self):
        print('Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NetworkMonitorApp()
    sys.exit(app.exec_())
