import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import heapq

nodes = 10

def generate_random_tree(matrix,i):
    while(True):
        if i == nodes - 1:
            break
        else:
            j = random.randint(0,nodes-1)
            weight = random.randint(1,100)
            if j == i:
                continue
            else:
                if matrix[i][j] == 0:
                    matrix[i][j] = weight
                    matrix[j][i] = weight
                    i = i + 1
                else:
                    continue
            
    return matrix

def add_edges(matrix,n):
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
                if matrix[i][j] == 0:
                    matrix[i][j] = weight
                    matrix[j][i] = weight
                    n = n - 1
                else:
                    continue

    return matrix

def generate_sparse_graph(matrix,i):

    matrix = generate_random_tree(matrix,i)
    extra_no_of_edges = nodes//2
    matrix = add_edges(matrix,extra_no_of_edges)
            
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
    adjacency_matrix = [[0 for x in range(nodes)] for y in range(nodes)]
    generated_adjacency_matrix = generate_sparse_graph(adjacency_matrix,0)

    plot_graph(generated_adjacency_matrix)

    result = prims_lazy_sparse_matrix(generated_adjacency_matrix)

    plot_mst(result)
    



