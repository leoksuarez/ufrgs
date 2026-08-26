import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox

# 1. baixa rede cicloviaria de porto alegre
place = ["Porto Alegre, Rio Grande do Sul, Brasil"]
print(f"Buscando malha cicloviária de {place}...")

custom_filter = '["highway"~"primary|secondary|tertiary|cycleway"]'

G = ox.graph_from_place(place, custom_filter=custom_filter, network_type="bike", simplify=True)

# 2. converte multigrafo direcionado em grafo simples nao direcionado
# ox.convert.to_undirected works in OSMnx 2.0+; G.to_undirected() works anywhere
try:
  G_undirected = ox.convert.to_undirected(G)
except AttributeError:
  G_undirected = ox.get_undirected(G)

# guarda apenas a maior componente conexa e descarta ilhas desconectadas
largest_cc = max(nx.connected_components(G_undirected), key=len)
G_sub = G_undirected.subgraph(largest_cc).copy()

# 3. computa a arvore geradora minima (MST) usando o algoritmo de Kruskal
mst = nx.minimum_spanning_tree(G_sub, weight="length", algorithm="kruskal")

# 4. compara comprimento total da rede original com a arvore geradora minima
total_length = (
    sum(data.get("length", 0) for _, _, data in G_sub.edges(data=True)) / 1000
)
mst_length = (
    sum(data.get("length", 0) for _, _, data in mst.edges(data=True)) / 1000
)

print(f"Rede original: {len(G_sub.nodes)} vértices, {len(G_sub.edges)} arestas")
print(f"Arvore geradora minima: {len(mst.nodes)} vértices, {len(mst.edges)} arestas")
print(f"Comprimento total da rede original: {total_length:.2f} km")
print(f"Comprimento total da árvore geradora mínima: {mst_length:.2f} km")

# 5. compara visualmente a rede original com a arvore geradora minima
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ox.plot_graph(
    G_sub,
    ax=ax1,
    node_size=0,
    edge_color="#777777",
    edge_linewidth=0.8,
    show=False,
    close=False,
)
ax1.set_title(f"Rede original ({total_length:.1f} km)")

ox.plot_graph(
    mst,
    ax=ax2,
    node_size=0,
    edge_color="#0066cc",
    edge_linewidth=1.2,
    show=False,
    close=False,
)
ax2.set_title(f"Árvore geradora mínima ({mst_length:.1f} km)")

plt.tight_layout()
plt.show()