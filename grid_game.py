#LATEST VERSION
#format-wise: it looks alright with max of M,N,K = 10

import random
def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def scorekeeper():
    #keeps score lol
    return 0

def adj_match(contents, cell_val, match_count):
    #fxn that searches for adjacent matches, if any
    checklist = [] #this is the list of the matches -- to check for adj matches of selected cell's matches
    
    c
    return 0

def coords_check(contents):
    #fxn that checks whether input coords are valid
    r_coord = int(input("Please enter the row number: "))
    c_coord = int(input("Please enter the col number: "))
    
    cell_ind = 0 #to check whether the cell is empty later
    is_coord = 0 #increased to 1 if the coordinates are within bounds
    cell_val = 0 #displayed int in cell
    match_count = 0 #number of potential matches in grid
    no_matches = 0 #list of cell coords with >= 3 possible matches
    
    #are the coordinates within range?
    for coord in contents:
        if coord[1] == r_coord and coord[2] == c_coord:
            cell_ind = contents.index(coord)
            is_coord += 1
    
    #is the selected cell "empty"?
    if is_coord and if contents[cell_ind][0] != "-":
        cell_val = contents[cell_ind][0]
    else:
        print("Invalid Input! Try again.")
        coords_check(contents)
    
    #does the value in the selected cell have at least 2 possible matches?
    for _ in contents:
        if _[0] == cell_val:
            match_count += 1
            
    if match_count >= 3:
        #does the value in the selected cell have at least 2 adjacent matches?
        adj_match(contents)
    else:
        print("Invalid Input! Try again.")
        coords_check(contents)
        
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
    print(contents)
    print("\nGame on!\n")
    
    grid_gen(M,N,row_label,col_label,contents)

set_up()
