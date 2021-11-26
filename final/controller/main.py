from PySide2.QtWidgets import QApplication
from controller.login import Login


if __name__ == "__main__":
    app = QApplication()
    window = Login()
    window.show()

    app.exec_()