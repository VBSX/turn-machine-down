import sys
from PySide6 import QtCore, QtWidgets, QtGui
import subprocess
from time import sleep

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.setStyleSheet("padding :15px;background-color: #00008b;color: #FFFFFF ")
        self.window_wait = WindowMessage()

        self.label_computer = QtWidgets.QLineEdit()
        self.label_computer.setPlaceholderText('Coloque o nome ou IP da maquina ')
        self.button_shutdown = QtWidgets.QPushButton('Desligar maquina', clicked=self.a)
        self.button_restart = QtWidgets.QPushButton('Reiniciar maquina', clicked=self.restart_machine)
        self.label_output = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.label_output.setText("")
        self.label_message = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.label_message.setText("")
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label_computer)
        self.layout.addWidget(self.button_shutdown)
        self.layout.addWidget(self.button_restart)
        self.layout.addWidget(self.label_output)
        self.layout.addWidget(self.label_message)
        
    # def a (self):
    #     if self.verify_label_computer_is_not_empty():
    #         self.window_wait.show()
    #         # try:
    #         #     self.turn_machine_down()
    #         # except:
    #         #     self.show_dialog("erro no desligamento")
    #     else:
    #         self.show_dialog("Coloque o nome da maquina Primeiro!")
    #     self.window_wait.close()
    #     self.label_message.setText("processo finalizado")
        
    def turn_machine_down(self):
        
    
        self.label_message.setText("Aguarde o processo Terminar")     
        command = str(r'shutdown /s /m \\')
        final_command = command+self.label_computer.text()+' /t 0 /f'
        process = subprocess.Popen(final_command, shell=True,stdout=subprocess.PIPE)
        process.kill()
        output = str(process.communicate()[0].decode('utf-8'))
        print(output)
  

                
    def a (self):
        self.window_wait.show()
    def restart_machine(self):
        if self.verify_label_computer_is_not_empty():
            try:
                
                command = str(r'shutdown /r /m \\')
                final_command = command+self.label_computer.text()+' /t 0 /f'
                process = subprocess.Popen(final_command, shell=True,stdout=subprocess.PIPE)
                output = str(process.communicate()[0].decode('utf-8'))
                print(output)
                self.label_output.setText(output)
            except Exception as e:
                self.label_output.setText(e)
          
        else:
            self.show_dialog("Coloque o nome da maquina Primeiro!")
            
    def verify_label_computer_is_not_empty(self):
        if self.label_computer.text():
            return True
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
        
class WindowMessage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.setStyleSheet("padding :15px;background-color: #00008b;color: #FFFFFF ")
        self.label_output = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.label_output.setText("Aguarde o processo Terminar")
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label_output)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    # widget = WindowMessage()
    widget.show()
    sys.exit(app.exec())