import numpy as np
from tqdm import tqdm

def neglog_density_normal(x, mean=0., sigma=1.):
    """
    Negative log Density of the normal distribution up to constant
    :param x:      location
    :param mean:   mean
    :param sigma:  standard deviation
    :return:       density value at x
    """
    return np.sum((x - mean)**2, axis=1) / 2 / sigma**2


def mala(x_init, grad_f, f, nb_iters=1000, h_mala = None, verbose = False):
    """
    MALA algorithm
    :param x_init:    initialization  (N, d)
    :param grad_f:    gradient of the negative log density
    :param f:         the negative log density
    :param nb_iters:  number of iterations
    :param h_mala:    step size h
    :param verbose:   show progress bar or not
    :return:          acceptance rate, and the trace of the last dimension xd
    """
    N, d = x_init.shape

    x_curr = x_init.copy()
    xd_all = np.zeros((N, nb_iters))
    xd_all[:,-1] = x_init.copy()[:,-1]

    if h_mala is None:
        raise ValueError("Step size undefined")

    nh_mala = np.sqrt(2 * h_mala)

    accept_rate_all = np.zeros(nb_iters)
    accept_rate_all[0] = 1.0

    for i in (tqdm(range(nb_iters - 1)) if verbose else range(nb_iters-1)):
        proposal = x_curr - h_mala * grad_f(x_curr) \
                   + nh_mala * np.random.randn(N, d)

        log_ratio = - f(proposal) \
                    - neglog_density_normal(x=x_curr,
                                            mean=proposal - h_mala * grad_f(proposal),
                                            sigma=nh_mala)
        log_ratio -= - f(x_curr) \
                     -  neglog_density_normal(x=proposal,
                                              mean=x_curr - h_mala * grad_f(x_curr),
                                              sigma=nh_mala)

        ratio = np.exp(log_ratio)
        # Metropolis Hastings step
        ratio = np.minimum(1., ratio)
        a = np.random.rand(N)
        index_forward = np.where(a <= ratio)[0]
        accept_rate_all[i+1] = len(index_forward)/float(N)

        x_curr[index_forward, ] = proposal[index_forward, ]
        xd_all[:, i] = x_curr[:, -1].copy()


    return accept_rate_all, xd_all



def ula(x_init, grad_f, nb_iters=1000, h_ula = None, verbose = False):
    """
    ULA algorithm
    :param x_init:    initialization  (N, d)
    :param grad_f:    gradient of the negative log density
    :param nb_iters:  number of iterations
    :param h_ula:    step size h
    :param verbose:   show progress bar or not
    :return:          acceptance rate, and the last state of the chain
    """
    N, d = x_init.shape

    x_curr = x_init.copy()

    if h_ula is None:
        raise ValueError("Step size undefined")


    for i in tqdm(range(nb_iters - 1) if verbose else range(nb_iters-1)):

        x_curr += -h_ula * grad_f(x_curr) + np.sqrt(2*h_ula)*np.random.randn(N,d)

    return x_curr