#LATEST VERSION
#format-wise: it looks alright with max of M,N,K = 10

import random
def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def scorekeeper():
    #keeps score lol
    return 0

def match_check(contents):
    #fxn that handles User engagement in the game
    r_coord = int(input("Please enter the row number: "))
    c_coord = int(input("Please enter the col number: "))
    
    #error handling-----|
    
    #are the coordinates within range?
    #is the selected cell "empty"?
    #does the selected cell have at least 2 adjacent matches?

def grid_gen(M,N,row_label,col_label,contents):
    #fxn that generates the grid each time (from beginning through udpates)
    for row in range(M+1):
        print(row_label[row], end = "  ")
        if row == 0:
            for col in range(N):
                print(col_label[col], end = "  ")
        else:
            for col in range(N):
                print(contents[(row-1)*N + col][0], end = "  ")
        print("  ")

def set_up():
    M = int(input("no. of rows: "))
    N = int(input("no. of cols: "))
    K = int(input("boundary no: "))
    
    #for checking: contents = [[0, 0, 0], [1, 0, 1], [0, 1, 0], [2, 1, 1], [1, 2, 0], [1, 2, 1]]
    row_label = [j for j in range(M)]
    col_label = [i for i in range(N)]    
    contents = [[rand_gen(K),row,col] for row in row_label for col in col_label]
    
    row_label.insert(0, " ")
   
    #print(contents)
    print("\nGame on!\n")
    
    grid_gen(M,N,row_label,col_label,contents)

set_up()
