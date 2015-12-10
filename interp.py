from scipy.misc import derivative
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = np.array([3.0, -4.0, -2.0, -1.0, 3.0, 6.0, 10.0, 8.0, 12.0, 20.0])
f = interp1d(x, y, kind = 'cubic')
xint = np.arange(0, 9.01, 0.01)
yint = f(xint)
z=np.arange(1,8,0.1)
first = derivative(f,z,dx=0.1,n=1)
fig, ax = plt.subplots(2,1,sharex = True)

ax[0].plot(x,f(x))
ax[0].plot(xint,yint)
ax[0].set_ylabel(r'$f(x)$')
ax[1].plot(z,first)
ax[1].set_ylabel(r'$f\/\prime(x)$')
#plt.plot(x, y, 'o', c = 'b')
#plt.plot(xint, yint, '-r')
plt.show()
