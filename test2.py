import os
import sys
from PyQt5.QtWidgets import (QSlider, QPushButton, QLabel, QLineEdit, QCheckBox, QApplication, QMainWindow, QAction, qApp)
from PyQt5.QtCore import Qt


class MenuDemo(QMainWindow):
        def __init__(self):
                super().__init__()
                bar = self.menuBar()
                file = bar.addMenu('File')
                edit = bar.addMenu('Edit')
                save_action = QAction('Save', self)
                save_action.setShortcut('Ctrl+S')

                new_action = QAction('New', self)
                new_action.setShortcut('Ctrl+N')

                quit_action = QAction('Quit', self)
                quit_action.setShortcut('Ctrl+Q')

                find_action = QAction('Find', self)
                replace_action = QAction('Replace', self)

                file.addAction(new_action)
                file.addAction(save_action)
                file.addAction(quit_action)

                find_menu = edit.addMenu('Find')
                find_menu.addAction(find_action)
                find_menu.addAction(replace_action)

                quit_action.triggered.connect(self.quit_trigger)
                file.triggered.connect(self.selected)





                self.setWindowTitle('My Menus')
                self.resize(600, 400)

                self.show()
        
        def quit_trigger(self):
                qApp.quit()

        def selected(self):
                pass



if __name__ == '__main__':
        app = QApplication(sys.argv)
        a_window = MenuDemo()
        sys.exit(app.exec_())


                
def main():
        print('Hello')
        # app = QApplication(sys.argv)
        # a_window = MenuDemo()
        # sys.exit(app.exec_())






# class Window(QtWidgets.QWidget):
#         def __init__(self):
#                 super().__init__()
#                 self.init_ui()
#         def init_ui(self):
#                 self.b1 = QtWidgets.QPushButton('Clear')
#                 self.b2 = QtWidgets.QPushButton('Print')
#                 self.l = QtWidgets.QLabel()
#                 self.le = QtWidgets.QLineEdit()
#                 self.s1 = QtWidgets.QSlider(Qt.Horizontal)
#                 self.s1.setMinimum(1)
#                 self.s1.setMaximum(99)
#                 self.s1.setValue(25)
#                 self.s1.setTickInterval(10)
#                 self.s1.setTickPosition(QtWidgets.QSlider.TicksBelow)
#                 self.check = QtWidgets.QCheckBox("Do You like dogs?")

#                 h_box = QtWidgets.QHBoxLayout()

#                 v_box = QtWidgets.QVBoxLayout()
#                 v_box.addWidget(self.le)
#                 v_box.addWidget(self.check)
#                 v_box.addWidget(self.b1)
#                 v_box.addWidget(self.b2)
#                 v_box.addWidget(self.s1)
#                 v_box.addLayout(h_box)

#                 self.setLayout(v_box)
#                 self.setWindowTitle(' My Window')
#                 self.b1.clicked.connect(lambda: self.btn_click(self.b1, "Hello World from Clear"))
#                 self.b2.clicked.connect(lambda: self.btn_click(self.check.isChecked(), self.l))
#                 self.s1.valueChanged.connect(self.v_change)

#                 self.show()
        
#         def btn_click(self, check, l):
#                 # if b.text()=="Print":
#                 #         print(self.le.text())
#                 if check:
#                         l.setText("I guess you like dog")

#                 else:
#                         l.setText("Dog Hater then")

        
#         def v_change(self):
#                 my_value = str(self.s1.value())
#                 self.le.setText(my_value)


