from QuickSort import *

def RSelect(list,i):
	n = len(list)
	if n<2: 
		try:
			return list[0]
		except IndexError:
			return None
	else:
		pi = choosePivot(list)
		p = list[pi]
		lpart,j = Partition(list,pi)
		if j==i: return p
		elif j>i: return RSelect(lpart[:j-1],i)
		else: return RSelect(lpart[j:],i-j)