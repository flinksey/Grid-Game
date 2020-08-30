import random
from collections import Counter

def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def grid_update():
    return 0

def adj_check(basis, contents, checklist):
    #fxn that looks for the adjacent matches
    #print("adj_check has run.")
    #NEED TO: comment out or remove print statements for testing
    
    #NEED TO EDIT: so that we only check the adj matches of those that are adj matches of the selected cell
    in_check = checklist.copy()
    matches = [] #matches of selected cell, including selected cell
    sel_matches = [basis] #dummy var just to keep track of the ones matching for the first run
    count = len(checklist)
    
    print("checklist:", checklist)
    while count > 0:
        for item in checklist:
            if item == basis:
                for cell in in_check:
                    if (cell[1] == item[1] + 1) and (cell[2] == item[2]) and cell not in matches:#bottom
                        matches.append(cell)
                    elif (cell[1] == item[1] - 1) and (cell[2] == item[2]) and cell not in matches:#top
                        matches.append(cell)
                    elif (cell[1] == item[1]) and (cell[2] == item[2] + 1) and cell not in matches:#right
                        matches.append(cell)
                    elif (cell[1] == item[1]) and (cell[2] == item[2] - 1) and cell not in matches:#left
                        matches.append(cell)
            elif item != basis: #item in matches:
                for cell in matches:
                    if (cell[1] == item[1] + 1) and (cell[2] == item[2]) and cell != basis:#bottom
                        sel_matches.append(cell)
                    elif (cell[1] == item[1] - 1) and (cell[2] == item[2]) and cell != basis:#top
                        sel_matches.append(cell)
                    elif (cell[1] == item[1]) and (cell[2] == item[2] + 1) and cell != basis:#right
                        sel_matches.append(cell)
                    elif (cell[1] == item[1]) and (cell[2] == item[2] - 1) and cell != basis:#left
                        sel_matches.append(cell)
            count = count -1
            
    print("checklist:", checklist)
    print("sel_matches:", matches)
    
    return matches

def coords_check(contents):
    #fxn that checks whether the User input for selected cell is valid
    #NEED TO ACCOUNT FOR: if the selected cell is not in the matches list, then User must select a new cell
    r = int(input("Please input the row number: "))
    c = int(input("Please input the col number: "))
    is_valid = False
    cell_index = 0
    checklist = []
    selected = 0
    
    #are the coordinates within range?
    for coord in contents:
        if coord[1] == r and coord[2] == c:
            cell_index = contents.index(coord)
            cell_value = coord[0]
            selected = coord
            is_valid = True
            break
    if is_valid == False:
        print("Input out of bounds. Try again!")
        coords_check(contents)
            
    #is the cell empty?
    if cell_value != "-":
        checklist.append(contents[cell_index])
    else:
        print("Selected cell is empty. Try again!")
        coords_check(contents)
    
    #what are the adjacent matches?
    for cell in contents:
        if cell[0] == cell_value and contents.index(cell) != cell_index:
            checklist.append(cell)
    
    #are there enough potential matches?
    if len(checklist) >= 3:
        is_checked = adj_check(selected, contents, checklist)
        if selected in is_checked and len(is_checked) >= 3:
            print("VALID SELECTION!")
            #grid_update()
        else:
            print("Not enough adjacent matches. Try again!")
            coords_check(contents)
    else:
        print("Not enough possible matches. Try again!")
        coords_check(contents)

def is_game(contents):
    #fxn that checks whether there are any possible plays in the current round
    #basically, this should just check whether any displayed value has more than 2 occurrences
    cell_values = [i[0] for i in contents]
    count = Counter(cell_values)
    validity = False
    for value in count.values():
        if value >= 3:
            validity = True
            break
    return validity

def play(contents):
    in_play = is_game(contents)
    if in_play:
        coords_check(contents)
    else:
        #assumes User is not trolling
        print("Game over! No more possible plays. Input 1 to play again. Input 0 to stop playing.")
       # play_again = int(input("Would you like to start a new game? "))
       # if play_again == 1:
       #     set_up() #ERROR: fxn defined before set_up()
       # else:
       #     end_game()

def grid_gen(M,N,row_label,col_label,contents): #parameters: M,N,row_label,col_label,contents
    #fxn that generates the grid each time (from beginning through udpates)
    #comment out test case
    
    #M = 3
    #N = 2
    #row_label = [i for i in range(3)]
    #col_label = [j for j in range(2)]
    #row_label.insert(0," ")
    #contents = [[0, 0, 0], [2, 0, 1], [2, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1]]
    
    for row in range(M+1):
        print(row_label[row], end = "  ")
        if row == 0:
            for col in range(N):
                print(col_label[col], end = "  ")
        else:
            for col in range(N):
                print(contents[(row-1)*N + col][0], end = "  ")
        print("  ")
    
    play(contents)

def set_up():
    M = int(input("no. of rows: "))
    N = int(input("no. of cols: "))
    K = int(input("boundary no: "))
    
    row_label = [j for j in range(M)]
    col_label = [i for i in range(N)]    
    contents = [[rand_gen(K),row,col] for row in row_label for col in col_label]
    
    row_label.insert(0, " ")
    print(contents)
    print("\nGame on!\n")
    
    grid_gen(M,N,row_label,col_label,contents)

#grid_gen()
set_up()
