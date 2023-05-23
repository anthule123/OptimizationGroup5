from matplotlib import pyplot as plt
import networkx as nx


n =10 
G = nx.Graph()
G.add_nodes_from(range(n))
G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,0)])
nx.draw(G, with_labels=True)
plt.show()
