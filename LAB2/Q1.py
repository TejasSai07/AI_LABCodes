class Graph :
    def __init__(self) : 
        self.adjlist = {}
    def addv(self,vertex) : 
        if vertex not in self.adjlist :
            self.adjlist[vertex] = []
    def addedge(self,source,dest) : 
        if source in self.adjlist and dest in self.adjlist :
            self.adjlist[source].append(dest)
    def edgerep(self) : 
        edge = []
        for source, dest in self.adjlist.items() : 
            for de in dest : 
                edge.append(f"{source}->{dest}")
        return edge
    
graph1 = Graph()
graph2 = Graph()

graph1.addv(0)
graph1.addv(1)
graph1.addv(2)
graph1.addv(3)
graph2.addv(4)
graph2.addv(5)

graph1.addedge(0,1)
graph1.addedge(1,2)
graph1.addedge(2,0)
graph1.addedge(2,1)
graph1.addedge(3,2)

graph2.addedge(4,5)
graph2.addedge(5,4)

print(graph1.edgerep())
print(graph2.edgerep())
