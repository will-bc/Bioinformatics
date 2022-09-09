# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:02:43 2017

@author: Willian
"""

#Rosalind - COnditions and loops
#
## Problem:
#
#Given:Two positive integers aa and bb (a<b<10000a<b<10000).
#Return:The sum of all odd integers from aa through bb, inclusively.

a= 4696

b= 9035

R=0

for i in range (a,b+1):
   if i%2==1:
       R=R+i
         
        
print (R)