import networkx as nx
import matplotlib.pyplot as plt

# 1. Initialize an empty undirected graph
G = nx.Graph()

# 2. Add individual or batches of nodes 
G.add_node("Alice")
G.add_nodes_from(["Bob", "Charlie", "Diana"])

# 3. Add edges (connections) with custom attributes (e.g., weights)
G.add_edge("Alice", "Bob", weight=4.5)
G.add_edges_from([
    ("Bob", "Charlie", {"weight": 5.0}),
    ("Charlie", "Diana", {"weight": 6.2}),
    ("Alice", "Diana", {"weight": 2.1})
])

# 4. Basic inspection & metrics
print("Total Nodes:", G.number_of_nodes())
print("Total Edges:", G.number_of_edges())
print("Neighbors of Alice:", list(G.neighbors("Alice")))

# 5. Run a graph algorithm (Shortest Path)
shortest_path = nx.shortest_path(G, source="Bob", target="Diana", weight="weight")
print("Shortest path from Bob to Diana:", shortest_path)

# 6. Visualize the network
pos = nx.spring_layout(G)  # Position nodes using a layout algorithm
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500)

# Add edge weight labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
