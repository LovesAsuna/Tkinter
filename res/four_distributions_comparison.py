import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def three_sampling_dis():
    """
    三大抽样分布与标准正态分布
    :return:
    """
    nor_dis = stats.norm()
    chi2_dis = stats.chi2(df=4)
    t_dis = stats.t(df=5)
    f_dis = stats.f(dfn=30, dfd=5)

    x1 = np.linspace(nor_dis.ppf(0.001), nor_dis.ppf(0.999), 1000)
    x2 = np.linspace(chi2_dis.ppf(0.001), chi2_dis.ppf(0.999), 1000)
    x3 = np.linspace(t_dis.ppf(0.001), t_dis.ppf(0.999), 1000)
    x4 = np.linspace(f_dis.ppf(0.001), f_dis.ppf(0.999), 1000)
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    ax.plot(x1, nor_dis.pdf(x1), 'r-', lw=2, label=r'N(0, 1)')
    ax.plot(x2, chi2_dis.pdf(x2), 'g-', lw=2, label=r'$\chi^2$(4)')
    ax.plot(x3, t_dis.pdf(x3), 'b-', lw=2, label='t(5)')
    ax.plot(x4, f_dis.pdf(x4), 'm-', lw=2, label='F(30, 10)')

    plt.ylabel('Probability')
    plt.title(r'PDF of Three Sampling Distribution')
    ax.legend(loc='best', frameon=False)
    plt.savefig('diff_dist_pdf.png', dip=500)
    plt.show()
