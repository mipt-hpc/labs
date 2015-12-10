from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.exp(-x)*np.sin(x)
x = np.arange(0,10, 0.1)
first = derivative(f,x,dx=1,n=1)
second = derivative(f,x,dx=1,n=2)
fig, ax = plt.subplots(3,1,sharex = True)

ax[0].plot(x,f(x))
ax[0].set_ylabel(r'$f(x)$')
ax[1].plot(x,first)
ax[1].set_ylabel(r'$f\/\prime(x)$')
ax[2].plot(x,second)
ax[2].set_ylabel(r'$f\/\prime\prime(x)$')
ax[2].set_xlabel(r'$x$')

plt.show()
