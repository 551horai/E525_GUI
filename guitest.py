import sys
from PyQt4 import QtGui, QtCore

class ButtonBoxWidget(QtGui.QWidget):
	def __init__(self):
		super(ButtonBoxWidget, self).__init__()
		self.initUI()

	def initUI(self):
		check_QDC = QtGui.QCheckBox("QDC", self)
		check_TDC = QtGui.QCheckBox("TDC", self)
		check_FADC = QtGui.QCheckBox("FADC", self)
		check_BG = QtGui.QCheckBox("BackGround", self)

		combo_daq = QtGui.QComboBox(self)
		combo_daq.addItem("Ge")
		combo_daq.addItem("CsI")
		combo_daq.addItem("LaBr")
		combo_daq.addItem("LqS")
		combo_daq.addItem("kill")
		
		combo_beam = QtGui.QComboBox(self)
		combo_beam.addItem("30[MeV]")
		combo_beam.addItem("246[MeV]")
		
		combo_RI = QtGui.QComboBox(self)
		combo_RI.addItem("137Cs")
		combo_RI.addItem("60Co")
		combo_RI.addItem("22Na")
		combo_RI.addItem("252Cf")
		combo_RI.addItem("241AmBe")

		event = QtGui.QLabel("n")
		time = QtGui.QLabel("t")	
		source = QtGui.QLabel("Source")
		beam = QtGui.QLabel("Beam")
		RI = QtGui.QLabel("RI")
		BG = QtGui.QLabel("Background")
		event_edit = QtGui.QLineEdit()
		time_edit = QtGui.QLineEdit()

		Run = QtGui.QPushButton("Run", self)

		ch = range(16)
		for i in range(16):
			ch[i] = QtGui.QLabel("ch%d" %i, self)
		combo = range(16)
		for i in range(16):
			combo[i] = combo_daq

		layout = QtGui.QGridLayout()
		layout.addWidget(check_QDC, 0, 0)
		layout.addWidget(check_TDC, 1, 0)
		layout.addWidget(check_FADC, 2, 0)
		for i in range(16):
			layout.addWidget(ch[i], i+3, 0)
		for j in range(16):
			layout.addWidget(combo[i], j+3, 1)
		layout.addWidget(event, 19, 0)
		layout.addWidget(event_edit, 19, 1)
		layout.addWidget(time, 20, 0)
		layout.addWidget(time_edit, 20 ,1)
		layout.addWidget(source, 21, 0)	
		layout.addWidget(beam, 22, 0)
		layout.addWidget(RI, 22, 1)
		layout.addWidget(BG, 22,2)
		layout.addWidget(combo_beam, 23, 0)	
		layout.addWidget(combo_RI, 23, 1)
		layout.addWidget(check_BG, 23, 2)
		layout.addWidget(Run, 24, 3)

		self.setLayout(layout)
		
		self.setGeometry(100, 200, 300, 400)
		self.show()


	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, "Message", "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

class Running(QtGui.QWidget):
	def __init__(self):
		super(Running, self).__init__()
		self.initUI()
        
	def initUI(self):
		info = QtGui.QLabel("#Run information")

		layout = QtGui.QGridLayout()
		layout.addWidget(info, 1,0)
		self.setLayout(layout)
		self.setGeometry(510,200,500,500)
		self.show()

	def start_timer(self):
		if self.count > 0:
			self.timer.start()

	def stop_timer(self):
		self.timer.stop()
		
	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, "Message", "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
	app = QtGui.QApplication(sys.argv)
	#left = QtGui.QFrame(self)
	#left.setFrameShape(QtGui.QFrame.StyledPanel)
	
    #right = QtGui.QFrame(self)
	#right.setFrameShape(QtGui.QFrame.StyledPanel)

	#splitter = QtGui.QSplitter(self)
	#splitter.addWidget(left)
	#splitter.addWidget(right)

	#hbox.addWidget(splitter)
	#hbox.addWidget(combo)
	#self.setLayout(hbox)

	#self.setGeometry(300, 300, 700 ,500)
	#self.setWindowTitle("test")
	#self.show()
	btn = ButtonBoxWidget()
	running = Running()
	#ButtonBoxWidget.Run.clicked.connect(Running)
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
