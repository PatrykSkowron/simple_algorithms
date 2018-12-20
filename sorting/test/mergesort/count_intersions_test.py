from Count_inversions import *
Input=[]
c=0

# FILE CONTAINING 10E6 distinct integers from <0,99999> . Source: https://www.coursera.org/learn/algorithms-divide-conquer
file='C:\kursy\Algorithms1_coursera\Array_week2.txt'
with open(file) as f:
	for line in f.readlines():
		Input.append(line)


A = [3,2,1,5,8,6,7,4]
print(log_time(CountInv,A))

print(CountSplit([3],[2]))
print(CountSplit([3,5],[2,1]))
print(CountSplit([3,5,6],[2,1,4]))
print(CountSplit([3,5,6],[1]))
print(CountSplit([3,5,6],[]))
print(CountInv([]))

print(CountInv(Input))


# checking if Algorithm complexity is O(n log n)
from random import sample
import numpy as np
import matplotlib.pyplot as plt
arr =[]
t = []
for k in range(5):
	tmp=[]
	t.extend([f*10**k for f in [0.25,0.5,0.75,1.0]])
	for s in range(0,10):
		input = sample(range(10**k),10**k)
		tmp.append(log_time(CountInv,input))
	arr.append([10**k,list(map(np.mean, zip(*tmp)))[0],list(map(np.mean, zip(*tmp)))[1]])

arr = list(map(list,zip(*arr)))
arr2=arr[:2]
arr3=arr.copy()
arr3.pop(1)

const = np.mean(t*np.log(t)*[0.05]*len(t))/np.mean(arr2[1])

plt.subplot(211)
plt.plot(*arr2, 'ro')
plt.loglog(t,t*np.log(t)*[1./const]*len(t))

plt.subplot(212)
plt.plot(*arr3, 'ro')
plt.loglog()
plt.show()
