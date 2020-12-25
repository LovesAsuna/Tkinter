import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


def generate():
    # Python实现正态分布
    # 绘制正态分布概率密度函数
    u = app.m  # 均值μ
    u01 = -2
    sig = app.n  # 标准差δ
    sig01 = math.sqrt(1)
    sig02 = math.sqrt(5)
    sig_u01 = math.sqrt(0.5)
    x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
    x_01 = np.linspace(u - 6 * sig, u + 6 * sig, 50)
    x_02 = np.linspace(u - 10 * sig, u + 10 * sig, 50)
    x_u01 = np.linspace(u - 10 * sig, u + 1 * sig, 50)
    y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
    y_sig01 = np.exp(-(x_01 - u) ** 2 / (2 * sig01 ** 2)) / (math.sqrt(2 * math.pi) * sig01)
    y_sig02 = np.exp(-(x_02 - u) ** 2 / (2 * sig02 ** 2)) / (math.sqrt(2 * math.pi) * sig02)
    y_sig_u01 = np.exp(-(x_u01 - u01) ** 2 / (2 * sig_u01 ** 2)) / (math.sqrt(2 * math.pi) * sig_u01)
    plt.plot(x, y_sig, "r-", linewidth=2)
    plt.plot(x_01, y_sig01, "g-", linewidth=2)
    plt.plot(x_02, y_sig02, "b-", linewidth=2)
    plt.plot(x_u01, y_sig_u01, "m-", linewidth=2)
    # plt.plot(x, y, 'r-', x, y, 'go', linewidth=2,markersize=8)
    plt.grid(True)
    plt.show()


class Application(Tk):
    def __init__(self):
        self.m = 0
        self.n = math.sqrt(0.2)

        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("350x25")
        self.title("正态分布")

    def createWidgets(self):
        # 参数μ
        self.label1 = Label(master=self, text="μ: ")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(master=self, width=15)
        self.entry1.pack(side=LEFT)
        # 参数σ
        self.label2 = Label(master=self, text="σ: ")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(master=self, width=15)
        self.entry2.pack(side=LEFT)

        # 空格
        self.label3 = Label(master=self, text="  ")
        self.label3.pack(side=LEFT)
        self.button = Button(master=self, text="运算", width=7, command=self.verifiy)
        self.button.pack(side=LEFT)

    def verifiy(self):
        self.m = float(self.entry1.get() or self.m)
        self.n = float(self.entry2.get() or self.n)
        generate()
        self.destroy()


app = Application()
app.mainloop()
