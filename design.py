import systeminfo
import sys
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QGridLayout,QWidget
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("CPU Info")
window.setFixedSize(540,240)

# Create a grid layout
central_widget = QWidget(window)
grid = QGridLayout(central_widget)


label0 = QLabel("", window)
label1 = QLabel("", window)
label2 = QLabel("", window)
label3 = QLabel("",window)

cName = systeminfo.cName
label3.setText(str(cName))
label3.setFont(QFont("arial", 12))
label3.setAlignment(Qt.AlignCenter)

grid.addWidget(label3, 0,0,1,2)
grid.addWidget(label0, 1, 0)
grid.addWidget(label1, 1, 1)
grid.addWidget(label2, 2, 0)


# Create a label
def cpu_info():
    # Get the number of cores
    core = systeminfo.cores
    logical_core = systeminfo.logical_cores
    usage = systeminfo.system.cpu('usage')
    
    label0.setText("Total Cores: "+str(core))
    label1.setText("Logical Cores: "+str(logical_core))
    label2.setText("Cpu usage: "+str(usage))
    #color managemnet
    if systeminfo.cores >= 4:
        label0.setStyleSheet("background-color: limegreen;")
    else:
        label0.setStyleSheet("background-color: red;")

    #End color management
    labelsList = [label0,label1,label2]
    for label in labelsList:
        label.setFont(QFont("arial", 15))
        label.setAlignment(Qt.AlignCenter)



timer = QTimer()
timer.timeout.connect(cpu_info)
timer.start(100)


# Set the grid layout as the central widget of the main window
window.setCentralWidget(central_widget)

# Show the main window
window.show()

# Run the application
sys.exit(app.exec_())
