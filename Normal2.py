import math
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np


def generate():
    x, y = np.mgrid[-10:10:200j, -10:10:200j]
    mu1 = app.m
    mu2 = app.n
    sig1 = app.o
    sig2 = app.p
    rho = app.i
    z = (1 / 2 * math.pi * sig1 * sig2 * ((1 - rho ** 2) ** 0.5)) * \
        np.exp(-(1 / 2 * (1 - rho ** 2)) *
               (((x - mu1) / sig1) ** 2 - 2 * rho * ((x - mu1) / sig1) * ((y - mu2) / sig2) + ((y - mu2) / sig2) ** 2))

    ax = plt.subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow', alpha=0.9)  # 绘面

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


class Application(Tk):
    def __init__(self):
        self.m = 0
        self.n = 0
        self.o = 1
        self.p = 1
        self.i = 0

        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("775x25")
        self.title("二维正态分布")

    def createWidgets(self):
        # 参数μ1
        self.label1 = Label(master=self, text="μ1: ")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(master=self, width=15)
        self.entry1.pack(side=LEFT)
        # 参数μ2
        self.label2 = Label(master=self, text="μ2: ")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(master=self, width=15)
        self.entry2.pack(side=LEFT)
        # 参数σ1
        self.label3 = Label(master=self, text="σ1: ")
        self.label3.pack(side=LEFT)
        self.entry3 = Entry(master=self, width=15)
        self.entry3.pack(side=LEFT)
        # 参数σ2
        self.label4 = Label(master=self, text="σ2: ")
        self.label4.pack(side=LEFT)
        self.entry4 = Entry(master=self, width=15)
        self.entry4.pack(side=LEFT)
        # 参数ρ
        self.label5 = Label(master=self, text="ρ: ")
        self.label5.pack(side=LEFT)
        self.entry5 = Entry(master=self, width=15)
        self.entry5.pack(side=LEFT)
        # 空格
        self.label3 = Label(master=self, text="  ")
        self.label3.pack(side=LEFT)
        self.button = Button(master=self, text="运算", width=7, command=self.verifiy)
        self.button.pack(side=LEFT)

    def verifiy(self):
        self.m = float(self.entry1.get() or self.m)
        self.n = float(self.entry2.get() or self.n)
        self.o = float(self.entry3.get() or self.o)
        self.p = float(self.entry4.get() or self.p)
        self.i = float(self.entry5.get() or self.i)
        generate()
        self.destroy()


app = Application()
app.mainloop()
