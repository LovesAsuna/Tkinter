import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy import stats
from tkinter import *


def compare_binom_poisson(mu=4, n1=8, n2=50):
    """
    二项分布与泊松分布的比较
    :param mu: 泊松分布的参数，保持mu不变
    :param n1: 第一个二项分布中的实验次数，n比较小
    :param n2: 第二个二项分布中的实验次数，n比较大
    :return:
    """
    # 为了具有可比性, 利用mu = n * p, 计算p
    p1 = mu / n1  # 二项分布中的参数，单次实验成功的概率
    p2 = mu / n2
    poisson_dist = stats.poisson(mu)  # 初始化泊松分布
    binom_dist1 = stats.binom(n1, p1)  # 初始化第一个二项分布
    binom_dist2 = stats.binom(n2, p2)  # 初始化第二个二项分布

    # 计算pmf
    X = np.arange(poisson_dist.ppf(0.0001), poisson_dist.ppf(0.9999))
    y_po = poisson_dist.pmf(X)
    print(X)
    print(y_po)
    y_bi1 = binom_dist1.pmf(X)
    y_bi2 = binom_dist2.pmf(X)

    # 作图
    # First group
    # 当n比较小，p比较大时，两者差别比较大
    figure1 = plt.figure(1)
    bar1 = FigureCanvasTkAgg(figure1, app)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    plt.subplot(211)
    plt.plot(X, y_bi1, 'b-', label='binom1 (n={}, p={})'.format(n1, p1))
    plt.plot(X, y_po, 'r--', label='poisson (mu={})'.format(mu))
    plt.ylabel('Probability')
    plt.title('Comparing PMF of Poisson Dist. and Binomial Dist.')
    plt.legend(loc='best', frameon=False)

    # second group
    # 当n比较大，p比较小时，两者非常相似
    plt.subplot(212)
    plt.plot(X, y_bi2, 'b-', label='binom1 (n={}, p={})'.format(n2, p2))
    plt.plot(X, y_po, 'r--', label='poisson (mu={})'.format(mu))
    plt.ylabel('Probability')
    plt.legend(loc='best', frameon=False)
    # plt.show()


class Application(Tk):
    def __init__(self):
        self.m = 4
        self.n = 8
        self.p = 50
        Tk.__init__(self, None)
        self.createWidgets()
        self.geometry("1500x600")
        self.title("泊松定理")

    def createWidgets(self):
        # 参数λ
        self.label1 = Label(master=self, text="λ: ")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(master=self, width=15)
        self.entry1.pack(side=LEFT)
        # 参数n
        self.label2 = Label(master=self, text="n: ")
        self.label2.pack(side=LEFT)
        self.entry2 = Entry(master=self, width=15)
        self.entry2.pack(side=LEFT)
        # 参数p
        self.label3 = Label(master=self, text="p: ")
        self.label3.pack(side=LEFT)
        self.entry3 = Entry(master=self, width=15)
        self.entry3.pack(side=LEFT)
        # 空格
        self.label4 = Label(master=self, text="  ")
        self.label4.pack(side=LEFT)
        self.button = Button(master=self, text="运算", width=7, command=self.verifiy)
        self.button.pack(side=LEFT)

    def verifiy(self):
        self.m = float(self.entry1.get() or self.m)
        self.n = float(self.entry2.get() or self.n)
        self.p = float(self.entry3.get() or self.p)
        compare_binom_poisson(app.m, app.n, app.p)
        # self.destroy()


app = Application()
app.mainloop()
