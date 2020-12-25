import random
import time
from tkinter import *
from tkinter.simpledialog import askinteger

start = time.perf_counter()


class Application(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.canvas = Canvas(self, width=500, height=600, bg='white')

    def create_widgets(self):
        self.canvas.create_rectangle(0, 0, 500, 600, fill="white")
        self.canvas.create_oval(2, 2, 498, 498, fill="yellow", outline='black')
        self.canvas.pack()


def Monte_Carlo(N, root):
    root.create_widgets()
    i = 0
    count = 0
    while i <= N:
        x = random.random() * 500
        y = random.random() * 500
        if pow(x - 250, 2) + pow(y - 250, 2) < 62500:
            count += 1
            root.canvas.create_oval(x, y, x + 5, y + 5, fill="#be4000")
        else:
            root.canvas.create_oval(x, y, x + 5, y + 5, fill="#6c8080")
        root.update()
        i += 1
    pi = 4 * count / N
    t = app.canvas.create_text(200, 550, fill="darkblue", font="Times 20 italic bold",
                               text="圆周率的值是{:.10f}".format(pi))
    app.canvas.update()


def ask_integer():
    return askinteger('请输入参数', prompt='输入一个整数，作为模拟次数', initialvalue=1000, maxvalue=10000, minvalue=1)


def startApp():
    i = ask_integer()
    Monte_Carlo(i, app)


app = Application()
app.title('蒙特卡洛方法（求圆周率）')
app.geometry('500x600')

# 菜单
menubar = Menu(app)
menubar.add_command(label='开始', command=lambda: startApp())
app['menu'] = menubar

app.mainloop()
