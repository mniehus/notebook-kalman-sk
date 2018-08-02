import pylab as plt
from matplotlib.patches import Ellipse
from numpy import sqrt, arctan, pi
from numpy.linalg import eigh


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
