import matplotlib.pyplot as plt
R = 10**6
tau = 1
V_thres = 100
dt=0.0001
I = 0.00018
V_list = []
V=0

for i in range(100000):
    
    V= (I*R*dt/tau)+V*(1-(dt/tau))
    
    if V>=V_thres :
        V=0
    V_list.append(V)
        


plt.plot(V_list)
plt.show()
