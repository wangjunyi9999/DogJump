import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import weight
#uic文件生成py文件指令
# python -m PyQt5.uic.pyuic weight.ui -o weight.py
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = weight.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
