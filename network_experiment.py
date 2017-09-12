import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_node(1)
G.add_nodes_from([2,3,4,5])
G.add_edge(1,2)
G.add_edges_from([(1,3),(2,4),(2,5),(4,1),(5,1),(5,3),(5,4)])
G.remove_node(1)
nx.draw(G,with_labels=True)
plt.savefig("exp.png")
plt.show()