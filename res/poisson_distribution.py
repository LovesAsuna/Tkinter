import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


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
    plt.figure(1)
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
    plt.show()


compare_binom_poisson(mu=4, n1=8, n2=50)
