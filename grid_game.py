##### LATEST AS OF SEPTEMBER 7, 2020
import random
from collections import Counter

def rand_gen(K):
    num = random.randint(0,K-1)
    return num

def score(match_len):
    score = (match_len - 2)**2
    return score

def grid_gen(M,N,row_label,col_label,contents): #parameters: M,N,row_label,col_label,contents
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
    
    return 0

def grid_update(matches, contents):
    #fxn that updates the contents list to reflect "dropped" cells
    updated_contents = contents.copy()

    for cell in updated_contents:
        if cell in matches:
            cell[0] = "-"
        else:
            continue
           
    for cell in updated_contents:
        for ff in updated_contents:
            if cell[0] != "-" and ff[0] == "-" and ff[1] == cell[1]+1 and ff[2] == cell[2]:
                ff[0] = cell[0]
                cell[0] = "-"
            elif cell[0] == "-" and ff[0] != "-" and ff[1] == cell[1]-1 and ff[2] == cell[2]:
                cell[0] = ff[0]
                ff[0] = "-"
                
        
    #print("updated_contents:", updated_contents)
    return updated_contents

def adj_check(basis, contents, checklist):
    #fxn that looks for the adjacent matches

    in_check = checklist.copy()
    matches = [] #matches of selected cell, including selected cell
    count = len(checklist)
    
    #print("checklist:", checklist)
    while count > 0:
        for item in checklist:
            if item == basis:
                matches.append(item)
                for cell in in_check:
                    if (cell[1] == item[1] + 1) and (cell[2] == item[2]) and cell not in matches:#bottom
                        matches.append(cell)
                    elif (cell[1] == item[1] - 1) and (cell[2] == item[2]) and cell not in matches:#top
                        matches.append(cell)
                    elif (cell[1] == item[1]) and (cell[2] == item[2] + 1) and cell not in matches:#right
                        matches.append(cell)
                    elif (cell[1] == item[1]) and (cell[2] == item[2] - 1) and cell not in matches:#left
                        matches.append(cell)
            else:
                for cell in in_check:
                    for item in matches:
                        if (cell[1] == item[1] + 1) and (cell[2] == item[2]) and cell not in matches:#bottom
                            matches.append(cell)
                        elif (cell[1] == item[1] - 1) and (cell[2] == item[2]) and cell not in matches:#top
                            matches.append(cell)
                        elif (cell[1] == item[1]) and (cell[2] == item[2] + 1) and cell not in matches:#right
                            matches.append(cell)
                        elif (cell[1] == item[1]) and (cell[2] == item[2] - 1) and cell not in matches:#left
                            matches.append(cell)
            count = count -1
    
    #print("matches:", matches)
    return matches

def coords_check(contents, points):
    #fxn that checks whether the User input for selected cell is valid
    r = int(input("Please input the row number: "))
    c = int(input("Please input the col number: "))
    is_valid = False
    cell_index = 0
    checklist = []
    selected = 0
    update = None
    
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
        coords_check(contents, points)
            
    #is the cell empty?
    if cell_value != "-":
        checklist.append(contents[cell_index])
    else:
        print("Selected cell is empty. Try again!")
        coords_check(contents, points)
    
    #what are the adjacent matches?
    for cell in contents:
        if cell[0] == cell_value and contents.index(cell) != cell_index:
            checklist.append(cell)
    
    #are there enough potential matches?
    if len(checklist) >= 3:
        is_checked = adj_check(selected, contents, checklist)
        if selected in is_checked and len(is_checked) >= 3:
            print("VALID SELECTION!")
            points += score(len(is_checked))
            update = grid_update(is_checked, contents)
            print("Score: ", points)
            print("\n")
        else:
            print("Not enough adjacent matches. Try again!")
            coords_check(contents, points)
    else:
        print("Not enough possible matches. Try again!")
        coords_check(contents, points)

    return [update, points]

def is_game(contents):
    #fxn that checks whether there are any possible plays in the current round
    #basically, this should just check whether any displayed value has more than 2 occurrences
    cell_values = [i[0] for i in contents if i[0] != "-"]
    count = Counter(cell_values)
    validity = False
    for value in count.values():
        if value >= 3:
            validity = True
            break
    return validity

def set_up():
    M = int(input("no. of rows: "))
    N = int(input("no. of cols: "))
    K = int(input("boundary no: "))
    
    row_label = [j for j in range(M)]
    col_label = [i for i in range(N)]    
    contents = [[rand_gen(K),row,col] for row in row_label for col in col_label]
    score = 0
    
    row_label.insert(0, " ")
    print(contents)
    print("\nGame on!\n")
    print("\nScore: ", score)
    
    while is_game(contents):
        grid_gen(M,N,row_label,col_label,contents)
        play = coords_check(contents, score)
        contents = play[0]
        score = play[1]
        

    print("Game over! No more possible plays. Input 1 to play again. Input 0 to stop playing.")
    in_play = int(input("Would you like to start a new game? "))
    if in_play:
        set_up()
    else:
        print("Thank you for playing!")

set_up()
