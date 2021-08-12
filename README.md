## MALA_code

Code for the paper "Minimax mixing time of MALA". 

Run ```python MALA_only.py``` with the following four flags:

```
-target        Target is the perturbed Gaussian or the original Gaussian',     Either 'perturbed' or 'original'.
-init          Warm or bad (feasible) initialization.                          Either 'warm' or 'bad'.
-dependency    Dimension dependency or condition number dependency.            Either 'dimension' or 'condition'.
-plot          Plot acceptance rate or mixing time.                            Either 'acc' or 'mix'.
```

Run ```python ULA_MALA.py``` for experiments on ULA+MALA.