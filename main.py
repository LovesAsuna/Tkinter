import random
import time
from tkinter import *

start = time.perf_counter()


class Application(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.createWidgets()

    def createWidgets(self):
        self.canvas = Canvas(self, width=500, height=500, bg='white')
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 500, 500, fill="red")


def monteCarlo(N, root):
    i = 0
    count = 0
    while i <= N:
        x = random.random()
        y = random.random()
        if pow(x, 2) + pow(y, 2) < 1:
            count += 1
        i += 1
    pi = 4 * count / N
    print("圆周率的值是{:.10f}".format(pi))
    print("程序运行时间为{}s".format(time.perf_counter() - start))


app = Application()
# 设置窗口标题:
app.title('test')
app.mainloop()
monteCarlo(10000000, app)
