# -*- coding: utf-8 -*-


matrix_lists = [[0,2,-2,1,0,0],[-2,0,2,0,1,0],[2,-2,0,0,0,1]]
new_list_1 = [[0,-2,2,-1,0,0],[2,0,-2,0,1,0],[-2,2,0,2,0,1]]
new_list_2 = [[0,-2,2,1,2,0],[2,0,-2,0,-1,0],[-2,2,0,0,0,1]]
new_list_3 = [[0,-2,2,1,0,0],[2,0,-2,0,1,2],[-2,2,0,0,0,-1]]
new_list_1_2 =[[0,2,-2,-1,0,0],[-2,0,2,0,-1,0],[2,-2,0,2,2,1]]
new_list_1_3 =[[0,2,-2,3,0,2],[-2,0,2,0,1,0],[2,-2,0,-2,0,-1]]
def quiver_mutation(matrix_lists,mutated_node):
    list_copy = matrix_lists.copy()
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
        list_copy[0] = [element * -1 for element in list_copy[0]]
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
        list_copy[1] = [element * -1 for element in list_copy[1]]
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
        list_copy[2] = [element * -1 for element in list_copy[2]]
        list_copy[1][2]*=-1
        list_copy[0][2]*=-1

    return matrix_lists
z = matrix_lists.copy()
x =  quiver_mutation(z,1)
w = x.copy()

y = quiver_mutation(w, 2)
k = y.copy()
h = quiver_mutation(k,3)
print(h)
