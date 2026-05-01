from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
)
import sys


class CircleCal(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.initUi()

    def initUi(self):
        QLabel("半径=", self).setGeometry(80, 40, 71, 21)
        self.leRadius = QLineEdit(self)
        self.leRadius.setGeometry(140, 40, 113, 21)
        self.leRadius.returnPressed.connect(self.calCircle)

        QLabel("周长=", self).setGeometry(80, 80, 71, 21)
        self.leLength = QLineEdit(self)
        self.leLength.setGeometry(140, 80, 113, 21)
        self.leLength.setEnabled(False)

        QLabel("面积=", self).setGeometry(80, 120, 71, 21)
        self.leArea = QLineEdit(self)
        self.leArea.setGeometry(140, 120, 113, 21)
        self.leArea.setEnabled(False)

        self.pbCal = QPushButton("计算", self)
        self.pbCal.setGeometry(140, 160, 93, 28)
        self.pbCal.clicked.connect(self.calCircle)

        self.resize(350, 200)
        self.move(300, 300)
        self.setWindowTitle("计算圆面积")

    def calCircle(self):
        r = int(self.leRadius.text())
        if r >= 0:
            length = 2 * 3.14159 * r
            area = 3.14159 * r * r
            self.leLength.setText(str(length))
            self.leArea.setText(str(area))


app = QApplication(sys.argv)
dlg = CircleCal()
dlg.show()
sys.exit(app.exec())
