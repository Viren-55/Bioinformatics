# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 05:00:26 2018

@author: kumar
"""

A='LGASGIAAFAFGSTAILIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQYGMGIPPLHDGGWWLMAGLFMTLSLGSWWIRVYSRARALGLGTHIAWNFAAAIFFVLCIGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCPWHGFSIGFAYGCGLLFAAHGATILAVARFGGDREIEQITDRGTAVERAALFW'
B='XHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHXXHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXX'
z='ACDEFGHIKLMNPQRSTWYV'#string of  amino  acid 

def propers(z,seq,seq_helix):          
        for i in z:
            u=seq.count(i)#counting number of partcular amino acid present 
            g=0
            for j in range(len(seq)):
                if seq[j]==i and seq_helix[j]=='H':
                    g+=1                             
            pros=g/u
            print(pros,i)
print(propers(z,A,B))#calling function
