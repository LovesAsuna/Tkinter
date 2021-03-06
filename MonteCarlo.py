import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger

start = time.perf_counter()


class Application(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.createWidgets()

    def createWidgets(self):
        self.canvas = Canvas(self, width=500, height=500, bg='white')
        self.canvas.create_rectangle(0, 0, 500, 500, fill="#d9c682")
        self.canvas.create_oval(2, 2, 498, 498, fill="#d9c682", outline='black')
        self.canvas.pack()


def monteCarlo(root):
    N = askinteger("参数:", prompt='输入一个整数，作为模拟次数', initialvalue=10000000, maxvalue=10000000, minvalue=100)
    i = 0
    count = 0
    while i <= N:
        x = random.random() * 500
        y = random.random() * 500
        if pow(x - 250, 2) + pow(y - 250, 2) < 62500:
            count += 1
            root.canvas.create_oval(x, y, x + 5, y + 5, fill="#bf4c03")
        else:
            root.canvas.create_oval(x, y, x + 5, y + 5, fill="#6f7976")
        root.update()
        i += 1
    pi = 4 * count / N
    messagebox.showinfo("结果", "程序运行时间为{}s".format(time.perf_counter() - start) + "\n" + "圆周率的值是{:.10f}".format(pi))


app = Application()
# 设置窗口标题:
app.title('蒙特卡洛方法（求圆周率）')
app.geometry('500x500')
app.resizable(False, False)
monteCarlo(app)
app.mainloop()
