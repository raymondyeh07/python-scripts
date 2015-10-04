import networkx as nx

G = nx.DiGraph()

G.add_edges_from([(1,2), (2,3), (2,4), (1,5)])

for n in nx.dfs_postorder_nodes(G, 1):
    print n

print G
