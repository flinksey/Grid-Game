# grid game but using a list instead of a dict for the grid content
import random

def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def start_game(M, N, inside):
    #Problem: I'm creating the cell content list AS the grid is being generated, but
    #I'll have to find a way to generate the updated grid based on the updated list
    
    return 0

def set_up():
    M = int(input("no. of rows: "))
    N = int(input("no. of cols: "))
    K = int(input("boundary no: "))
    
    cell = [] #format is [no. displayed in cell, row, col]
    row_label = [j for j in range(M)]
    col_label = [i for i in range(N)]
    row_label.insert(0, " ")

    print("\nLet's start!\n")
    
    for row in range(M+1):
        print(row_label[row], end="  ")
        if row == 0:
            for col in range(N):
                print(col_label[col], end="   ")
        else:
            for col in range(N):
                ins = rand_gen(K)
                print(ins, end=" | ")
                cell.append([ins,row-1,col])
        print(" ")
    
    #start_game(M,N,cell)

set_up()
