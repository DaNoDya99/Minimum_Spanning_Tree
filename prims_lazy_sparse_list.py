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

def generate_random_tree():
    i = 0
    while(True):
        if i == nodes:
            break
        else:
            j = random.randint(0,nodes-1)
            weight = random.randint(1,100)
            if j == i:
                continue
            else:
                if j in graph[i]:
                    continue
                else:
                    graph[i].append((j,weight))
                    graph[j].append((i,weight))
                    i += 1
            
    return graph

def add_edges(n):
    while(True):
        if n == 0:
            break
        else:
            i = random.randint(0,nodes-1)
            j = random.randint(0,nodes-1)
            weight = random.randint(1,100)
            if i == j:
                continue
            else:
                if j in graph[i]:
                    continue
                else:
                    graph[i].append((j,weight))
                    graph[j].append((i,weight))
                    n -= 1

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
    graph_generated = generate_random_tree()
    extra_no_of_edges = nodes//2
    graph_generated = add_edges(extra_no_of_edges)

    plot_graph(graph_generated)

    result = lazy_prims(graph_generated)

    # print(result)
    plot_mst(result)


