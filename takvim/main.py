from PyQt5.QtWidgets import QApplication
from anapencere import anapencere_page
from girisyap import girisyap_page


app = QApplication([])
pencere = girisyap_page()
pencere.show()
app.exec_()
