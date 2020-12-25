import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


def generate():
    lambd = app.m
    x = np.arange(0, 15, 0.1)
    y = lambd * np.exp(-lambd * x)
    plt.plot(x, y)
    plt.title('Exponential:$\lambda$=%.2f' % lambd)
    plt.xlabel('x')
    plt.ylabel('Probability density')
    plt.show()

    x = np.arange(0, 15, 0.1)
    y = 1 - np.exp(-lambd * x)
    plt.plot(x, y)
    plt.title('Exponential:$\lambda$=%.2f' % lambd)
    plt.xlabel('x')
    plt.ylabel('cumulative distribution')
    plt.show()


class Application(Tk):
    def __init__(self):
        self.m = 0.5
        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("225x25")
        self.title("指数分布")

    def createWidgets(self):
        # 参数λ
        self.label = Label(master=self, text="λ: ")
        self.label.pack(side=LEFT)
        self.entry = Entry(master=self, width=15)
        self.entry.pack(side=LEFT)
        # 空格
        self.label1 = Label(master=self, text="  ")
        self.label1.pack(side=LEFT)
        self.button = Button(master=self, text="运算", width=7, command=self.verifiy)
        self.button.pack(side=LEFT)

    def verifiy(self):
        self.m = float(self.entry.get() or self.m)
        generate()
        self.destroy()


app = Application()
app.mainloop()
