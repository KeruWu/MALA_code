import numpy as np

ds_dict = {('perturbed', 'dimension', 'warm', 'acc') : 2**np.arange(1, 23, 3),
           ('perturbed', 'dimension', 'warm', 'mix') : np.array([2, 512, 1024, 2048, 4096]),
           ('perturbed', 'dimension', 'bad',  'acc') : 2**np.arange(5, 16),
           ('perturbed', 'dimension', 'bad',  'mix') : np.array([32, 64, 96, 128, 192, 256, 384, 512, 784]),
           ('perturbed', 'condition', 'warm', 'acc') : np.array([2, 4, 8, 16, 32, 64, 96]),
           ('perturbed', 'condition', 'warm', 'mix') : np.array([2, 4, 8, 16, 32, 64, 96]),

           ('gaussian',  'dimension', 'warm', 'acc') : 2**np.arange(1, 12),
           ('gaussian',  'dimension', 'warm', 'mix') : 2**np.arange(1, 11),
           ('gaussian',  'dimension', 'bad',  'acc') : np.array([2, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]),
           ('gaussian',  'dimension', 'bad',  'mix') : np.array([2, 32, 64, 128, 256, 512, 1024, 2048, 4096]),
           ('gaussian',  'condition', 'warm', 'acc') : np.array([2, 4, 8, 16, 32, 64, 96]),
           ('gaussian',  'condition', 'warm', 'mix') : np.array([2, 4, 8, 16, 32, 64, 96])}

dpowers_dict = {('perturbed', 'dimension', 'warm', 'acc') : np.array([0.20, 0.35, 0.50, 0.65, 0.80]),
                ('perturbed', 'dimension', 'warm', 'mix') : np.array([0.20, 0.35, 0.50, 0.65, 0.80]),
                ('perturbed', 'dimension', 'bad',  'acc') : np.array([0.50, 0.75, 1.00, 1.25, 1.50]),
                ('perturbed', 'dimension', 'bad',  'mix') : np.array([0.50, 0.75, 1.00, 1.25, 1.50]),
                ('perturbed', 'condition', 'warm', 'acc') : np.array([0.50, 0.75, 1.00, 1.25, 1.50]),
                ('perturbed', 'condition', 'warm', 'mix') : np.array([0.50, 0.75, 1.00, 1.25, 1.50]),

                ('gaussian',  'dimension', 'warm', 'acc') : np.array([0.10, 0.20, 0.33, 0.40, 0.50]),
                ('gaussian',  'dimension', 'warm', 'mix') : np.array([0.10, 0.20, 0.33, 0.40, 0.50]),
                ('gaussian',  'dimension', 'bad',  'acc') : np.array([0.20, 0.33, 0.50, 0.66, 0.80]),
                ('gaussian',  'dimension', 'bad',  'mix') : np.array([0.20, 0.33, 0.50, 0.66, 0.80]),
                ('gaussian',  'condition', 'warm', 'acc') : np.array([0.50, 0.75, 1.00, 1.25, 1.50]),
                ('gaussian',  'condition', 'warm', 'mix') : np.array([0.50, 0.75, 1.00, 1.25, 1.50])}

xlabel_dict = {'dimension' : "Dimension $d$",
               'condition' : "Condition Number $\kappa$"}

ylim_dict = {('perturbed', 'dimension', 'warm', 'acc') : 1.05,
             ('perturbed', 'dimension', 'warm', 'mix') : 4000,
             ('perturbed', 'dimension', 'bad',  'acc') : 1.05,
             ('perturbed', 'dimension', 'bad',  'mix') : 7500,
             ('perturbed', 'condition', 'warm', 'acc') : 1.05,
             ('perturbed', 'condition', 'warm', 'mix') : 26000,

             ('gaussian',  'dimension', 'warm', 'acc') : 1.05,
             ('gaussian',  'dimension', 'warm', 'mix') : 3200,
             ('gaussian',  'dimension', 'bad',  'acc') : 1.05,
             ('gaussian',  'dimension', 'bad',  'mix') : 10000,
             ('gaussian',  'condition', 'warm', 'acc') : 1.05,
             ('gaussian',  'condition', 'warm', 'mix') : 4000}

h_const_dict = {('perturbed', 'dimension', 'warm', 'acc') : 2.5,
                ('perturbed', 'dimension', 'warm', 'mix') : 2.5,
                ('perturbed', 'dimension', 'bad',  'acc') : 10.,
                ('perturbed', 'dimension', 'bad',  'mix') : 10.,
                ('perturbed', 'condition', 'warm', 'acc') : 2.5,
                ('perturbed', 'condition', 'warm', 'mix') : 2.5,

                ('gaussian',  'dimension', 'warm', 'acc') : 1.,
                ('gaussian',  'dimension', 'warm', 'mix') : 1.,
                ('gaussian',  'dimension', 'bad',  'acc') : 1.5,
                ('gaussian',  'dimension', 'bad',  'mix') : 1.5,
                ('gaussian',  'condition', 'warm', 'acc') : 1.,
                ('gaussian',  'condition', 'warm', 'mix') : 1.}

emph_dict = {('perturbed', 'dimension', 'warm', 'acc') : 0.5,
             ('perturbed', 'dimension', 'warm', 'mix') : 0.5,
             ('perturbed', 'dimension', 'bad',  'acc') : 1.,
             ('perturbed', 'dimension', 'bad',  'mix') : 1.,
             ('perturbed', 'condition', 'warm', 'acc') : 1.,
             ('perturbed', 'condition', 'warm', 'mix') : 1.,

             ('gaussian',  'dimension', 'warm', 'acc') : 0.33,
             ('gaussian',  'dimension', 'warm', 'mix') : 0.33,
             ('gaussian',  'dimension', 'bad',  'acc') : 0.5,
             ('gaussian',  'dimension', 'bad',  'mix') : 0.5,
             ('gaussian',  'condition', 'warm', 'acc') : 1.,
             ('gaussian',  'condition', 'warm', 'mix') : 1.}
