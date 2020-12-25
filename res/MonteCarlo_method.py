import random
import time

start = time.perf_counter()


def monte_carlo(N):
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


monte_carlo(10000)
