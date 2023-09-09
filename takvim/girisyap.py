from PyQt5.QtWidgets import *
from girisyap_python import Ui_Form
from anapencere import anapencere_page
from kayitekrani import kayit_page
from hata import error_message
import pyodbc

class girisyap_page(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.girisform = Ui_Form()
        self.anapencerelogin = anapencere_page()
        self.kayit_ol_button = kayit_page()
        self.error_message_obj = error_message()
        self.girisform.setupUi(self)
        self.girisform.pushButton.clicked.connect(self.login)
        self.girisform.pushButton_2.clicked.connect(self.kayitol)
    def login(self):
        user_name = self.girisform.lineEdit.text()
        password = self.girisform.lineEdit_2.text()

        conn = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',host = 'Baturay',database = "Takvim",trusted_connection = 'yes')

        sql = "SELECT KullaniciId from Kullanicilar where KullaniciAdi = ? and Parola = ?"

        cursor = conn.cursor()
        cursor.execute(sql, user_name, password)
        self.user_id = cursor.fetchone()
        self.anapencerelogin.user_id_send(self.user_id)
        conn.commit()
        conn.close()
        try:
            if self.user_id[0] != None:
                self.anapencerelogin.show()
                self.hide()
        except TypeError as a:
            self.error_message_obj.show()
            
    def kayitol(self):
        self.kayit_ol_button.show()
    
    
        


        