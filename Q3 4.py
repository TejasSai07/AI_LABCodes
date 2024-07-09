class Graph : 
	def __init__(self) : 
		self.vertices = set()
		self.edges = []
		self.adjlist = {}
		self.admat = []

	def addv(self,vertex) : 
		self.vertices.add(vertex)

	def adde(self,v1,v2) : 
		self.edges.append((v1,v2))
		self.vertices.add(v1)
		self.vertices.add(v2)
		self.updlist()
		self.updmat()

	def updmat(self) : 
		v_list = sorted(list(self.vertices))
		size = len(v_list)
		self.admat = [[0]*size for i in range(size)]
		for e in self.edges : 
			v1_ind = v_list.index(e[0])
			v2_ind = v_list.index(e[1])
			self.admat[v1_ind][v2_ind] = 1
			self.admat[v2_ind][v1_ind] = 1

	def updlist(self) : 
		self.adlist = {}
		for ver in self.vertices : 
			neig = [v[1] for v in self.edges if v[0]==ver]+[u[0] for u in self.edges if u[1]==ver]
			self.adlist[ver] = neig

	def pal(self) : 
		for ver,nei in self.adlist.items() : 
			print(f"{ver} : {nei}")

	def pam(self) : 
		for r in self.admat :
			print(r)



graph = Graph()
graph.addv('A')
graph.addv('B')
graph.addv('C')
graph.addv('D')
graph.addv('E')

graph.adde('A','B')
graph.adde('A','C')
graph.adde('A','E')
graph.adde('B','C')
graph.adde('C','D')
graph.adde('C','E')

graph.pal()
graph.pam()
