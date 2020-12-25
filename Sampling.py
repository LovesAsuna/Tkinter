from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def three_sampling_dis():
    """
    三大抽样分布与标准正态分布
    :return:
    """
    nor_dis = stats.norm()
    chi2_dis = stats.chi2(df=app.df1)
    t_dis = stats.t(df=app.df2)
    f_dis = stats.f(dfn=app.df3, dfd=app.df4)

    x1 = np.linspace(nor_dis.ppf(0.001), nor_dis.ppf(0.999), 1000)
    x2 = np.linspace(chi2_dis.ppf(0.001), chi2_dis.ppf(0.999), 1000)
    x3 = np.linspace(t_dis.ppf(0.001), t_dis.ppf(0.999), 1000)
    x4 = np.linspace(f_dis.ppf(0.001), f_dis.ppf(0.999), 1000)
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    ax.plot(x1, nor_dis.pdf(x1), 'r-', lw=2, label=r'N(0, 1)')
    ax.plot(x2, chi2_dis.pdf(x2), 'g-', lw=2, label=f'$\chi^2$({app.df1})')
    ax.plot(x3, t_dis.pdf(x3), 'b-', lw=2, label=f't({app.df2})')
    ax.plot(x4, f_dis.pdf(x4), 'm-', lw=2, label=f'F({app.df3}, {app.df4 * 2})')

    plt.ylabel('Probability')
    plt.title(r'PDF of Three Sampling Distribution')
    ax.legend(loc='best', frameon=False)
    plt.show()


class Application(Tk):
    def __init__(self):
        self.df1 = 4
        self.df2 = 5
        self.df3 = 30
        self.df4 = 5
        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("650x25")
        self.title("三大抽样分布")

    def createWidgets(self):
        # 参数1
        self.label1 = Label(master=self, text="χ2:n: ")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(master=self, width=15)
        self.entry1.pack(side=LEFT)
        # 参数2
        self.label2 = Label(master=self, text="t:n: ")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(master=self, width=15)
        self.entry2.pack(side=LEFT)
        # 参数3
        self.label3 = Label(master=self, text="F:n1: ")
        self.label3.pack(side=LEFT)
        self.entry3 = Entry(master=self, width=15)
        self.entry3.pack(side=LEFT)
        # 参数4
        self.label4 = Label(master=self, text="F:n2: ")
        self.label4.pack(side=LEFT)
        self.entry4 = Entry(master=self, width=15)
        self.entry4.pack(side=LEFT)
        # 空格
        self.label5 = Label(master=self, text="  ")
        self.label5.pack(side=LEFT)
        self.button = Button(master=self, text="运算", width=7, command=self.verifiy)
        self.button.pack(side=LEFT)

    def verifiy(self):
        self.df1 = float(self.entry1.get() or self.df1)
        self.df2 = float(self.entry2.get() or self.df2)
        self.df3 = float(self.entry3.get() or self.df3)
        self.df4 = float(self.entry4.get() or self.df4)
        three_sampling_dis()
        self.destroy()


app = Application()
app.mainloop()
