import numpy as np

inlist= [23]
outlist=[]

for i in range(0,len(inlist)):

	f=np.arange(1,(inlist[i]+2),1)
	
	for ii in range(0,inlist[i]+1):
		
		if ii == 0:
			f[ii]=0

		if ii==1:
			f[ii]= 1

		if ii>1:
			
			f[ii]= f[ii-1]+f[ii-2]
			
	outlist.append(f[inlist[i]])

print (outlist)



