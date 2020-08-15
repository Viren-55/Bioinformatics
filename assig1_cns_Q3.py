import matplotlib.pyplot as plt
import numpy as np
R = 1000000
tau = 1
V_thres = 10
dt=0.00001

t1=2
V=0
Io=[]
To=[]
samples = 100000
for cur in np.arange(0,0.0002,0.000001):
    t=0
    V=0
    for i in range(samples):
        V= (cur*R*dt/tau)+(V*(1-(dt/tau)))
        t += dt 
        if V>=V_thres:
           V=0
           break 
    Io.append(cur)
    To.append(1/(t+t1))
plt.plot(Io,To)
plt.show()
