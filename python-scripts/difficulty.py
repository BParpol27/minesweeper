def set_difficulty():
    available_difficulties = ["easy", "medium", "hard"]
    difficulty = input("Enter the difficulty (Easy / Medium / Hard): ").lower()
    while difficulty not in available_difficulties: 
        difficulty = input("Invalid difficulty, please re-enter it (Easy / Medium / Hard): ")
    return difficulty

def unpack_difficulty(difficulty):
    if difficulty == "easy":
        size = (9,10)
        num_mines = 15
    elif difficulty == "medium":
        size = (12,13)
        num_mines = 45
    elif difficulty == "hard":
        size = (19,20)
        num_mines = 120
        
    return size, num_mines