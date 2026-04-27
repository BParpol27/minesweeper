import numpy as np
import difficulty as df

def generate_hidden_field(difficulty):
    size, num_mines = df.unpack_difficulty(difficulty)
    field = np.zeros(size, dtype=int) 
    
    indexes = np.random.choice(size[0]*size[1], num_mines, replace = False)
    
    for item in indexes:
        x,y = divmod(item,size[1])
        field[x,y] = 9 # 9 representa una mina
        
    for row in range(size[0]):
        for col in range(size[1]):
            if field[row,col] == 9:
                continue
            else:
                num_mines_surrounding = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0 <= row + i < size[0] and 0 <= col + j < size[1]:
                            if field[row + i, col +j] == 9:
                                num_mines_surrounding += 1
                field[row,col]=num_mines_surrounding
            
    return field

def generate_visible_field(difficulty):
    size, num_mines = df.unpack_difficulty(difficulty)
    field = np.zeros(size, dtype=str)
    for row in range(size[0]):
        for col in range(size[1]):
            field[row, col] = "□"
            
    return field

def print_field(field):
    filas, columnas = field.shape
    ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("X ", end="")
    for i in range(columnas):
        print(f"{ABC[i]}", end=" ")
    print()
     
    for row in range(filas):
        print(f"{abc[row]} ", end="")
        for col in range(columnas):
            print(f"{field[row,col]}", end=" ")
        print()