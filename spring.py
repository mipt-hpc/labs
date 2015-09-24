#import matplotlib.pyplot as plt
#import mpl_toolkits.mplot3d.axes3d as p3
#import matplotlib.animation as animation
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
    def calc_KE(self):
        KE=0.5*self.mass*(self.vel[0]**2+self.vel[1]**2+self.vel[2]**2)
        return KE

def update(particle, spring):
    #x+=v*dt
    particle.coord[0] += particle.vel[0]*dt
    particle.coord[1] += particle.vel[1]*dt
    particle.coord[2] += particle.vel[2]*dt
    #v-=F_spring/m*dt
    particle.vel[0]-=spring.dx[0]*spring.k*dt/particle.mass
    particle.vel[1]-=spring.dx[1]*spring.k*dt/particle.mass
    particle.vel[2]-=spring.dx[2]*spring.k*dt/particle.mass
    #dx+=v*dt
    spring.dx[0]+=particle.vel[0]*dt
    spring.dx[1]+=particle.vel[1]*dt
    spring.dx[2]+=particle.vel[2]*dt

def update_verlet(particle, spring):

    prev_coord_store=particle.coord[:]
    #x+=v*dt+1/2*a*dt**2 
    particle.coord[0] += particle.vel[0]*dt - 0.5*spring.k*particle.coord[0]/particle.mass*dt**2
    particle.coord[1] += particle.vel[1]*dt - 0.5*spring.k*particle.coord[1]/particle.mass*dt**2
    particle.coord[2] += particle.vel[2]*dt - 0.5*spring.k*particle.coord[2]/particle.mass*dt**2

    particle.coord_prev=prev_coord_store
    #v+=1/2*(a + a_prev)*dt
    particle.vel[0]+=-0.5*(spring.k*particle.coord[0]/particle.mass + spring.k*particle.coord_prev[0]/particle.mass)*dt
    particle.vel[1]+=-0.5*(spring.k*particle.coord[1]/particle.mass + spring.k*particle.coord_prev[1]/particle.mass)*dt
    particle.vel[2]+=-0.5*(spring.k*particle.coord[2]/particle.mass + spring.k*particle.coord_prev[2]/particle.mass)*dt

    spring.dx=particle.coord

#data_anim=[]
pp1=Particle([2,0,0],[-3,3,0],1)
sp1=Spring(1,[2,0,0])

for i in range(nsteps):
    update(pp1,sp1)
    print i, pp1.coord[0],pp1.coord[1],pp1.coord[2]
#    data_anim.append([[pp1.coord[0],pp1.coord[1],pp1.coord[2]]])



#def plot_update(data):
#    ax.clear()
#    ax.set_xlim3d([-4, 4])
#    ax.set_ylim3d([-4, 4])
#    ax.set_zlim3d([-2, 2])
#    img=[ax.scatter3D(0,0,0,c='red',s=100)]
#    for i in range(len(data)):
#        img.append(ax.scatter3D(data[i][0],data[i][1],data[i][2],c='yellow',s=100))
#    return img

#fig = plt.figure()
#ax = p3.Axes3D(fig)
#line_ani = animation.FuncAnimation(fig, plot_update,data_anim,interval=15, blit=False)
#plt.show()

