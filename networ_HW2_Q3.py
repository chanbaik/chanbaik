import networkx as nx

G=nx.DiGraph()
G.add_edge(1,2)
G.add_edge(2,1)
G.add_edge(2,4)
G.add_edge(3,2)
G.add_edge(3,4)
G.add_edge(4,2)
G.add_edge(4,3)

pagerank=nx.pagerank(G)
print pagerank
