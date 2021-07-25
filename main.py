
import argparse
from settings import *
from scipy.stats import norm

from MALA import mala
from plot_function import plot_accept_rate, plot_mixing_time
from target_distribution import f_perturbed, grad_f_perturbed, f_gaussian, grad_f_gaussian
from initialization import perturbed_bad_init, perturbed_warm_init, gaussian_warm_init, gaussian_bad_init

grad_f    = {'perturbed' : grad_f_perturbed, 'original' : grad_f_gaussian}
f         = {'perturbed' : f_perturbed,      'original' : f_gaussian}
init_dist = {('perturbed', 'warm') : perturbed_warm_init, ('perturbed', 'bad') : perturbed_bad_init,
             ('gaussian', 'warm')  : gaussian_warm_init,  ('gaussian', 'bad')  : gaussian_bad_init}
plot_f    = {'acc' : plot_accept_rate, 'mix' : plot_mixing_time}


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-target", type=str, choices=['perturbed', 'original'], required=True,
                        help='Target is the perturbed Gaussian or the original Gaussian')
    parser.add_argument("-init", type=str, choices=['warm', 'bad'],
                        help="Warm or bad (feasible) initialization")
    parser.add_argument("-dependency", type=str, choices=['dimension', 'condition'],
                        help="Dimension dependency or condition number dependency")
    parser.add_argument("-plot", type=str, choices=['acc', 'mix'],
                        help="Plot acceptance rate or mixing time")
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    N = 200
    nb_iters = 40000
    quantile = 0.9
    error = 0.05

    title = '_'.join([args.target, args.dependency, args.plot, args.init])
    ds = ds_dict[(args.target, args.dependency, args.init, args.plot)]
    dpowers = dpowers_dict[(args.target, args.dependency, args.init, args.plot)]
    xlabel = xlabel_dict[args.dependency]
    ylim = ylim_dict[(args.target, args.dependency, args.init, args.plot)]
    h_const = h_const_dict[(args.target, args.dependency, args.init, args.plot)]

    np.random.seed(17)

    if args.dependency == 'dimension':
        L = m = 1.

        accept_rate = np.zeros((len(ds), len(dpowers)))
        mixing_time = np.zeros((len(ds), len(dpowers)))


        for i, d in enumerate(ds):
            init = init_dist[(args.target, args.init)](N, d, L, m)
            for j, gamma in enumerate(dpowers):
                print('MALA: d=%s, gamma=%s' % (d, gamma))


                def grad_f_local(x):
                    return grad_f[args.target](x, L=L, m=m)

                def f_local(x):
                    return f[args.target](x, L=L, m=m)


                accept, xd, x_norm= mala(init, grad_f_local, f_local, nb_iters=nb_iters,
                                         h_mala = h_const/(d**gamma), verbose = False)
                accept_rate[i,j] = np.mean(accept[(nb_iters)//2:])

                mixing_tmp = np.zeros(N)+nb_iters
                for n in range(N):
                    for iter in range(10, nb_iters, 10):
                        if np.abs(np.quantile(xd[n,:iter], quantile) - norm.isf(1-quantile)) < error:
                            mixing_tmp[n] = iter
                            break
                mixing_time[i,j] = np.mean(mixing_tmp)

        plot_f[args.plot](accept_rate, ds, dpowers, title, xlabel, ylim)


    else:
        m = 1.
        d = 32
        Ls = ds
        gpowers = dpowers

        accept_rate = np.zeros((len(Ls), len(gpowers)))
        mixing_time = np.zeros((len(Ls), len(gpowers)))

        for i, L in enumerate(Ls):
            init = init_dist[(args.target, args.init)](N, d, L, m)
            for j, gamma in enumerate(gpowers):
                print('MALA: kappa=%s, gamma=%s' % (L, gamma))


                def grad_f_local(x):
                    return grad_f[args.target](x, L=L, m=m)

                def f_local(x):
                    return f[args.target](x, L=L, m=m)


                accept, xd, x_norm= mala(init, grad_f_local, f_local, nb_iters=nb_iters,
                                         h_mala = h_const/(L**gamma*np.sqrt(d)), verbose = False)
                accept_rate[i,j] = np.mean(accept[(nb_iters//2):])

                mixing_tmp = np.zeros(N)+nb_iters
                for n in range(N):
                    for iter in range(10, nb_iters, 20):

                        if np.abs(np.quantile(xd[n,:iter], quantile) - norm.isf(1-quantile)) < error:
                            mixing_tmp[n] = iter
                            break
                mixing_time[i,j] = np.mean(mixing_tmp)
                
        plot_f[args.plot](accept_rate, Ls, gpowers, title, xlabel, ylim)