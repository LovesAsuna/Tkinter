from tkinter import *
from tkinter.ttk import *


class Application(Tk):
    def __init__(self):
        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("350x75")
        self.title("主窗体")

    def createWidgets(self):
        self.selector = Combobox(self)
        self.selector['value'] = (
            '蒙特卡洛方法（求圆周率）',
            '泊松定理',
            '指数分布',
            '正态分布（一维）',
            '正态分布（二维）',
            '卡方分布',
            '三大抽样分布'
        )
        self.selector.current(0)
        self.selector.pack()
        self.button = Button(master=self, text="选择", width=7, command=self.verifiy)
        self.button.pack(side=BOTTOM)

    def verifiy(self):
        num = self.selector.current()
        if num == 0:
            import MonteCarlo
        elif num == 1:
            import Poisson
        elif num == 2:
            import Cumulative
        elif num == 3:
            import Normal
        elif num == 4:
            import Normal2
        elif num == 5:
            import Probability
        elif num == 6:
            import Sampling


app = Application()
app.mainloop()
