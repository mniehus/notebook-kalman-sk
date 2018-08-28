import pylab as plt
from matplotlib.patches import Ellipse
from numpy import sqrt, arctan, pi, arange, dot, array
from numpy.linalg import eigh
from numpy.random import randn


def cov_ellipse(fig, m, S, ec='r', fc='y', fill=True, alpha=0.3, vector=False):
    '''
    Plot covariance ellipse
    
    m      - means - array [m0, m1]
    S      - covariance - matrix [[s00, s01],[s10, s11]]
    ec     - line color
    fc     - fill color
    fill   - fill ellipse, boolean
    vector - draw main vectors
    '''
    [e1, e2],[v1 ,v2] = eigh(S)         # vlastne vektory a vlastne hodnoty
    
    w=2*sqrt(e1*9.21)                   # vypocet parametrov elipsy
    h=2*sqrt(e2*9.21)
    phi=arctan(v1[1] / v1[0])*180/pi    # uhol natocenia 

    #fig = plt.figure(0)                 # konfiguracia kreslenia
    ax = fig.add_subplot(111) 
    ellipse = Ellipse(xy=(m[0],m[1]), width=w, height=h, 
                      angle=phi, edgecolor=ec, facecolor=fc, 
                      lw=1, alpha=alpha, fill=fill)
    ax.add_artist(ellipse)              # vykreslenie elipsy
    
    if vector:                          # vykreslenie skalovanych vlastnych vektorov
        plt.plot([0, v1[0]*w/2] + m[0],[0, v1[1]*w/2] + m[1], color=ec)  
        plt.plot([0, v2[0]*h/2] + m[0],[0, v2[1]*h/2] + m[1], color=ec)
        
        
        

def motionData(t, f, std = [0.02, 0.02, 0.05], m=100., dt=0.1):
 
    x=[0., 0., 0.]              # state vector [s, v, a]  
      
    F=[[1.0,  dt, dt*dt/2],
       [0.0, 1.0,      dt],
       [0.0, 0.0,     0.0]]     # ! F[3,3] - control value   
        
    u=[0.0]                     # control vector    
    
    G=[[0.0],                   # control matrix
       [0.0],
       [1./m]]                  # substitute for F[3,3] 
             
    H=[[1.0, 0.0, 0.0],
       [0.0, 1.0, 0.0],
       [0.0, 0.0, 1.0]]
    
    zr = [] 
    xr = []                # return values

    for i in range(len(t)):
        u=[f[i]]
        for j in arange(0, t[i], dt):
            z = dot(H,x) + std*randn(3)    # x(k)
            zr.append(z)
            xr.append(x)
            x = dot(F, x) + dot(G,u)       # x(k+1)

    return array(zr), array(xr), arange(0, sum(t),dt)
