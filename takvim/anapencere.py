from PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from ekle import ekle_page
from PyQt5 import QtCore, QtGui, QtWidgets
from goruntule import view_page
from PyQt5.QtCore import QTimer
import pyodbc
import datetime
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QSound



class anapencere_page(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_window_form = Ui_MainWindow()
        self.main_window_form.setupUi(self)
        self.add_page_obj = ekle_page()
        self.view_page_obj = view_page()
        self.main_window_form.pushButton.clicked.connect(self.add_page_open)
        self.main_window_form.pushButton_2.clicked.connect(self.view_page_open)
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_events)
        self.timer.start(60000)  # Her 60 saniyede bir kontrol eder
        
        
        
        
    def add_page_open(self):
        self.selected_date = self.main_window_form.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)  # Seçilen tarihi alıyoruz
        self.add_page_obj.show()
        self.add_page_obj.send_date(self.selected_date)
        print(self.selected_date)
    def user_id_send(self,user_id):
        self.add_page_obj.user_id_catch(user_id)
        self.view_page_obj.user_id_catch2(user_id)
    def view_page_open(self):
        self.selected_date2 = self.main_window_form.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        self.view_page_obj.show()
        self.view_page_obj.send_date2(self.selected_date2)
        self.view_page_obj.view_fonk()
    def check_events(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Takvim;Trusted_Connection=yes;')
        sql = "SELECT * FROM Olaylar WHERE DAY(Tarih) = DAY(GETDATE()) AND MONTH(Tarih) = MONTH(GETDATE()) AND YEAR(Tarih) = YEAR(GETDATE()) AND BaslangicZamani > CONVERT(varchar(5), GETDATE(), 108)"
        cursor = conn.cursor()
        cursor.execute(sql)
        events = cursor.fetchall()

        for event in events:
            event_start_time = event.BaslangicZamani
            current_time = datetime.datetime.now().time()

            if (datetime.datetime.combine(datetime.date.today(), event_start_time) - datetime.datetime.combine(datetime.date.today(), current_time)).total_seconds() <= 60:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(f"{event.OlayId} adlı olay 1 dakika içinde başlayacak.")
                msg.setWindowTitle("Olay Uyarısı")
                msg.exec_()
                self.alarm_music()
                
                
    def alarm_music(self):
        
         # Müzik dosyasının yolunu belirtin
        music_file = "music.wav"

        # QSound örneği oluşturun ve müziği çalın
        QSound.play(music_file)

        
                
   
    
                

        
        

                

        

        
