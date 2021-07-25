import numpy as np
from MALA import mala

def f_perturbed(x, L, m, delta=1./40):
    """
    Negative log density of the perturbed Gaussian distribution in the paper
    :param x:       location
    :param L:       L in the perturbed Gaussian
    :param m:       m in the perturbed Gaussian
    :param delta:   delta in the perturbed Gaussian
    :return:        density value at x
    """
    d = x.shape[1]
    return 0.5*L*np.sum(x[:,:-1]**2, axis=1) - \
           0.5/((d-1)**(0.5-2*delta)) * np.sum(np.cos((d-1)**(0.25-delta)*(L**0.5)*x[:,:-1]), axis=1) + \
           0.5*m*x[:,-1]**2

def grad_f_perturbed(x, L, m, delta=1./40):
    """
    Gradient of the negative log density of the perturbed Gaussian distribution
    :param x:       location
    :param delta:   delta in the perturbed Gaussian
    :param L:       L in the perturbed Gaussian
    :param m:       m in the perturbed Gaussian
    :return:        gradient value at x
    """
    d = x.shape[1]
    grad = x.copy()
    grad[:,:-1] = L*x[:,:-1] + \
                  0.5*(L**0.5)/((d-1)**(0.25-delta)) * np.sin((d-1)**(0.25-delta)*(L**0.5)*x[:,:-1])
    grad[:,-1] = m*x[:,-1]
    return grad



def f_gaussian(x, L, m):
    """
    Negative log density of the Gaussian distribution considered in the paper
    :param x:       location
    :param L:       L in the Gaussian
    :param m:       m in the Gaussian
    :return:        density value at x
    """
    return 0.5*L*np.sum(x[:,:-1]**2, axis=1) + 0.5*m*x[:,-1]**2



def grad_f_gaussian(x, L, m):
    """
    Gradient of the negative log density of the Gaussian distribution considered in the paper
    :param x:       location
    :param L:       L in the Gaussian
    :param m:       m in the Gaussian
    :return:        density value at x
    """
    grad = x.copy()
    grad[:,:-1] = L*x[:,:-1]
    grad[:,-1] = m*x[:,-1]
    return grad
