def addedgelist(adlist,admatrix,src,dest,cost) :
    adlist[src].append((dest,cost))

    admatrix[src][dest] = cost



N = int(input("Enter the Number of Vertices : "))
src = 0
adjlist = [[] for i in range(N+1)]
admatrix = [[0]*(N+1) for i in range(N+1)]
while(src!=-1) :
    src = int(input("Enter the Source :  "))
    dest = int(input("Enter the Dest :  "))
    cost = int(input("Enter the Cost : "))
    if(src==-1) :
        break
    addedgelist(adjlist,admatrix,src,dest,cost)
    
    
print("Adjacency List:")
for i in range(N+1):
    print(f"{i}: {adjlist[i]}")

print("Adjacency Matrix:")
for row in admatrix:
    print(row)
