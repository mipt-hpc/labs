import sys

dt=float(sys.argv[1])                  #timestep for integration
nsteps=int(sys.argv[2])            #total number of integr steps

class Spring():         #spring F=k*dx
    def __init__(self,k,dx):
        self.k = k
        self.dx = dx


class Particle():       #particle with mass m, position coord=[x,y,z] and velocity vel = [v_x,v_y,v_z]
    def __init__(self,coord, vel,m):
        self.coord = coord
        self.vel = vel
        self.mass = m
        self.force=[0,0,0]
    def calc_KE(self):
        KE=0.5*self.mass*(self.vel[0]**2+self.vel[1]**2+self.vel[2]**2)
        return KE


class xWall_potential():
    def __init__(self,eps,sigma,position):
        self.eps=eps
        self.sigma=sigma
        self.position = position
    def get_force(self,particle):
        if particle.coord[0] < self.position+self.sigma:
            return [-self.eps*(self.position+self.sigma-particle.coord[0]),0,0]
        else:
            return [0,0,0]


def update_force(particle,potential):
    force=potential.get_force(particle)
    particle.force[0]=force[0]
    particle.force[1]=force[1]
    particle.force[2]=force[2]


def update(particle, spring):
    #x+=v*dt
    particle.coord[0] += particle.vel[0]*dt
    particle.coord[1] += particle.vel[1]*dt
    particle.coord[2] += particle.vel[2]*dt
    #v-=F_spring/m*dt
    particle.vel[0]-=(spring.dx[0]*spring.k + particle.force[0])*dt/particle.mass
    particle.vel[1]-=(spring.dx[1]*spring.k + particle.force[1])*dt/particle.mass
    particle.vel[2]-=(spring.dx[2]*spring.k + particle.force[2])*dt/particle.mass
    #dx+=v*dt
    spring.dx[0]+=particle.vel[0]*dt
    spring.dx[1]+=particle.vel[1]*dt
    spring.dx[2]+=particle.vel[2]*dt


pp1=Particle(coord=[2,0,0],vel=[-3,3,0],m=1)
sp1=Spring(k=1,dx=[2,0,0])
Wall=xWall_potential(eps=10,sigma=1,position=-1)

for i in range(nsteps):
    update_force(pp1,Wall)
    update(pp1,sp1)
    print i, pp1.coord[0],pp1.coord[1],pp1.coord[2]
