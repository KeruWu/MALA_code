import numpy as np
from Langevin_algorithms import mala

def perturbed_warm_init(N, d, L, m, delta=1./40):
    """
    Warm initialization for the perturbed Gaussian target.
    :param N:      number of chains
    :param d:      number of dimensions
    :param delta:  delta in the perturbed Gaussian
    :param L:      L in the perturbed Gaussian
    :param m:      m in the perturbed Gaussian
    :return:       initial positions (N, d)
    """
    x = np.zeros((N, d))
    candidates = np.zeros((5*N, d))
    candidates[:,:-1] = MH_each(5*N, d, delta)
    candidates[:,-1] = np.random.randn(5*N)
    j = 0
    for i in range(candidates.shape[0]):
        if np.linalg.norm(candidates[i,:-1]) < np.sqrt(d-1) and np.abs(candidates[i,-1]) < 1:
            x[j,:-1] = candidates[i,:-1]/np.sqrt(L)
            x[j, -1] = candidates[i, -1]/np.sqrt(m)
            j += 1
        if j==N:
            break
    return x


def MH_each(N, d, delta):
    """
    Helper function for perturbed_warm_init. It generates samples according to the perturbed Gaussian target
    via generating from each dimension. (L = m = 1)
    :param N:       number of samples to generate
    :param d:       number of dimensions
    :param delta:   delta in the perturbed Gaussian
    :return:        N samples
    """
    def f_tmp(x, d=d, delta=delta):
        return 0.5*np.sum(x**2) - 0.5/((d-1)**(0.5-2*delta)) * np.sum(np.cos((d-1)**(0.25-delta)*x))
    def grad_f_tmp(x, d=d, delta=delta):
        return x + 0.5/((d-1)**(0.25-delta)) * np.sin((d-1)**(0.25-delta)*x)
    x = np.zeros((N, d-1))
    for i in range(d-1):
        _, x1 = mala(np.array([[x[0,i]]]), grad_f_tmp, f_tmp, nb_iters=2*N, h_mala = 1., verbose=False)
        x[:,i] = x1[0,N:]
    x = x
    return x


def perturbed_bad_init(N, d, L=1., m=1.):
    """
    Bad (feasible) initialization for the perturbed Gaussian target. (L = m = 1)
    :param N:       number of chains
    :param d:       number of dimensions
    :return:        initial positions  (N, d)
    """
    return np.random.randn(N, d)/1000



def gaussian_warm_init(N, d, L, m):
    """
    Warm initialization for the Gaussian target distribution.
    :param N:       number of chains
    :param d:       number of dimensions
    :param L:       L in the perturbed Gaussian
    :param m:       m in the perturbed Gaussian
    :return:        initial positions (N, d)
    """
    x = np.zeros((N, d))
    candidates = np.random.randn(5*N, d)
    j = 0
    for i in range(candidates.shape[0]):
        if np.linalg.norm(candidates[i,:]) <= np.sqrt(d):
            x[j,:-1] = candidates[i,:-1]/np.sqrt(L)
            x[j, -1] = candidates[i, -1]/np.sqrt(m)
            j += 1
        if j==N:
            break
    return x



def gaussian_bad_init(N, d, L=1., m=1.):
    """
    Bad (feasible) initialization for the Gaussian target distribution (L = m = 1).
    :param N:        number of chains
    :param d:        number of dimensions
    :return:         initial positions (N, d)
    """
    candidates = np.random.randn(5*N, d)/np.sqrt(2)
    res = np.zeros((N, d))
    j = 0
    for i in range(candidates.shape[0]):
        if np.linalg.norm(candidates[i,:-1]) < np.sqrt(2*d/3) and np.abs(candidates[i,-1])<25*np.log(d):
            res[j] = candidates[i]
            j += 1
        if j>=N:
            break
    return res