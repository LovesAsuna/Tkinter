from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def diff_chi2_dis():
    """
    不同参数下的卡方分布
    :return:
    """
    # chi2_dis_0_5 = stats.chi2(df=0.5)
    chi2_dis_1 = stats.chi2(df=app.df1)
    chi2_dis_4 = stats.chi2(df=app.df2)
    chi2_dis_10 = stats.chi2(df=app.df3)
    chi2_dis_20 = stats.chi2(df=app.df4)

    # x1 = np.linspace(chi2_dis_0_5.ppf(0.01), chi2_dis_0_5.ppf(0.99), 100)
    x2 = np.linspace(chi2_dis_1.ppf(0.65), chi2_dis_1.ppf(0.9999999), 100)
    x3 = np.linspace(chi2_dis_4.ppf(0.000001), chi2_dis_4.ppf(0.999999), 100)
    x4 = np.linspace(chi2_dis_10.ppf(0.000001), chi2_dis_10.ppf(0.99999), 100)
    x5 = np.linspace(chi2_dis_20.ppf(0.00000001), chi2_dis_20.ppf(0.9999), 100)
    fig, ax = plt.subplots(1, 1)
    # ax.plot(x1, chi2_dis_0_5.pdf(x1), 'b-', lw=2, label=r'df = 0.5')
    ax.plot(x2, chi2_dis_1.pdf(x2), 'g-', lw=2, label=f'df = %{app.df1}')
    ax.plot(x3, chi2_dis_4.pdf(x3), 'r-', lw=2, label=f'df = %{app.df2}')
    ax.plot(x4, chi2_dis_10.pdf(x4), 'b-', lw=2, label=f'df = %{app.df3}')
    ax.plot(x5, chi2_dis_20.pdf(x5), 'y-', lw=2, label=f'df = %{app.df4}')
    plt.ylabel('Probability')
    plt.title(r'PDF of $\chi^2$ Distribution')
    ax.legend(loc='best', frameon=False)
    plt.show()


class Application(Tk):
    def __init__(self):
        self.df1 = 1
        self.df2 = 4
        self.df3 = 10
        self.df4 = 20
        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("650x25")
        self.title("χ2分布")

    def createWidgets(self):
        # 参数1
        self.label1 = Label(master=self, text="df1: ")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(master=self, width=15)
        self.entry1.pack(side=LEFT)
        # 参数2
        self.label2 = Label(master=self, text="df2: ")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(master=self, width=15)
        self.entry2.pack(side=LEFT)
        # 参数3
        self.label3 = Label(master=self, text="df3: ")
        self.label3.pack(side=LEFT)
        self.entry3 = Entry(master=self, width=15)
        self.entry3.pack(side=LEFT)
        # 参数4
        self.label4 = Label(master=self, text="df4: ")
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
        diff_chi2_dis()
        self.destroy()


app = Application()
app.mainloop()