from PyQt6.QtCore import QBuffer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys


def btnfunc():
    print("btn1 clicked.")
    pass


app = QApplication(sys.argv)
w = QWidget()
w.resize(300, 200)
w.move(260, 240)
w.setWindowTitle("PyQt窗口")

btn = QPushButton(w)
btn.setText("Test Button")
btn.move(120, 150)
btn.clicked.connect(btnfunc)

w.show()
sys.exit(app.exec())
