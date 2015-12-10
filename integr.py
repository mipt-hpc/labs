import scipy.integrate as integrate
from math import pi,sin,exp

f = lambda x : exp(-x**2)
I = integrate.quad(f, -float('inf'), float('inf'))

# limits for radius
r1 = 0.
r2 = 1.
# limits for theta
t1 = 0
t2 = 2*pi
# limits for phi
p1 = 0
p2 = pi

def diff_volume(p,t,r):
    return r**2*sin(p)

volume = integrate.tplquad(diff_volume, r1, r2, lambda r:   t1, lambda r:   t2, lambda r,t: p1, lambda r,t: p2)

