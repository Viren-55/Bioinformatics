# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 03:02:55 2018

@author: kumar
"""
import matplotlib.pyplot as plt
import numpy as np

dict_hydro={'A':13.85,'D':11.61,'C':15.37,'E':11.38,'F':13.93,'G':13.34,'H':13.82,'I':15.28,'K':11.58,'L':14.13,
'M':13.86,'N':13.02,'P':12.35,'Q':12.61,'R':13.10,'S':13.39,'T':12.70,'V':14.56,'W':15.48,'Y':13.88}

seq_id=''
f=open('Q2.fasta')
for lines in f.readlines():
		if lines[0] == '>':
			pass
		else:
			seq_id+= lines.strip()
def window_slide(window_size):
    w = []
    z=[]   
    for i in range(len(seq_id)-window_size+1):
         k=0
         while k+i<i+ window_size:
            j = seq_id[k+i]
            z.append(float(dict_hydro[j]))
            k += 1
         avg_hydro=np.mean(z)         
         w.append(avg_hydro)       
         z=[]
    avg = np.mean(w)      
    plt.plot([i for i in range(1, len(seq_id)-window_size+2)], w)
    plt.plot([i for i in range(1, len(seq_id)-window_size+2)], [avg for i in range(1, len(seq_id)-window_size+2)], color = 'g')
    plt.show()
print( window_slide(19))
print( window_slide(9))

