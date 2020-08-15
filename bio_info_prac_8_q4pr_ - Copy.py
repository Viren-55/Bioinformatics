# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:44:21 2018

@author: kumar
"""
import re
pattern_s= ['STV[IL]{2}[^DERK]', '[FILV]Q[A-Z]{3}[RK]G[A-Z]{3}[RK][A-Z]{2}[FILVWY]']

def pattern_matcher(X):
    for i in X:
      print('Current Pattern is : ', i)
    f=open('Q4.fasta')
    for j in f:
        if j[0] == '>':
            seq_id = j[1:]
        for match in re.finditer(i, j):
            print(seq_id, match.group(), match.start())
    print('\n')

print(pattern_matcher(pattern_s))