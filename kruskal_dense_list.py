import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

nodes = 10

graph = {}

def initialize_graph():
    for i in range(nodes):
        graph[i] = []
    return graph

def generate_dense_graph():
    for i in range(nodes):
        for j in range(i+1,nodes):
            weight = random.randint(1,100)
            graph[i].append((j,weight))
            graph[j].append((i,weight))

    return graph

def find(parent, i):
    if parent[i] == -1:
        return i
    return find(parent, parent[i])

def union(parent,u,v):
    u_set = find(parent,u)
    v_set = find(parent,v)
    parent[u_set] = v_set

def kruskal(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((node, neighbor, weight))

    edges.sort(key=lambda edge: edge[2])
    minimum_spanning_tree = []
    parent = [-1]*nodes

    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            minimum_spanning_tree.append((u, v, weight))
            union(parent, u, v)

    return minimum_spanning_tree

def plot_graph(graph):
    G = nx.Graph()
    
    G.add_nodes_from(graph.keys())

    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(vertex, neighbor[0], weight=neighbor[1])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True,node_color='lightblue', font_weight='bold')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()

def plot_mst(mst):
    G = nx.Graph()
    G.add_nodes_from(graph.keys())

    for edge in mst:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True,node_color='lightblue', font_weight='bold')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()

if __name__ == '__main__':
    graph = initialize_graph()
    graph = generate_dense_graph()
    
    plot_graph(graph)

    mst = kruskal(graph)

    plot_mst(mst)
                