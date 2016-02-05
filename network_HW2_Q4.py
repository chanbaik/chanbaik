import community as co
import networkx as nx

##implementing the Karate club network from networkx
G= nx.karate_club_graph()

##Using the Louvain algorithm to detect community in the Karate Club network
partition = co.best_partition(G)
print "Louvain Partition", partition

##Structuring the actual community provided in Ground Truth
partition_GT =  {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1,7:1, 8:1, 9:2, 10:1, 11:1, \
12:1, 13:1, 14:2, 15:2, 16:1, 17:1, 18:2, 19:1, 20:2, 21:1, 22:2, 23:2, 24:2, \
25:2, 26:2, 27:2, 28:2, 29:2, 30:2, 31:2, 32:2, 33:2}

print "Ground Truth Partition",partition_GT 

##Evaluating the method using Modularity
print "Louvain Modularity", co.modularity(partition, G)
print "Ground Truth Modularity", co.modularity(partition_GT,G)

##Evaluating the method using Normalized Mutual Information Score
from sklearn.metrics.cluster import normalized_mutual_info_score
NMI = normalized_mutual_info_score(list(partition_GT.values()),list(partition.values()))
print "Louvain Normalized Mutual Information Score", NMI
