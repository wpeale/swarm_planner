import sys
from PyQt4 import QtGui, QtCore


class Communicate(QtCore.QObject):
    
    updateCW = QtCore.pyqtSignal(int)


class CopterWidget(QtGui.QWidget):
  
    def __init__(self):      
        super(CopterWidget, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setMinimumSize(75, 75)
        self.copterID = 1
	self.pos = "0.0"
	self.battery = "100"
	self.heading = "360"
	self.other = 1


    def setCopterID(self, value):

        self.copterID = value
	
    def setPos(self, value):
	
	self.pos = value
    
    def setBattery(self, value):
	
	self.battery = value


    def paintEvent(self, e):
      
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
      
    def drawWidget(self, qp):
      
        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, 
            QtCore.Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
	text = "Copter " + str(self.copterID)
        metrics = qp.fontMetrics()
        fw = metrics.width(text)
        qp.drawText(w/2-fw/2, h/10, text)
	text = "Pos: " + str(self.pos)
	fw = metrics.width(text)
	qp.drawText(w/2-fw/2, h/4, text)
	text = "Hdg: " + str(self.heading)
	fw = metrics.width(text)
	qp.drawText(w/2-fw/2, h/2, text)
	text = "Batt: " + str(self.battery) + "%"
	fw = metrics.width(text)
	qp.drawText(w/2-fw/2, 3*h/4, text)
	

            

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      
	self.Copters = []
	copters_per_row = 3
	grid = QtGui.QGridLayout()
	for i in range(9):
		self.c = Communicate()        
		self.Copters.append(CopterWidget())
		self.c.updateCW[int].connect(self.Copters[i].setCopterID)
		self.c.updateCW.emit(i+1)
		self.Copters[i].repaint()
		grid.addWidget(self.Copters[i],i%copters_per_row,i/copters_per_row)
        """hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)"""
        self.setLayout(grid)
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Swarm Planner v(-1.0)')
        self.show()
        
    def changeValue(self, value, copter):
             
        self.c.updateBW.emit(value)        
        self.Copters[copter].repaint()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
