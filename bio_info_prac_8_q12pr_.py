# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:10:06 2018

@author: kumar
"""

import matplotlib.pyplot as plt

hgm = {}

with open('Hydrophobicity.dat') as f:
	for line in f.readlines():
		line = line.split()
		j = 0
		while j<len(line)-1:
			hgm[line[j][0]] = line[j+1]
			j +=2

seq = ''
with open('Q2.fasta') as f:
	for lines in f.readlines():
		if lines[0] == '>':
			seq_name = lines[1:]
		else:
			seq += lines.strip()
print(seq)

window = [9, 19]
for w in window:
	y = []
	for i in range(len(seq)-w+1):
		avg_h = 0
		c = i
		while c < i+w:
			ch = seq[c]
			avg_h += float(hgm[ch])
			c += 1
		avg_h /= w
		y.append(avg_h)
	ave = sum(y)/len(y)
	fig = plt.figure(figsize = (10,5))
	plt.plot([i for i in range(1, len(seq)-w+2)], y)
	plt.plot([i for i in range(1, len(seq)-w+2)], [ave for i in range(1, len(seq)-w+2)], color = 'r')
	plt.show()

