# input : vertices and edges

# vertices of the graph
V=[0,1,2,3,4]

# construct 2d array to hold adjacency matrix
#adj=[[1],[0,2,4],[1,3,4],[2,4],[1,2,3]]
"""
adj.append([1])         #   0
adj.append([0,2,4])     #   1
adj.append([1,3,4])     #   2
adj.append([2,4])       #   3
adj.append([1,2,3])     #   4
"""

adj=[[1,4],[0,2],[1,3,4],[2,4],[0,1,2,3]]


# used to check vertex color of adjacent vertices
used=[]

#set all used[i]=0
for i in range(len(V)):  
    used.append(False)

# color assigned to each vertex
# set all colors to -1
color=[]    
for i in range(len(V)):  
    color.append(-1)

# set color of 0 to 0
color[0]=0          

for i in range(1,len(V)):
    print('----iteration:%s------'%(i))    
    print('adjacenct vertices at %s are %s'%(i,adj[i]))

    for j in range(len(adj[i])):
        if(color[adj[i][j]]!=-1): 
            used[color[adj[i][j]]]=True
        print("adj:%s, color:%s, used:%s"%(adj[i][j],color[adj[i][j]],used[j]))
        # we have found adj vertices which are colored
    print(used)

    color_req=-1
    for j in range(len(V)):
        if(used[j]==False):
            color_req=j
            break
    color[i]=color_req
    print("color assigned : ",color_req)
   
    for j in range(len(adj[i])):
        if(color[adj[i][j]]==-1):
            used[color[j]]=False
    
    print("color for vertex %s is:%s "%(i,color[i]))

print("color vector is:%s "%(color))



