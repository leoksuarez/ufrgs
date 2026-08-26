import networkx as nx
import random

# 1. Create a basic graph (e.g., a cycle graph of 5 nodes)
G = nx.cycle_graph(5)

# 2. Define the starting node
current_node = 0
walk_path = [current_node]
num_steps = 10

# 3. Perform the random walk
for _ in range(num_steps):
    # Get a list of all neighbors for the current node
    neighbors = list(G.neighbors(current_node))
    
    # Randomly choose the next node with equal probability
    next_node = random.choice(neighbors)
    
    walk_path.append(next_node)
    current_node = next_node

print("Path taken by the walker:", walk_path)
