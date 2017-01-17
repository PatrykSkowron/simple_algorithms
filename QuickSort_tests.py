from QuickSort import *
import unittest
from random import *

class TestQuickSort(unittest.TestCase):
	
	def _testing(self,A):
		
		Bt,B = log_time(sorted,A)
		At,A = log_time(QuickSort,A)
		self.assertEqual(A,B)
		print("OK!\nlength: %d \nAlgorithm time: %.5f seconds. \nBuilt in time: %.5f seconds." % (len(A),At,Bt))
		
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
	
if __name__ == '__main__':
	unittest.main()
	
	
#test