from PyQt5.QtWidgets import *
from goruntule_python import Ui_Form
import pyodbc

class view_page(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.viewform = Ui_Form()
        self.viewform.setupUi(self)
        self.viewform.tableWidget.cellChanged.connect(self.update_database)
        self.viewform.pushButton_delete2.clicked.connect(self.delete_event)
    def view_fonk(self):
        
        conn = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',host = 'Baturay',database = "Takvim",trusted_connection = 'yes')

        sql = ''' DECLARE @KullaniciTuru bit
                select @KullaniciTuru = ?

                IF(@KullaniciTuru = 0)
                begin
                    select OlayId,Tarih,BaslangicZamani,OlayinTanimlamasi,OlayTipi,OlayAciklamasi,o.KullaniciId
                    FROM Olaylar o inner join Kullanicilar k on o.KullaniciId = k.KullaniciId WHERE KullaniciTuru = ? and o.KullaniciId = ? and Tarih = ?
                end
                ELSE
                begin
                    select OlayId,Tarih,BaslangicZamani,OlayinTanimlamasi,OlayTipi,OlayAciklamasi,KullaniciId from olaylar where Tarih = ?
                end 
                '''
        
        if (self.user_id == 8):
            KullaniciTuru = 1
        else:
            KullaniciTuru = 0
        
            

        cursor = conn.cursor()
        cursor.execute(sql,KullaniciTuru ,KullaniciTuru,self.user_id,self.date,self.date)
        self.rows = cursor.fetchall()
        
        conn.commit()
        conn.close()
        
        self.populate_table_widget(self.rows)
    def send_date2(self,date):
        self.date = date
    def user_id_catch2(self,user_id):
        self.user_id = int(user_id[0])
    def populate_table_widget(self, data):

        if not data:  # Eğer data boş ise
            self.viewform.tableWidget.clearContents()  # tableWidget'ı temizle
            return  # Fonksiyondan çık ve hiçbir işlem yapma


        self.viewform.tableWidget.setRowCount(len(data))
        self.viewform.tableWidget.setColumnCount(len(data[0]))

        for row_index, row_data in enumerate(data):
            for column_index, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.viewform.tableWidget.setItem(row_index, column_index, item)
    def update_database(self, row, column):
        # Değiştirilen hücrenin değerini alın
        changed_value = self.viewform.tableWidget.item(row, column).text()

        # İlk sütundaki (ID) değeri alın
        event_id = self.viewform.tableWidget.item(row, 0).text()

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
    def delete_event(self):
        # Seçili satırın indeksini al
        current_row = self.viewform.tableWidget.currentRow()

        # Seçili satırın ID'sini al
        event_id = self.viewform.tableWidget.item(current_row, 0).text()

        # QTableWidget'tan seçili satırı sil
        self.viewform.tableWidget.removeRow(current_row)

        # Veritabanından ilgili satırı sil
        self.delete_event_from_database(event_id)
    def delete_event_from_database(self, event_id):
        conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host='Baturay', database="Takvim", trusted_connection='yes')

        sql = "DELETE FROM Olaylar WHERE OlayId = ?"

        cursor = conn.cursor()
        cursor.execute(sql, event_id)
        conn.commit()

        conn.close()

    
        