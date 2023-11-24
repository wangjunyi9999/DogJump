from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
                             QMainWindow, QTextEdit, 
                             QAction, QApplication, 
                             QPushButton,QVBoxLayout)
from PyQt5.QtGui import QIcon
import sys
#uic文件生成py文件指令
# python -m PyQt5.uic.pyuic weight.ui -o weight.py
class Example(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        #设置了提示框的字体，我们使用了10px的SansSerif字体。    
        #QToolTip.setFont(QFont('SansSerif', 10))
        #setTooltip()创建提示框，鼠标悬停在相应控件时会显示提示信息
        #self.setToolTip('This is a <b>QWidget</b> widget')
        #创建一个按钮，并且为按钮添加了一个提示框
        btn_serial = QPushButton('串口连接', self)
        btn_save = QPushButton('保存数据', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')
        #调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()方法提供了一个默认的按钮大小。
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_serial)
        hbox.addWidget(btn_save)
        # btn_serial.resize(btn_serial.sizeHint())
        # btn_serial.move(50, 50)       
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
 
        self.setLayout(vbox)    

        self.setGeometry(300, 200,1000, 800)# 整体尺寸(pos_x,pos_y, length, width)
        self.setWindowTitle('一体化关节测试')    
        self.show()

if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())