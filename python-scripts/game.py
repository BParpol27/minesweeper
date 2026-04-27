from difficulty import unpack_difficulty
import numpy as np

def choose_action(field):
    available_actions = ["f", "df", "r"]
    if not np.any(np.isin(field, "F")):
        available_actions.remove("df")
        
    action = input("Choose your next action (Reveal - r / Flag - f / De-flag - df): ").lower()
    while action not in available_actions:
        action = input("Invalid action, please re-enter it (Reveal - r / Flag - f / De-flag - df): "). lower()

    return action

def ask_coordinates(difficulty, field, action):
    size = unpack_difficulty(difficulty)[0]
    ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ABC = ABC[:size[1]]
    abc = abc[:size[0]]
    
    col = input("Enter the x-coordinate: ").upper()
    while col not in ABC:
        col = input("Invalid x-coordinate, please re-enter it: ").upper()
    row = input("Enter the y-coordinate: ").lower()
    while row not in abc:
        row = input("Invalid y-coordinate: please re-enter it: ").lower()
    
    col = ABC.index(col)
    row = abc.index(row)
    
    if action != "df":
        while field[row, col] != "□":
            print("Those coordinates were already used")
            col = input("Enter the x-coordinate: ").upper()
            while col not in ABC:
                col = input("Invalid x-coordinate, please re-enter it: ").upper()
            row = input("Enter the y-coordinate: ").lower()
            while row not in abc:
                row = input("Invalid y-coordinate: please re-enter it: ").lower()
            col = ABC.index(col)
            row = abc.index(row)
    else:
        while field[row, col] != "F":
            print("Those coordinates don't have a flag. Choose another one")
            col = input("Enter the x-coordinate: ").upper()
            while col not in ABC:
                col = input("Invalid x-coordinate, please re-enter it: ").upper()
            row = input("Enter the y-coordinate: ").lower()
            while row not in abc:
                row = input("Invalid y-coordinate: please re-enter it: ").lower()
            col = ABC.index(col)
            row = abc.index(row)
        
    return row, col

def reveal_zeros(vis_field, hid_field, row, col, size, visited):
    # Evitar repetir casillas
    if (row, col) in visited:
        return

    visited.add((row, col))
    vis_field[row, col] = hid_field[row, col]

    # Si es un 0, propaga la revelación
    if hid_field[row, col] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nr, nc = row + i, col + j
                if 0 <= nr < size[0] and 0 <= nc < size[1]:
                    reveal_zeros(vis_field, hid_field, nr, nc, size, visited)
                    
def play(difficulty, vis_field, hid_field, revealed_squares, win, loose):
    action = choose_action(vis_field)
    row, col = ask_coordinates(difficulty, vis_field, action)
    size, num_mines = unpack_difficulty(difficulty)
    zero = False
    if action == "f":
        vis_field[row, col] = "F"
    elif action == "df":
        vis_field[row, col] = "□"
    else:
        if hid_field[row, col] == 9:
            loose = True
            vis_field[row, col] = "💣"
        else:
            visited = set()
            reveal_zeros(vis_field, hid_field, row, col, size, visited)
            revealed_squares += len(visited)

            
                
    remaining_squares = size[0] * size[1] - num_mines - revealed_squares
    if remaining_squares == 0:
        win = True
        
    return vis_field, loose, revealed_squares, win
                
                
    
        
    
    

