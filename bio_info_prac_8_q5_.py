# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 05:00:26 2018

@author: iumar
""i

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 21:20:38 2018

@author: iumar
"""
import numpy as np
hy={'A':13.85,'D':11.61,'C':15.37,'E':11.38,'F':13.93,'G':13.34,'H':13.82,'I':15.28,'i':11.58,'L':14.13,
'M':13.86,'N':13.02,'P':12.35,'Q':12.61,'R':13.10,'S':13.39,'T':12.70,'V':14.56,'W':15.48,'Y':13.88}
s_id = []
f=open('Q1.fasta')
for line in f.readlines():
	if line[0] == '>':
		pass
	else:
		s_id.append(line.strip())
def alpha_sheet(s_id):		
    for s_ in s_id:
        print('sequences :-',s_)        
        z=[]
        for t in range(len(s_)):           
            z.append(hy[s_[t]])
        av_s=np.mean(z)
        for i in range(0,len(s_)):
            #for i in range(i,i+8):           
                if (i+7<len(s_) and (hy[s_[i]]>av_s and hy[s_[i+1]]>av_s and hy[s_[i+2]]<av_s and hy[s_[i+3]]<av_s and hy[s_[i+4]]>av_s and hy[s_[i+5]]>av_s and hy[s_[i+6]]<av_s and hy[s_[i+7]]<av_s)):                    
                    print ('from_condition _1','interval from',i,'-',i+8,'alpha_hlix',s_[i:i+8],abs(((hy[s_[i]]+hy[s_[i+1]]+hy[s_[i]]+hy[s_[i+5]]+hy[s_[i+4]])-(hy[s_[i+1]]+hy[s_[i+2]]+hy[s_[i+6]]+hy[s_[i+7]]))/len(s_)))
                if (i+7<len(s_) and (hy[s_[i]]<av_s and hy[s_[i+1]]<av_s and hy[s_[i+2]]>av_s and hy[s_[i+3]]>av_s and hy[s_[i+4]]<av_s and hy[s_[i+5]]<av_s and hy[s_[i+6]]>av_s and hy[s_[i+7]]>av_s)):                    
                    print ('from_condition _2','interval from',i,'-',i+8,'alpha_hlix',s_[i:i+8],abs(((hy[s_[i]]+hy[s_[i+1]]+hy[s_[i]]+hy[s_[i+5]]+hy[s_[i+4]])-(hy[s_[i+1]]+hy[s_[i+2]]+hy[s_[i+6]]+hy[s_[i+7]]))/len(s_)))
                if (i+7<len(s_) and (hy[s_[i]]>av_s and hy[s_[i+1]]<av_s and hy[s_[i+2]]<av_s and hy[s_[i+3]]>av_s and hy[s_[i+4]]>av_s and hy[s_[i+5]]<av_s and hy[s_[i+6]]<av_s and hy[s_[i+7]]>av_s)):                    
                    print ('from_condition _3','interval from',i,'-',i+8,'alpha_hlix',s_[i:i+8],abs(((hy[s_[i]]+hy[s_[i+1]]+hy[s_[i]]+hy[s_[i+5]]+hy[s_[i+4]])-(hy[s_[i+1]]+hy[s_[i+2]]+hy[s_[i+6]]+hy[s_[i+7]]))/len(s_)))
                if (i+7<len(s_) and (hy[s_[i]]<av_s and hy[s_[i+1]]<av_s and hy[s_[i+2]]>av_s and hy[s_[i+3]]<av_s and hy[s_[i+4]]<av_s and hy[s_[i+5]]>av_s and hy[s_[i+6]]<av_s and hy[s_[i+7]]<av_s)):                    
                    print ('from_condition _4','interval from',i,'-',i+8,'alpha_hlix',s_[i:i+8],abs(((hy[s_[i]]+hy[s_[i+1]]+hy[s_[i]]+hy[s_[i+5]]+hy[s_[i+4]])-(hy[s_[i+1]]+hy[s_[i+2]]+hy[s_[i+6]]+hy[s_[i+7]]))/len(s_)))
def beta_sheet(s__id):		
    for s_ in s__id:
        print('s_:-',s_)          
        y=[]
        for i in range(len(s_)):           
            y.append(hy[s_[i]])
        av_s=np.mean(y)                  
        for i in range(0,len(s_)-6,6):
            for i in range(i,i+6):                
                if (i+5<len(s_) and hy[s_[i]]>av_s and hy[s_[i+1]]<av_s and hy[s_[i+2]]>av_s and hy[s_[i+3]]<av_s and hy[s_[i+4]]>av_s and hy[s_[i+5]]<av_s) :
                        print ('interval from',i,'-',i+6,'beta_sheet',s_[i:i+6],abs(((hy[s_[i]]+hy[s_[i+2]]+hy[s_[i+2]])-(hy[s_[i+1]]+hy[s_[i+3]]+hy[s_[i+5]]))/len(s_)))
                if  (hy[s_[i]]<av_s and hy[s_[i+1]]>av_s and hy[s_[i+2]]<av_s and hy[s_[i+3]]>av_s and hy[s_[i+4]]<av_s and hy[s_[i+5]]>av_s):
                        print ('interval from',i,'-',i+6,'beta_sheet',s_[i:i+6],abs(((hy[s_[i]]+hy[s_[i+2]]+hy[s_[i+2]])-(hy[s_[i+1]]+hy[s_[i+3]]+hy[s_[i+5]]))/len(s_)))
beta_sheet(s_id)
alpha_sheet(s_id)