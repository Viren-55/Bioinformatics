# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:00:21 2018

@author: kumar
"""

import matplotlib.pyplot as plt
import numpy as np
#import numpy as np
np.array(['1','2','3']).astype(np.float)
dict_hydro={'A':13.85,'D':11.61,'C':15.37,'E':11.38,'F':13.93,'G':13.34,'H':13.82,'I':15.28,'K':11.58,'L':14.13,
'M':13.86,'N':13.02,'P':12.35,'Q':12.61,'R':13.10,'S':13.39,'T':12.70,'V':14.56,'W':15.48,'Y':13.88}


seq_id = []
f=open('Q1.fasta')
for line in f.readlines():
	if line[0] == '>':
		pass
	else:
		seq_id.append(line.strip())
def alpha_beta_hydro(X):
    for i in X:
       
        z = []
        
        for j in i:
            dict_val = float(dict_hydro[j])
            z.append(dict_val)
        plt.plot([k for k in range(1, len(i)+1)], z)
        X_avg=np.mean(z)
        plt.plot([k for k in range(1, len(i)+1)], [X_avg for k in range(1, len(i)+1)], color = 'g')
        plt.show()
           
print(alpha_beta_hydro(seq_id))	         
