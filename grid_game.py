#LATEST VERSION
#format-wise: it looks alright with max of M,N,K = 10

import random
def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def scorekeeper():
    #keeps score lol
    return 0

def adj_match(checklist):
    #fxn that searches for adjacent matches, if any: bottom, top, right, left    
    in_check = checklist.copy()
    base = ref_list[0] #selected cell
    counter = len(checklist)
    
    if len(checklist):
        while counter:
            for cell in in_check:
                if (cell[1] == base[1] + 1) and (cell[2] == base[2]):#bottom
                    if cell not in checked:
                        checked.append(cell)
                if (cell[1] == base[1] - 1) and (cell[2] == base[2]):#top
                    if cell not in checked:
                        checked.append(cell)
                if (cell[1] == base[1]) and (cell[2] == base[2] + 1):#right
                    if cell not in checked:
                        checked.append(cell)
                if (cell[1] == base[1]) and (cell[2] == base[2] - 1):#left
                    if cell not in checked:
                        checked.append(cell)
            counter -= 1
    
    del in_check[0]
    
    #[some loop] adj_match() for each cell in checklist
    return 0 #needs to return no. of matches, 

def iter_match(checklist):
    #fxn that tracks checking of adj matches per adj match of selected cell
    checked = [] 
    in_check = checklist.copy() #to track the cells that still need to be checked for matches
    
    while len(in_check):
        adj_match(in_check)
        del in_check[0] #how can I update the list (need to make it "empty" + gravity)

def coords_check(contents):
    #fxn that checks whether input coords are valid
    r_coord = int(input("Please enter the row number: "))
    c_coord = int(input("Please enter the col number: "))
    
    cell_ind = 0 #to check whether the cell is empty later
    is_coord = 0 #increased to 1 if the coordinates are within bounds
    cell_val = 0 #displayed int in cell
    
    checklist = 0 #list of matching cells
    no_matches = 0 #list of cell coords with >= 3 possible matches
    
    #are the coordinates within range?
    for coord in contents:
        if coord[1] == r_coord and coord[2] == c_coord:
            cell_ind = contents.index(coord)
            is_coord += 1
    
    #is the selected cell "empty"?
    if is_coord and if contents[cell_ind][0] != "-":
        cell_val = contents[cell_ind][0]
        checklist.append(contents[cell_ind]) #selected cell should be the first in the checklist
    else:
        print("Invalid Input! Try again.")
        coords_check(contents)
    
    #does the value in the selected cell have at least 2 possible matches?
    for _ in contents:
        if _[0] == cell_val:
            checklist.append(_)
            
    if len(checklist) >= 3:
        #does the value in the selected cell have at least 2 adjacent matches?
        iter_match(checklist)
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
