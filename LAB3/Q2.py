class Graph : 
	def __init__(self) : 
		self.graph = {}
	def add_edge(self,u,v) :
		if u in self.graph :
			self.graph[u].append(v)
		else : 
			self.graph[u] = [v]

def hc(graph) : 
	visited = set()
	stack = set()
	def dfs(vertex) : 
		visited.add(vertex)
		stack.add(vertex)

		if vertex in graph :
			for nei in graph[vertex] :
				if nei not in visited : 
					if dfs(nei) : 
						return True 
				elif nei in stack : 
					return True
		stack.remove(vertex)
		return False
	for vertex in graph : 
		if vertex not in visited :
			if dfs(vertex) :
				return True
	return False



g = Graph()

edges = [(2,0),(2,1),(0,1),(0,2),(1,2),(2,3),(2,0),(3,3)]

for edge in edges : 
	g.add_edge(edge[0],edge[1])

if hc(g.graph) :
	print("Has Cycle")
else :
	print("Doesn't Have Cycle")
