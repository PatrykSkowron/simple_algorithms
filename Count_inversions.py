# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
# Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.

def CountSplit(B,C):
	nb = len(B)
	nc = len(C)
	arr=[]
	iB=0
	iC=0
	inv=0
	# print("#### SPLIT INVERSION (n=%d)#####" % (nb+nc))
	# print("B: ",B)
	# print("C: ",C)
	if not(len(B)==0) and not(len(C)==0):
		for k in range(nb+nc):
			try:
				if B[iB] < C[iC]:
					arr.append(B[iB])
					iB+=1		
				else:
					arr.append(C[iC])
					iC+=1
					inv+=(nb-iB)
			except IndexError as x:
				if iB <= nb-1:
					arr.append(B[iB])
					iB+=1
				else:
					arr.append(C[iC])
					iC+=1
					inv+=(nb-iB)
			# print("Arr: ",arr,"Inv: ",inv)
		B.pop()
		C.pop()
	# print("END OF SPLIT INVERSION, number of split inversions: %s" % inv)
	return inv

def CountInv(A):
	
	n = len(A)
	if n > 1:
		if n % 2 == 0: split = int(n/2)
		else: split = int((n+1)/2)
		B = A[:split]
		C = A[split:]
		# print("B: ",B,"C: ",C)
		x = CountInv(B)
		y = CountInv(C)
		B.sort()
		C.sort()
		# print("after CountInv: ","B: ",B,"C: ",C,"x,y: ",x,y)
		z = CountSplit(B,C) #  B , C sorted!
		return x+y+z
	else:
		return 0

from time import time
def log_time(function,*args,**kwargs):
	start = time()
	ret = function(*args,**kwargs)
	end = time()
	return([end-start,ret])