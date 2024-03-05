# -*- coding: utf-8 -*-


import copy

original_matrix = [[0,2,-2,1,0,0],[-2,0,2,0,1,0],[2,-2,0,0,0,1]]

def quiver_mutation(matrix_lists,mutated_node):
    """
    Creates new matrix to represent quiver after mutation
    
    Args:
        matrix_lists: a matrix of the original quiver (list)
        mutated_node: the node being mutated (int)
    
    returns: a matrix list that represents the new quiver after mutation
    
    """
    
    list_copy = copy.deepcopy(matrix_lists)
    if mutated_node == 1:
        for i in range(6):
            if list_copy[0][i]>0 and i<3:
                for j in range(i+1,6):
                    if list_copy[0][j]<0 and j<3: #case where new arrows are between main nodes
                        list_copy[i][j]+= list_copy[0][i]*list_copy[0][j]
                        list_copy[j][i]+= -1*list_copy[0][i]*list_copy[0][j]
                    elif list_copy[0][j]<0 and j>=3: #case where new arrows are between one main node and one prime
                        list_copy[i][j]+= list_copy[0][i]*list_copy[0][j]              
            elif list_copy[0][i]<0 and i<3:
                for j in range(i+1,6):
                    if list_copy[0][j]>0 and j<3: #case where new arrows are between main nodes
                        list_copy[i][j]+= -1*list_copy[0][i]*list_copy[0][j]
                        list_copy[j][i]+= list_copy[0][i]*list_copy[0][j]   
                    elif list_copy[0][j]>0 and j>=3: #case where new arrows are between one main node and one prime
                        list_copy[i][j]+= -1*list_copy[0][i]*list_copy[0][j]
        for i in range(len(list_copy[0])):
            list_copy[0][i]*=-1
        list_copy[1][0]*=-1
        list_copy[2][0]*=-1
                    
    elif mutated_node == 2:
        for i in range(6):
            if list_copy[1][i]>0 and i<3:
                for j in range(i+1,6):
    
                    if list_copy[1][j]<0 and j<3: #case where new arrows are between main nodes
                        list_copy[i][j]+= list_copy[1][i]*list_copy[1][j]
                        list_copy[j][i]+= -1*list_copy[1][i]*list_copy[1][j]
                    elif list_copy[1][j]<0 and j>=3: #case where new arrows are between one main node and one prime
                        list_copy[i][j]+= list_copy[1][i]*list_copy[1][j]              
            elif list_copy[1][i]<0 and i<3:
                for j in range(i+1,6):
                    if list_copy[1][j]>0 and j<3: #case where new arrows are between main nodes
                        list_copy[i][j]+= -1*list_copy[1][i]*list_copy[1][j]
                        list_copy[j][i]+= list_copy[1][i]*list_copy[1][j]   
                    elif list_copy[1][j]>0 and j>=3: #case where new arrows are between one main node and one prime
                        list_copy[i][j]+= -1*list_copy[1][i]*list_copy[1][j]
        for i in range(len(list_copy[1])):
            list_copy[1][i]*=-1
            
        list_copy[0][1]*=-1
        list_copy[2][1]*=-1

    elif mutated_node == 3:
        for i in range(6):
            if list_copy[2][i]>0 and i<3:
                for j in range(i+1,6):
    
                    if list_copy[2][j]<0 and j<3: #case where new arrows are between main nodes
                        list_copy[i][j]+= list_copy[2][i]*list_copy[2][j]
                        list_copy[j][i]+= -1*list_copy[2][i]*list_copy[2][j]
                    elif list_copy[2][j]<0 and j>=3: #case where new arrows are between one main node and one prime
                        list_copy[i][j]+= list_copy[2][i]*list_copy[2][j]              
            elif list_copy[2][i]<0 and i<3:
                for j in range(i+1,6):
                    if list_copy[2][j]>0 and j<3: #case where new arrows are between main nodes
                        list_copy[i][j]+= -1*list_copy[2][i]*list_copy[2][j]
                        list_copy[j][i]+= list_copy[2][i]*list_copy[2][j]   
                    elif list_copy[2][j]>0 and j>=3: #case where new arrows are between one main node and one prime
                        list_copy[i][j]+= -1*list_copy[2][i]*list_copy[2][j]
        for i in range(len(list_copy[2])):
            list_copy[2][i]*=-1
            
        list_copy[1][2]*=-1
        list_copy[0][2]*=-1

    return list_copy
def quiver_mutation_repeated(original_matrix,mutated_nodes):
    """
    Creates new matrix to represent quiver after several mutations
    
    Args:
        matrix_lists: a matrix of the original quiver (list)
        mutated_node: a list of nodes being mutated with first element being first mutation and so on (list)
    
    returns: a matrix list that represents the new quiver after mutations
    
    """
    if not mutated_nodes:
        return original_matrix
    list_copy = copy.deepcopy(original_matrix)
    mutated_quiver = quiver_mutation(list_copy, mutated_nodes[0])
    if len(mutated_nodes)>1:
        for i in range(1,len(mutated_nodes)):
            mutated_quiver = quiver_mutation(mutated_quiver, mutated_nodes[i])
    return mutated_quiver
quiver_map ={(1,):tuple(('r_1',)),(2,):tuple(('r_2',)),(3,):tuple(('r_3',))}

def quiver_mutation_reflections(matrix,mutated_nodes,i):
    """
    Creates new matrix to represent quiver after several mutations
    
    Args:
        matrix: the w[k] matrix, find this using quiver_mutation_repeated function (list)
        mutated_node: a list of nodes being mutated with first element being first mutation and so on (list)
        i: the edge we are reflecting about (int)
        
    
    returns: a tuple of r's 
    
    Example Input: quiver_mutation_reflections(quiver_mutation_repeated(original_matrix,[1,2,3]),[1,2,3],1)
    Example Output: ('r_1',)
    
    """
    nodes_copy = copy.deepcopy(mutated_nodes)
    map_tuple = tuple([i])+tuple(nodes_copy)
    if map_tuple in quiver_map:
        
        return quiver_map[map_tuple]
    else:
        k = nodes_copy.pop()
        w = quiver_mutation_repeated(original_matrix, nodes_copy)
        b = w[i-1][k-1]
        c = w[k-1][3:6]
        if (min(c)>=0 and sum(c)>0 and b>0) or (min(c)<=0 and sum(c)<0 and b<0):
            r_i = quiver_mutation_reflections(w,nodes_copy,k)+quiver_mutation_reflections(w,nodes_copy,i) \
            +quiver_mutation_reflections(w,nodes_copy,k)

        else:
            r_i = quiver_mutation_reflections(w,nodes_copy,i)
        
        return r_i


k = y.copy()
h = quiver_mutation(k,3)
print(h)
