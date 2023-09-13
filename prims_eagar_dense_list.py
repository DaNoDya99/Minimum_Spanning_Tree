import random
import matplotlib.pyplot as plt
import networkx as nx
import sys

nodes = 10

graph = {}
key = [sys.maxsize for x in range(nodes)]
visited = [False for x in range(nodes)]

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

def prims_eagar(graph):
    mst = []
    parent = [-1 for x in range(nodes)]

    key[0] = 0

    for i in range(nodes):
        min_vertex = min_key_vertex(key,visited)
        visited[min_vertex] = True

        for neighbor in graph[min_vertex]:
            if visited[neighbor[0]] == False and neighbor[1] < key[neighbor[0]]:
                key[neighbor[0]] = neighbor[1]
                parent[neighbor[0]] = min_vertex

    for i in range(1,nodes):
        mst.append((parent[i],i,key[i]))

    return mst


def min_key_vertex(key,visited):
    min_key = sys.maxsize
    min_vertex = -1
    for i in range(nodes):
        if visited[i] == False and key[i] < min_key:
            min_key = key[i]
            min_vertex = i

    return min_vertex

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
    

if '__main__' == __name__:
    graph_generated = initialize_graph()
    graph_generated = generate_dense_graph()

    plot_graph(graph_generated)

    result = prims_eagar(graph_generated)

    plot_mst(result)


