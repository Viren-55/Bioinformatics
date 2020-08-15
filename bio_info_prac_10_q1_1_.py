# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:20:41 2018

@author: kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 05:00:26 2018

@author: kumar
"""

A='LGASGIAAFAFGSTAILIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQYGMGIPPLHDGGWWLMAGLFMTLSLGSWWIRVYSRARALGLGTHIAWNFAAAIFFVLCIGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCPWHGFSIGFAYGCGLLFAAHGATILAVARFGGDREIEQITDRGTAVERAALFW'
B='XHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHXXHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXX'
z='ACDEFGHIKLMNPQRSTWYV'
#count_1=0
def propers(X):        
        t=B.count('H')#counting_number_of_helix_in_given_seq
        r=t/len(B)#percentage_of_helix_in_seq
        for i in X:
            u=A.count(i)
            g=0
            for j in range(len(A)):
                if A[j]==i and B[j]=='H':#countiing_number_of_helix_of_partcular_amino_acid
                    g+=1                                                              
            pros=g/u#percentage_of_partcular_amino_acid_helix_form_
            propensity=pros/r#propenity_calculation
            print('propensity_amino_acid',i,'in_given_seq:-',propensity)
print(propers(z))