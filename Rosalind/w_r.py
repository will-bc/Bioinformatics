# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:34:33 2017

@author: Willian
"""

#Rosalind - reading and writing
#
## Problem:
#
#Given:A file containing at most 1000 lines.
#Return:A file containing all the even-numbered lines from the original file. 
# Assume 1-based numbering of lines.

f= open('rosalind_ini5.txt', 'r')


s=[]
Gpoint=[]
c=0

s=f.readlines()

print (s)

for i in s:
    Gpoint=Gpoint+ i.splitlines()
    
f.close()
o=open('out.txt', 'w')
    
for i in (Gpoint):
 
    c=c+1
    
    if c%2==0:
        o.write(str(i)+'\n')

o.close()    
        
