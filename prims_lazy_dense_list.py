import random
import matplotlib.pyplot as plt
import networkx as nx
import heapq

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

def lazy_prims(graph):
    mst = []
    visited = [False for x in range(nodes)]
    heap = []
    start_vertex = 0

    for neighbor in graph[start_vertex]:
        heapq.heappush(heap,(neighbor[1],start_vertex,neighbor[0]))

    visited[start_vertex] = True

    while(len(heap) > 0):
        edge = heapq.heappop(heap)
        if visited[edge[2]] == True:
            continue
        else:
            visited[edge[2]] = True
            mst.append((edge[1],edge[2],edge[0]))
            for neighbor in graph[edge[2]]:
                if visited[neighbor[0]] == False:
                    heapq.heappush(heap,(neighbor[1],edge[2],neighbor[0]))

    return mst

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

    result = lazy_prims(graph_generated)
    
    plot_mst(result)


