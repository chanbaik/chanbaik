network = 'HW_1.4.txt'
start = '1'
end = '6'
def Q4_shortestpath(network,start,end):
    A = []
    A_nodes=set()
    B=open(network,'r')
    AB=B.read().split('\n')
    for i in range(len(AB)):
        line=AB[i].split(' ')
        A.append([line[0],line[1],float(line[2])])
        A_nodes.update([A[i][0],A[i][1]])
    nodes=list(A_nodes)
    nodes.sort()
    #a distionary to track the path 
    track = {}    
    for i in range(len(nodes)):
        index=nodes[i]
        track[index] = start
    #frameworks for Dijkstra's algorithms
    dist={}
    for i in range(len(nodes)):
        index=nodes[i]
        dist[index]=float("inf")
    nodes.remove(start)
    visited=[start]
    del dist[start]
    temp_dist=dist.copy()
    for i in range(len(A)):
        if A[i][0]==visited[-1]:
            dist[str(A[i][1])]=A[i][2]
        elif A[i][1]==visited[-1]:
            dist[str(A[i][0])]=A[i][2]
    visited.append(min(dist,key=dist.get))
    while end not in visited:
        for i in range(len(A)):
            if A[i][0]==visited[-1]:
                if dist.get(visited[-1])+ A[i][2]< dist.get(str(A[i][1])):
                    dist[str(A[i][1])]=dist.get(visited[-1])+A[i][2]
                    track[A[i][0]] = visited[-1]
            elif A[i][1]==visited[-1]:
                if dist.get(visited[-1])+ A[i][2]< dist.get(str(A[i][0])):
                    dist[str(A[i][0])]=dist.get(visited[-1])+A[i][2]
                    track[A[i][0]] = visited[-1]
        del temp_dist[visited[-1]]
        visited.append(min(temp_dist,key=dist.get))
    inversepath = [end]
    index = end
    while index[0]!=start:
        inversepath.append(track[index[0]])
        index=track[index[0]]
    path = inversepath[::-1]
    return 'The shortest path from node '+ str(start) + ' to node ' \
    + str(end) +' is ' +str(path)+'with cost'+str(dist.get(end))   

print Q4_shortestpath('HW1_4.txt','1','6')