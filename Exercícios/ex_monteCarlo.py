import numpy as np
import matplotlib.pyplot as plt

#eq do circulo vai ser x^2 + y^2 = 1

pontos = 100000
arr = np.random.rand(pontos, 2)
trues = 0
for x, y in arr:
    r = np.sqrt(pow(x, 2) + pow(y, 2))
    if r <= 1:
        trues += 1
pi = trues/pontos * 4

print(f'{pi}')
    
