from numpy.random import choice

def GraphInit(str):
	# GRAPH INITIALIZATION
	V = {}
	E = {}
	W = {} # number of vertices adjacent to ith vertex. Use later for sampling edges
	for line in str.splitlines():
		vertices = [int(v) for v in line.split("\t")]
		v = vertices[0]
		V[v] = [v] # vertex with name v will initially containt only himself
		E[v] = vertices[1:]
		W[v] = len(E[v])
	return V,E,W

	
def GraphContraction(V,E,W):
	while len(V.keys())>2:
		# choosing edge.
		v = choice(sorted(V.keys()),p=[f/sum(W) for f in sorted(W.keys())])
		u = choice(E[v])
		# print("choose: v-u: ",v,u)
		E[v] = [e for e in E[v]+E[u] if e!=u and e!=v] # append all edges to vertex v but remove self-loops (e!=v)
		V[v] = V[v] + V[u]
		W[v] = len(E[v])
		for e in E[u]:
			if e!=v: E[e] = [c if c!=u else v for c in E[e]] # re-linking edges from anihilated vertex u to anihilating vertex v
		# vertex u doesn't exists any more independently
		del E[u]
		del V[u]
		del W[u]
		# print("V: ",V)
		# print("E: ",E)
		# print("W: ",W)
		
		# Vo,Eo,Wo = [V.copy(),E.copy(),W.copy()]
	return(V,E,W)

def GraphCut(E):
	return len(list(E.values())[0])
	
	