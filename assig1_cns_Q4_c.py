import matplotlib.pyplot as plt
dt= 0.0001
V1= 0
I= -9
V_reset = 4
V_threshold=20
V=[]
T=[]

for t in range(100000):
    V1 = V1 + dt*(I + (V1**2) )
    if V1 > V_threshold:
        V1 = V_reset
    V.append(V1)
    T.append(t*dt)
plt.plot(T,V)
plt.show()
