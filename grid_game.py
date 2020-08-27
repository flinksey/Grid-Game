import random
from collections import Counter

def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def adj_check(contents, checklist):
    #fxn that looks for the adjacent matches
    return 0

def coords_check(contents):
    #fxn that checks whether the User input for selected cell is valid
    r = int(input("Please input the row number: "))
    c = int(input("Please input the col number: "))
    cell_index = 0
    is_valid = False
    checklist = []
    
    #are the coordinates within range?
    for coord in contents:
        if coord[1] == r and coord[2] == c:
            cell_index = contents.index(coord)
            cell_value = coord[0]
            is_valid = True
        else:
            print("Input out of bounds. Try again!")
            coords_check(contents)
            
    #is the cell empty?
    if is_valid and cell_value != "-":
        checklist.append(contents[cell_index])
    else:
        print("Selected cell is empty. Try again!")
        coords_check(contents)
        
    for cell in contents:
        if cell[0] == cell_value:
            checklist.append(cell)
    
    #are there enough potential matches?
    if len(checklist) >= 3:
        adj_check(contents, checklist)
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
       #     set_up() #ERROR: fxn defined before set_up() ---> this is a problem for MUCH later
       # else:
       #     end_game()

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
    
    play(contents)

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
