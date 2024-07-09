class WGraph  :
	def __init__(self):
		self.adjacencylist = {}
	def addvertex(self,vertex) :
		if vertex not in self.adjacencylist : 
			self.adjacencylist[vertex] = {}
	def addedge(self,s,d,w) :
		if s in self.adjacencylist and d in self.adjacencylist : 
			self.adjacencylist[s][d] = w
	def edgerep(self) : 
		edges = []
		for s,d in self.adjacencylist.items() : 
			for de, w in d.items() : 
				edges.append(f"({s}->{de},{w})")
		return edges


graph = WGraph()
graph1 = WGraph()
graph.addvertex(0)
graph.addvertex(1)
graph.addvertex(2)
graph.addvertex(3)
graph1.addvertex(4)
graph1.addvertex(5)

graph.addedge(0,1,6)
graph.addedge(1,2,7)
graph.addedge(2,0,5)
graph.addedge(2,1,4)
graph.addedge(3,2,10)

graph1.addedge(4,5,3)
graph1.addedge(5,4,1)

print(graph.edgerep())
print(graph1.edgerep())