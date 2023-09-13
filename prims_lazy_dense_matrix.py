import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import heapq

nodes = 10

def generate_dense_graph(matrix):
    for i in range(nodes):
        for j in range(nodes):
            if i == j:
                continue
            else:
                weight = random.randint(1,100)
                matrix[i][j] = weight
                matrix[j][i] = weight

    return matrix

def plot_graph(matrix):
    numpy_matrix = np.array(matrix)
    G = nx.Graph()
    num_nodes = numpy_matrix.shape[0]
    G.add_nodes_from(range(num_nodes))

    for i in range(num_nodes):
        for j in range(i + 1,num_nodes):
            if numpy_matrix[i][j] != 0:
                G.add_edge(i,j,weight=numpy_matrix[i][j])

    pos = nx.spring_layout(G)
    nx.draw(G,pos,with_labels=True,node_color='lightblue',font_weight='bold')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()

def prims_lazy_sparse_matrix(matrix):
    visited = [False for x in range(nodes)]
    result = []
    visited[0] = True
    edges = []
    for i in range(nodes):
        if matrix[0][i] != 0:
            heapq.heappush(edges,(matrix[0][i],0,i))

    while(len(edges) != 0):
        edge = heapq.heappop(edges)
        if visited[edge[2]] == True:
            continue
        else:
            visited[edge[2]] = True
            result.append(edge)
            for i in range(nodes):
                if matrix[edge[2]][i] != 0:
                    heapq.heappush(edges,(matrix[edge[2]][i],edge[2],i))

    return result


def plot_mst(matrix):
    G = nx.Graph()

    for x in matrix:
        G.add_edge(x[1],x[2],weight=x[0])

    pos = nx.spring_layout(G)
    nx.draw(G,pos,with_labels=True,node_color='lightblue',font_weight='bold')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()

    
if '__main__' == __name__:
    adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    generated_adjacency_matrix = generate_dense_graph(adjacency_matrix)

    plot_graph(generated_adjacency_matrix)

    mst = prims_lazy_sparse_matrix(generated_adjacency_matrix)

    plot_mst(mst)

    