
import math

f = open('fullmoon.txt')
##f = open('outlier.txt')
f = f.read()
f = f.split('\n')
X = []
eps = float(input('Enter a value of eps :'))
np = int(input('Enter no. of points  :'))
for i in range(len(f)-1):
        p = f[i].split(',')
        X.append((float(p[0]),float(p[1])))


def core1(X):
        core = []
        for i in range(len(X)):
                x = X[i]
                test = []
                
                for j in range((len(X))):
                    
                    d = 0
                    y = X[j]
                    d = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
                    if d <= eps :
                        test.append(y)

                        if len(test)>= np:
                            if x not in core:
                              core.append(x)

        return core
core = []

core = core1(X)
print(len(core))
def boun(X,core):
        boundary  = []
        
        for i in range(len(X)):
             x = X[i]


             for k in range((len(X))):
                    
                    d = 0
                    z = X[k]
                    d = math.sqrt((x[0]-z[0])**2 + (x[1]-z[1])**2)
                    if d<=eps and z in core  and x not in boundary and x not in core:
                         boundary.append(x)
                         
        return boundary
                 
boundary = []
boundary = boun(X,core)
print(len(boundary))


corex=[]
corey=[]

for i in core:
        corex.append(i[0])
        corey.append(i[1])
bx=[]
by=[]
for i in boundary:
        bx.append(i[0])
        by.append(i[1])
nx=[]
ny=[]
noise = []
for i in range(len(X)):
             x = X[i]
             if x not in core and x not in boundary:
                noise.append(x)
        
print(len(noise))
for i in noise:
       nx.append(i[0])
       ny.append(i[1])

import matplotlib.pyplot as plt
plt.plot(corex,corey, 'ro')
plt.plot(bx,by, 'mo')
plt.plot(nx,ny, 'bo')

plt.show()
