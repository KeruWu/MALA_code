
import numpy as np
import argparse
from scipy.stats import norm
from Langevin_algorithms import mala, ula
from target_distribution import f_perturbed, grad_f_perturbed
from plot_function import plot_accept_rate, plot_mixing_time


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-plot", type=str, choices=['acc', 'mix'],
                        help="Plot acceptance rate or mixing time")
    return parser

if __name__ == '__main__':

    parser = get_parser()
    args = parser.parse_args()


    L = m = 1.
    np.random.seed(17)

    ds = 2**np.arange(6, 13)
    dpowers = np.array([0.2, 0.33, 0.5, 0.66, 0.75, 1.0])

    N = 200
    nb_iters = 20000
    delta = 1/40.

    quantile = 0.9
    error = 0.05

    accept_rate = np.zeros((len(ds), len(dpowers)))
    mixing_time = np.zeros((len(ds), len(dpowers)))


    for i, d in enumerate(ds):

        init = np.random.randn(N, d)/1000

        for j, gamma in enumerate(dpowers):
            print('ULA + MALA: d=%s, gamma=%s' % (d, gamma))


            def grad_f_local(x):
                return grad_f_perturbed(x, L=L, m=m)

            def f_local(x):
                return f_perturbed(x,L=L, m=m)


            x_after_ula = ula(init, grad_f_local, nb_iters=50, h_ula=0.1, verbose=False)

            accept, xd = mala(x_after_ula, grad_f_local, f_local, nb_iters=nb_iters,
                              h_mala = 5./(d**gamma), verbose = False)
            accept_rate[i,j] = np.mean(accept[(nb_iters//2):])

            if args.plot == "mix":
                mixing_tmp = np.zeros(N)+nb_iters
                for n in range(N):
                    for iter in range(10, nb_iters, 25):
                        if np.abs(np.quantile(xd[n,:iter], quantile) - norm.isf(1-quantile)) < error:
                            mixing_tmp[n] = iter
                            break
                mixing_time[i,j] = np.mean(mixing_tmp)

    if args.plot == "acc":
        plot_accept_rate(accept_rate, ds, dpowers, 'perturbed_dimension_acc_bad_ula+mala', "Dimension $d$", ylim=1.05, emph=0.5)
    else:
        plot_mixing_time(mixing_time, ds, dpowers, 'perturbed_dimension_mix_bad_ula+mala', "Dimension $d$", ylim=5000, emph=0.5)