from GraphContraction import *
import unittest
from random import *
import numpy as np


from time import time
from random import randint

def log_time(function,*args,**kwargs):
	start = time()
	ret = function(*args,**kwargs)
	end = time()
	return([end-start,ret])
	
class Test(unittest.TestCase):
	
	def _testing(self,str):
		G0 = GraphInit(str)
		print("INIT GRAPH...")
		V,E,W = G0
		print("V: ",V)
		print("E: ",E)
		print("W: ",W)
		print("CONTRACTING GRAPH...")
		Gfin = GraphContraction(V.copy(),E.copy(),W.copy())
		print("GRAPH AFTER CONTRACTION:")
		V,E,W = Gfin
		print("V: ",V)
		print("E: ",E)
		print("W: ",W)
		cut = GraphCut(E)
		print("GRAPH CUT: ", cut)
		
		## ADD PLOT TO VISUALIZE MINIMUM CUT AFTER X RUNS
		
	def _testingMinCut(self,str):
		n=10
		G0 = GraphInit(str)
		V,E,W = G0
		cuts=[]
		print("RUNNING CONTRACTION ALGORITHM %d TIMES" % n)
		for i in range(n):
			Gfin = GraphContraction(V.copy(),E.copy(),W.copy())
			cut = GraphCut(Gfin[1])
			print("(%d) GRAPH CUT: " % i,cut)
			cuts.append(cut)
			del Gfin
		print(cuts)
	def testSimple(self):
		# Simple graph for tests
		str="""1	2	4
2	1	3	4
3	2	4
4	1	2	3"""
		self._testing(str)
		self._testingMinCut(str)
	def testBigGraph(self):
		file='C:\kursy\Algorithms1_coursera\kargerMinCut.txt'
		Input=open(file).read()
		str=""
		for l in Input.splitlines():
			str+=l[:-1]+"\n"
		self._testing(str)
		self._testingMinCut(str)
	# def testEmpty(self):
		# str =""
		# self._testing(str)
		
	def testTwoV(self):
		str="""1	2
2	1"""
		self._testing(str)
		self._testingMinCut(str)
		
	# def testTwoComponents(self):
		# str="""1	2
# 2	1
# 3	4
# 4	3"""
		# self._testing(str)
		# self._testingMinCut(str)
	
	
		
if __name__ == '__main__':
	unittest.main()