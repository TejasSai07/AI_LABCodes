class Graph : 
	def _init_(self) : 
		self.graph = {}
	def addedge(self,u,v) :
		if u in self.graph :
			self.graph[u].append[v]
		else :
			self.graph[u] = [v]

def topsort(graph) :
	visitec = set()
	topor = []
	def dfs(vertex) :
		visited.add(vertex)
		if vertex in graph : 
			for nei in graph(vertex) :
				if nei not in visited :
					dfs(nei)
		topor.insert(0,vertex)

	for vertex in graph :
		if vertex not in visited :
			dfs(vertex)

	return topor



g = Graph()
edges = [(2,3),(3,1),(4,0),(4,1),(5,0),(5,2)]

for edge in edges :
	g.addedge(edge[0],edge[1])

result = topsort(g.graph)
print(result)
