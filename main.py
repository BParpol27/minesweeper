# Buscaminas
# Ramón Vicente Rodríguez

import difficulty as df
import field as fld
import game

difficulty = df.set_difficulty()
size = df.unpack_difficulty(difficulty)[0]

visible_field = fld.generate_visible_field(difficulty)
fld.print_field(visible_field)
row, col = game.ask_coordinates(difficulty, visible_field, "r")
hidden_field = fld.generate_hidden_field(difficulty)

while hidden_field[row, col] != 0:
    hidden_field = fld.generate_hidden_field(difficulty)
    
fld.print_field(hidden_field)

print("\n\n")

visited = set()
game.reveal_zeros(visible_field, hidden_field, row, col, size, visited)
revealed_squares = len(visited)


fld.print_field(visible_field)
    
loose = False
win = False
while loose == False and win == False:
    visible_field, loose, revealed_squares, win = game.play(difficulty, visible_field, hidden_field, revealed_squares, win, loose)
    fld.print_field(visible_field)
    

    
if win == True:
    print("You won")
elif loose == True:
    print("You lost")
else:
    print("Que coño ha pasado aquí")


