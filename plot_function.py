import os
import numpy as np
import matplotlib.pyplot as plt

colors = plt.cm.coolwarm(np.linspace(0,1,17))
color_map = {0.10: colors[0],
             0.20: colors[1],
             0.33: colors[2],
             0.35: colors[2],
             0.40: colors[3],
             0.50: colors[4],
             0.65: colors[-6],
             0.66: colors[-6],
             0.75: colors[-5],
             0.80: colors[-4],
             1.00: colors[-3],
             1.25: colors[-2],
             1.50: colors[-1]}
linewidth = 2
markersize = 7.5
markers = ['^', 'X', 'd', 'P', 'v']


def plot_accept_rate(accept_rate, ds, dpowers, title, xlabel, ylim):
    """
    Function for plotting the acceptance rate
    :param accept_rate:   acceptance rate
    :param ds:            list of dimensions or condition numbers
    :param dpowers:       list of powers (gamma)
    :param title:         title of the plot
    :param xlabal:        label of the x axis
    """
    markers = ['^', 'X', 'd', 'P', 'v']

    plt.figure(figsize=(6,4))

    for j, dpower in enumerate(dpowers):
        if dpower != 1:
            plt.semilogx(ds[0:accept_rate.shape[0]], accept_rate[:,j], "o:", alpha = 1., linewidth=linewidth,
                         label=r'$\gamma = %0.2f$' %(dpower), marker = markers[j], markersize=markersize,
                         color = color_map[dpower])
        else:
            plt.semilogx(ds[0:accept_rate.shape[0]], accept_rate[:,j], "o-", alpha = 1., linewidth=linewidth,
                         label=r'$\gamma = %0.2f$' %(dpower), marker = markers[j], markersize=markersize,
                         color = color_map[dpower])

    plt.xlabel(xlabel)#"Dimension $d$"
    plt.ylabel("Acceptance rate")
    plt.ylim(-0.05, 1.05)
    plt.legend(bbox_to_anchor=(1, 0.45),loc='center right',prop={"size":8},markerscale=0.5)

    plt.tight_layout()
    plt.savefig(os.path.join('./results', title), dpi=300)




def plot_mixing_time(mixing_time, ds, dpowers, title, xlabel, ylim):
    """
    Function for plotting the mixing time
    :param mixing_time:   mixing time
    :param ds:            list of dimensions or condition numbers
    :param dpowers:       list of powers (gamma)
    :param title:         title of the plot
    :param xlabal:        label of the x axis
    :param ylim:          limit of y axis
    """


    plt.figure(figsize=(6,4))
    for j, dpower in enumerate(dpowers):
        if dpower != 1:
            plt.plot(ds[:], mixing_time[:,j], "o:", alpha = 1., linewidth=linewidth,
                     label=r'$\gamma = %0.2f$' %(dpower), marker = markers[j], markersize=markersize,
                     color = color_map[dpower])
        else:
            plt.plot(ds[:], mixing_time[:,j], "o-", alpha = 1., linewidth=linewidth,
                     label=r'$\gamma = %0.2f$' %(dpower), marker = markers[j], markersize=markersize,
                     color = color_map[dpower])
    plt.xlabel(xlabel)
    plt.ylabel("Mixing time")
    plt.ylim(0,ylim)
    plt.legend(bbox_to_anchor=(1, 0.2),loc='center right',prop={"size":8},markerscale=0.5)

    plt.tight_layout()
    plt.savefig(os.path.join('./results', title), dpi=300)
    plt.show()


