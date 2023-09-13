import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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

def find_parent(parent,i):
    if parent[i] == -1:
        return i
    else:
        return find_parent(parent,parent[i])
    
def union(parent,x,y):
    x_set = find_parent(parent,x)
    y_set = find_parent(parent,y)
    parent[x_set] = y_set

def kruskal(matrix):
    result = []
    i = 0
    e = 0
    parent = [-1 for x in range(nodes)]
    while e < nodes - 1:
        min = 999
        for i in range(nodes):
            for j in range(nodes):
                if find_parent(parent,i) != find_parent(parent,j) and matrix[i][j] < min and matrix[i][j] != 0:
                    min = matrix[i][j]
                    x = i
                    y = j
        union(parent,x,y)
        result.append([x,y,matrix[x][y]])
        e = e + 1

    return result

def plot_resultant_mst(result):
    resultant_matrix = [[0 for x in range(nodes)] for y in range(nodes)]

    for i in range(len(result)):
        resultant_matrix[result[i][0]][result[i][1]] = result[i][2]
        resultant_matrix[result[i][1]][result[i][0]] = result[i][2]

    plot_graph(resultant_matrix)


if '__main__' == __name__:
    adjacency_matrix = [[0 for x in range(nodes)] for y in range(nodes)]
    generated_adjacency_matrix = generate_sparse_graph(adjacency_matrix,0)

    # plot_graph(generated_adjacency_matrix)
    
    result = kruskal(generated_adjacency_matrix)

    print("Resultant MST: ",result)
    
    # plot_resultant_mst(result)



