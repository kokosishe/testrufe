class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядеть окно 
        self.initUI() # создаем и настраиваем графические элементы 
        self.connects() # устонавливает связи между элементами
        self.show() #старт