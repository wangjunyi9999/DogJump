import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

class SerialDataCollector(QMainWindow):
    def __init__(self):
        super().__init__()

        self.serial_port = None
        self.data_buffer = ""

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Serial Data Collector")
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        connect_button = QPushButton("Connect", self)
        connect_button.clicked.connect(self.connect_serial)
        connect_button.resize(30,30)
        connect_button.move(50,50)

        save_button = QPushButton("Save Data", self)
        save_button.clicked.connect(self.save_data)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(connect_button)
        layout.addWidget(save_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def connect_serial(self):
        if not self.serial_port:
            try:
                self.serial_port = serial.Serial('COM5', 9600)  # 串口名称和波特率，请根据你的需求修改
                self.text_edit.append("Serial port connected.")
            except serial.SerialException as e:
                self.text_edit.append(f"Error connecting to serial port: {str(e)}")
        else:
            self.text_edit.append("Serial port is already connected.")

    def save_data(self):
        if self.serial_port:
            data = self.serial_port.read(100)  # 读取串口数据的示例，根据需要修改
            self.data_buffer += data.decode("utf-8")

            with open("collected_data.txt", "a") as file:
                file.write(self.data_buffer)

            self.text_edit.append("Data saved to 'collected_data.txt'.")

def main():
    app = QApplication(sys.argv)
    window = SerialDataCollector()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
