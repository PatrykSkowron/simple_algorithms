from RandomizedSelection import *
import unittest
from random import *
import numpy as np

class Test(unittest.TestCase):
	
	def _testing(self,A):
		
		Bt,B = log_time(np.median,A)
		At,ith = log_time(RSelect,A,int(len(A)/2))
		if len(A)>0:
			print("OK!\nlength: %d \n ith element: %d\nAlgorithm time: %.5f seconds. \nBuilt in time: %.5f seconds." % (len(A),ith,At,Bt))
		
	def testSimple(self):
		A = [5,2,4,1,7,0,6,10]
		self._testing(A)
	
	def testOneItem(self):
		A = [5]
		self._testing(A)
		
	def testEmpty(self):
		A = []
		self._testing(A)
		
	def testLargeInput(self):
		# FILE CONTAINING 10000 distinct integers from <0,10000) . Source: https://www.coursera.org/learn/algorithms-divide-conquer
		file='C:\kursy\Algorithms1_coursera\QuickSort_input.txt'
		Input=[]
		with open(file) as f:
			for line in f.readlines():
				Input.append(int(line))
		self._testing(Input)
	
	def testRepeat(self):
		A = [randint(0,10**2) for i in range(10**4)]
		self._testing(A)
	
	def testRepeatLarge(self):
		A = [randint(0,10**5) for i in range(10**5)]
		self._testing(A)
		
	def testMedium(self):
		A = sample(range(10**3),10**3)
		self._testing(A)
	
	def testLarge(self):
		A = sample(range(10**6),10**6)
		self._testing(A)
	
if __name__ == '__main__':
	unittest.main()