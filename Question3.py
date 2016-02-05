A_main = [] 
B=open('HW1_3.txt','r')
AB=B.read().split('\n')
for i in range(len(AB)):
    line=AB[i].split(' ')
    A_main.append([line[0],line[1],float(line[2])])
def bubble_sort(unsort_list):
    sort_list = unsort_list
    swap = True
    while swap:
        swap = False
        for i in range(len(unsort_list)-1):
            if (sort_list[i][2] < sort_list[i+1][2]):
                sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
                swap = True
    return sort_list
S_list=bubble_sort(A_main) 
nodes=[] 
cost=S_list[0][2]
nodes.append([S_list[0][0],S_list[0][1]])
edges = []
edges.append((S_list[0][0],S_list[0][1]))
for i in range(len(S_list)-1):
    Check=True
    for j in range(len(nodes)):
        if (S_list[i+1][0] in nodes[j]) or (S_list[i+1][1] in nodes[j]):
            if (S_list[i+1][0] in nodes[j]) and (S_list[i+1][1] in nodes[j]): 
                Check=False
                break 
            else:
                if (S_list[i+1][0] in nodes[j]):
                    if (S_list[i+1][1] not in [item for sublist in nodes\
                    for item in sublist]):
                        nodes[j].append(S_list[i+1][1])
                        cost+=S_list[i+1][2]
                        edges.append((S_list[i+1][0],S_list[i+1][1]))
                        Check=False
                        break
                    else:
                        nodes[j].append(S_list[i+1][1])
                        nodes=[[item for sublist in nodes for item in sublist]]
                        edges.append((S_list[i+1][0],S_list[i+1][1]))
                        cost+=S_list[i+1][2]
                        Check=False
                        break
                elif (S_list[i+1][1] in nodes[j])==True:    
                    if (S_list[i+1][0] not in [item for sublist in nodes\
                    for item in sublist]):
                        nodes[j].append(S_list[i+1][0])
                        cost+=S_list[i+1][2]
                        edges.append((S_list[i+1][0],S_list[i+1][1]))
                        Check=False
                        break
                    else:
                        nodes[j].append(S_list[i+1][0])
                        nodes=[[item for sublist in nodes for item in sublist]]
                        cost+=S_list[i+1][2]
                        edges.append((S_list[i+1][0],S_list[i+1][1]))
                        Check=False
                        break
    if Check: 
        nodes.append([S_list[i+1][0],S_list[i+1][1]])
        cost+=S_list[i+1][2]
        edges.append((S_list[i+1][0],S_list[i+1][1]))

print edges, 'The max-cost is %f' % cost