from PyQt5.QtWidgets import *
from hata_python import Ui_form

class error_message(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.error_form = Ui_form()
        self.error_form.setupUi(self)
        self.error_form.pushButton_error.clicked.connect(self.shutdown)
    def shutdown(self):
        self.hide()
