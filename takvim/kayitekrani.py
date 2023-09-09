from PyQt5.QtWidgets import *
from kayitekrani_python import Ui_Form
import pyodbc


class kayit_page(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.sign_in_form = Ui_Form()
        self.sign_in_form.setupUi(self)
        self.sign_in_form.pushButton_kaydol.clicked.connect(self.save_data)
    

    def save_data(self):
        name = self.sign_in_form.lineEdit_ad.text()
        surname = self.sign_in_form.lineEdit_soyad.text()
        user_name = self.sign_in_form.lineEdit_kAd.text()
        password = self.sign_in_form.lineEdit_parola.text()
        identity_number = self.sign_in_form.lineEdit_TC.text()
        phone_number = self.sign_in_form.lineEdit_telefon.text()
        email = self.sign_in_form.lineEdit_email.text()
        address = self.sign_in_form.lineEdit_adres.text()
        

        try:
            conn = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',host = 'Baturay',database = "Takvim",trusted_connection = 'yes')

            sql = "INSERT INTO Kullanicilar (Ad,Soyad,KullaniciAdi,Parola,KimlikNo,Telefon,Email,Adres,KullaniciTuru) VALUES (?,?,?,?,?,?,?,?,?)"

            cursor = conn.cursor()
            cursor.execute(sql,name,surname,user_name,password,identity_number,phone_number,email,address,0)
            conn.commit()

            conn.close()
            self.hide()
        except pyodbc.Error as e:
            print("Veritabanı hatası:", e)

