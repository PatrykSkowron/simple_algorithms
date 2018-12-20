# QuickSort algorithm as fast O(n log n) algorithm with swapping in-place (low memory usage)

from time import time
from random import randint

def log_time(function,*args,**kwargs):
	start = time()
	ret = function(*args,**kwargs)
	end = time()
	return([end-start,ret])

def swap(list,i,j): # swaps elemnents i and j in non-zero list and returns that list
	if i<j: return list[:i] + list[j:j+1] + list[i+1:j] + list[i:i+1] + list[j+1:]
	elif j<i: return list[:j] + list[i:i+1] + list[j+1:i] + list[j:j+1] + list[i+1:]
	else: return list

def choosePivot(list): # returns index of chosen pivot
	return randint(0,len(list)-1)

def Partition(list,pi=0): # partition list around pivot with index pi
	list = swap(list,0,pi)
	# print("PARTITION: ",list[0])
	# print("INITIAL LIST: ",list)
	i = 1
	for j in range(1,len(list)):
		# print("J=",j)
		if list[j]< list[0]:
			# print("SWAPPING %d <-> %d " % (list[i],list[j]))
			list = swap(list,i,j)
			i+=1
			# print("--> list: ",list)
			
	list = swap(list,0,i-1)
	return (list,i)
		
def QuickSort(list): # QuickSort algorithm
	n=len(list)
	
	# print("QUICKSORT LIST: ",list)
	if n<2: return list
	else:
		pi = choosePivot(list)
		p = list[pi]
		lpart,i = Partition(list,pi)
		L = QuickSort(lpart[:i-1])
		R = QuickSort(lpart[i:])
		# print(lpart,L,R)
		return L+[p]+R
