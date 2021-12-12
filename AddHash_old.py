import sys
from PyQt5 import QtCore 
# from PyQt5.QtCore import *


#from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QMainWindow,QWidget, QAction, qApp, QToolTip,  QPushButton, QApplication,
QTableView,QHeaderView,QVBoxLayout, QMenu, QMenuBar, QFileDialog)
from PyQt5.QtGui import *


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        #QToolTip.setFont(QFont('SansSerif', 10))

        #self.setToolTip('This is a <b>QWidget</b> widget')

        #btn = QPushButton('Button', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')
        #btn.resize(btn.sizeHint())
        #btn.move(50, 50)

        #self.setGeometry(300, 300, 300, 200)
        #self.setWindowTitle('Tooltips')
        tbl = Table(self)
        self.cmb()
        self.show()

        
    def cmb(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction('Открыть',self.action_clicked)
        fileMenu.addAction('Сохранить',self.action_clicked)
        
    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]
            f = open(fname,'r')
            with f:
                data = f.read()
                print(data)
            f.close()
        elif action.text() == 'Сохранить':
            print('sdfgsdfg')
        
        
    

        
        # fileToolBar->addAction(openAct);








class Table(QWidget):
    def __init__(self,parent=None):
        super(Table, self).__init__(parent)
        # Установить заголовок и начальный размер
        self.setWindowTitle('Пример представления таблицы QTableView')
        self.resize(500,300)

        # Установить иерархию данных, 4 строки и 4 столбца
        self.model=QStandardItemModel(4,4)
        # Установить текстовое содержимое четырех меток заголовка в горизонтальном направлении
        self.model.setHorizontalHeaderLabels(['Название 1','Название 2','Название 3','Название 4'])


        # # Тодо оптимизации 2 добавить данные
        self.model.appendRow([
            QStandardItem('row %s,column %s' % (5,1)),
            QStandardItem('row %s,column %s' % (11,2)),
            QStandardItem('row %s,column %s' % (11,11)),
            QStandardItem('row %s,column %s' % (11,11)),
        ])

        for row in range(4):
            for column in range(4):
                item=QStandardItem('row %s,column %s'%(row,column))
                # Установить текстовое значение каждой позиции
                self.model.setItem(row,column,item)

        # Создать представление таблицы, установить модель на пользовательскую модель
        self.tableView=QTableView()
        self.tableView.setModel(self.model)



        # #todo Оптимизация 1 Форма заполняет окно
        # #Горизонтальная метка расширяет остальную часть окна и заполняет форму
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # # Горизонтальное направление, размер таблицы увеличивается до соответствующего размера
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #
        # #TODO Optimization 3 Удалить текущие выбранные данные
        # indexs=self.tableView.selectionModel().selection().indexes()
        # print(indexs)
        # if len(indexs)>0:
        #     index=indexs[0]
        #     self.model.removeRows(index.row(),1)


        # Установить макет
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        

    
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = MainWin()
    #table=Table()
    #ex.show()
    sys.exit(app.exec_())

    
    sys.exit(app.exec_())