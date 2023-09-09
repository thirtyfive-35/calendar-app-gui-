
from PyQt5.QtWidgets import *
from ekle_python import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pyodbc

class ekle_page(QWidget):
    counter = 0
    def __init__(self) -> None:
        super().__init__()
        
        self.add_form = Ui_Form()
        self.add_form.setupUi(self)
        self.add_form.pushButton.clicked.connect(self.save_event)
        self.add_form.tableWidget.cellChanged.connect(self.update_database)
        self.add_form.pushButton_delete.clicked.connect(self.delete_event)
        self.init_counter()

        

    def save_event(self):
        print("save_event called")

        time = self.time_calculator()
        
        # Tabloya verileri ekleme işlemleri
        # Örnek olarak, her tıklamada yeni bir satır eklendiğini varsayalım
        row_count = self.add_form.tableWidget.rowCount()
        self.add_form.tableWidget.insertRow(row_count)

        # Gönderilen verileri alın
        self.date_timer = self.data
        self.start_time = self.add_form.timeEdit.text()
        self.event_define = time
        self.event_type = self.add_form.lineEdit.text()
        self.event_description = self.add_form.lineEdit_2.text()

        self.send_datebase()
        

        # Tabloya verileri ekleme
        item1 = QTableWidgetItem(str(self.counter))
        date_timer_item = QTableWidgetItem(self.date_timer)
        start_time_item = QTableWidgetItem(self.start_time)
        event_define_item = QTableWidgetItem(self.event_define)
        event_type_item = QTableWidgetItem(self.event_type)
        event_description_item = QTableWidgetItem(self.event_description)
        
        self.add_form.tableWidget.setItem(row_count, 0, item1)
        self.add_form.tableWidget.setItem(row_count, 1, date_timer_item)
        self.add_form.tableWidget.setItem(row_count, 2, start_time_item)
        self.add_form.tableWidget.setItem(row_count, 3, event_define_item)
        self.add_form.tableWidget.setItem(row_count, 4, event_type_item)
        self.add_form.tableWidget.setItem(row_count, 5, event_description_item)
        self.counter +=1
    def send_date(self,data):
        self.data = data
    #def send_datebase(self):
    def time_calculator(self):
        # Şu anki zamanı al
        time = datetime.datetime.now()

        # Saat ve dakika değerlerini al
        hour = time.hour
        minute = time.minute

        real_time= str(hour) + ':' + str(minute)
        return real_time
    def send_datebase(self):

        conn = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',host = 'Baturay',database = "Takvim",trusted_connection = 'yes')

        sql = "INSERT INTO Olaylar (KullaniciId,Tarih,BaslangicZamani,OlayinTanimlamasi,OlayTipi,OlayAciklamasi) VALUES (?,?,?,?,?,?)"

        cursor = conn.cursor()
        cursor.execute(sql,self.user_id,self.date_timer,self.start_time,self.event_define,self.event_type,self.event_description)
        conn.commit()

        conn.close()
    def user_id_catch(self,user_id):
        self.user_id = int(user_id[0])
    def update_database(self, row, column):
        # Değiştirilen hücrenin değerini alın
        changed_value = self.add_form.tableWidget.item(row, column).text()

        # İlk sütundaki (ID) değeri alın
        event_id = self.add_form.tableWidget.item(row, 0).text()

        # Güncellemek istediğiniz sütunun adını belirleyin
        column_name = ""
        if column == 1:
            column_name = "Tarih"
        elif column == 2:
            column_name = "BaslangicZamani"
        elif column == 3:
            column_name = "OlayinTanimlamasi"
        elif column == 4:
            column_name = "OlayTipi"
        elif column == 5:
            column_name = "OlayAciklamasi"

        # Veritabanında güncelleme işlemini gerçekleştirin
        if column_name:
            self.update_event_in_database(event_id, column_name, changed_value)
    def update_event_in_database(self, event_id, column_name, changed_value):
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host='Baturay', database="Takvim", trusted_connection='yes')

        sql = f"UPDATE Olaylar SET {column_name} = ? WHERE OlayId = ?"

        cursor = conn.cursor()
        cursor.execute(sql, changed_value, event_id)
        conn.commit()

        conn.close()
    def init_counter(self):
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host='Baturay', database="Takvim", trusted_connection='yes')

        sql = "SELECT MAX(OlayId) FROM Olaylar"

        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()

        if result[0] is not None:
            self.counter = result[0]
        else:
            self.counter = 0

        conn.close()
    def delete_event(self):
        # Seçili satırın indeksini al
        current_row = self.add_form.tableWidget.currentRow()

        # Seçili satırın ID'sini al
        event_id = self.add_form.tableWidget.item(current_row, 0).text()

        # QTableWidget'tan seçili satırı sil
        self.add_form.tableWidget.removeRow(current_row)

        # Veritabanından ilgili satırı sil
        self.delete_event_from_database(event_id)
    def delete_event_from_database(self, event_id):
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host='Baturay', database="Takvim", trusted_connection='yes')

        sql = "DELETE FROM Olaylar WHERE OlayId = ?"

        cursor = conn.cursor()
        cursor.execute(sql, event_id)
        conn.commit()

        conn.close()
    



    




    
        
