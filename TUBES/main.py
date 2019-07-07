import sys
import datetime
from Calendar import *
class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calendarWidget.selectionChanged.connect(self.tampildate)
        self.ui.dateEdit.dateChanged.connect(self.tampil)
        self.ui.pushButton.clicked.connect(self.hitungUmur)

    def tampildate(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
    def tampil(self):
        self.ui.calendarWidget.setSelectedDate(self.ui.dateEdit.date())
    def hitungUmur(self):
        date = self.ui.calendarWidget.selectedDate()
        tanggalString = str(date.toPyDate())
        tahun = int(tanggalString[0:4])
        bulan = int(tanggalString[5:7])
        tanggal = int(tanggalString[8:10])
        x = datetime.datetime.now()
        if int(x.month) >= bulan and int(x.day) >= tanggal:
            umur = (int(x.year) - tahun)
        else :
            umur = (int(x.year) - tahun)-1
        self.ui.lineEdit.setText(str(umur)+" Tahun")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
