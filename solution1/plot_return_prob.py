import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import tikzplotlib

N = 58
ns = np.arange(2, N, 2)

probs = []
for i, n in enumerate(ns):
    bin_coeff = scipy.special.binom(n, n//2)
    prob = (bin_coeff*1/2**n)**2
    probs.append(prob)

plt.loglog(ns, probs, 'x', label='$p(0,0|N)$')

# Also plot the asymptotic behavior
xs = np.linspace(2, N, 50)
ys = 2/(np.pi * xs)
plt.loglog(xs, ys, '--', label='$2/(\pi N)$')

plt.xlabel('$N$')
plt.ylabel('$p(0, 0|N)$')
plt.legend()
tikzplotlib.save('Asymptotic.tex')
plt.show()
