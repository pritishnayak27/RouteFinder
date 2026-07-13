import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, path, cost):

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color="skyblue",
        node_size=700
    )

    # Draw all edges
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="gray",
        width=2
    )

    # Draw node labels
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10,
        font_weight="bold"
    )

    # Highlight shortest path
    path_edges = list(zip(path[:-1], path[1:]))

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color="red",
        width=4
    )

    # Edge labels
    edge_labels = nx.get_edge_attributes(G, "distance")

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    plt.title(
        f"Shortest Path: {' → '.join(path)}\nTravel Time: {cost:.2f} hours"
    )

    plt.axis("off")
    return plt.gcf()