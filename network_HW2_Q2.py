import networkx as nx

G=nx.Graph()
D=open('C:/Users/chanbaik/Downloads/karate.txt')

GD=D.read().split('\n')
for i in range(len(GD)):
    line=GD[i].split(' ')
    G.add_edge(line[0],line[1])

degree=nx.degree_centrality(G)
print 'degree', '\n', (sorted(degree.items(), key=lambda x:x[1], reverse= True))

betweenness=nx.betweenness_centrality(G,normalized=True)
print 'betweenness', '\n', (sorted(betweenness.items(), key=lambda x:x[1], reverse= True))

closeness=nx.closeness_centrality(G,normalized=True)
print 'closeness', '\n', (sorted(closeness.items(), key=lambda x:x[1], reverse= True))



