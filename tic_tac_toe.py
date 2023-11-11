from tkinter import ttk
from tkinter import *
from functools import partial

player = 0
SPACE = -1
board = [SPACE for _ in range(9)]
mode = 0

def process_click(index: int, player: int) -> (str, int):
    if valid_move(index):
        board[index] = player
        if player == 1:
            message = "Player X's turn"
        elif player == 0:
            message = "Player O's turn"
        if not did_win(player):  
            if is_tied():
                return "It's a tie!", -1
            return message, (player + 1) % 2
        else:
            game_over = True
            frm.configure(style='TFrame.Win.TFrame')
            return f"Player {('X', 'O')[player]} wins! Game over. Reset the game to play again.", -1
    return "Invalid move", player

def valid_move(index: int) -> bool:
    if board[index] == SPACE:
        return True
    else:
        return False

def board_num_to_row_and_col(num: int) -> (int, int):
    return (num // 3, num % 3)

def possible_winning_triples() -> list:
    return [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def status_of_triple(triple: list) -> list:
    return [board[n] for n in triple]

def status_of_all_winning_triples() -> list:
    return [status_of_triple(triple) for triple in possible_winning_triples()]

def did_win(player: int) -> bool:
    for triple in status_of_all_winning_triples():
        if len(set(triple)) == 1 and triple[0] == player:
            return True
    return False

def is_tied() -> bool:
    return all(board[space] != SPACE for space in range(9))
EASY_MOVES = {0, 1, 2, 3, 4, 5, 6, 7, 8}

   
def autoplay(player: int) -> int:
    global difficulty
    if difficulty == "easy":
        for triple in possible_winning_triples():
            status = status_of_triple(triple)
            if status.count(player) == 2 and status.count(SPACE) == 1:
                return triple[status.index(SPACE)]
        opponent = (player + 1) % 2
        for triple in possible_winning_triples():
            status = status_of_triple(triple)
            if status.count(opponent) == 2 and status.count(SPACE) == 1:
                return triple[status.index(SPACE)]
            available_moves = [i for i in range(9) if board[i] == SPACE]
        return triple[status.index(SPACE)]
        
        
    elif difficulty == "medium":
        for triple in possible_winning_triples():
            status = status_of_triple(triple)
            if status.count(player) == 2 and status.count(SPACE) == 1:
                return triple[status.index(SPACE)]
        opponent = (player + 1) % 2
        for triple in possible_winning_triples():
            status = status_of_triple(triple)
            if status.count(opponent) == 2 and status.count(SPACE) == 1:
                return triple[status.index(SPACE)]
        available_moves = [i for i in range(9) if board[i] == SPACE]
        return triple[status.index(SPACE)]
        for triple in possible_winning_triples():
            status = status_of_triple(triple)
            if status.count(player) == 1 and status.count(SPACE) == 2:
                return triple[status.index(SPACE)]
    
    elif difficulty == "hard":
      for triple in possible_winning_triples():
          status = status_of_triple(triple)

          if status.count(player) == 2 and status.count(SPACE) == 1:
              return triple[status.index(SPACE)]
      opponent = (player + 1) % 2
      for triple in possible_winning_triples():
          status = status_of_triple(triple)
          if status.count(opponent) == 2 and status.count(SPACE) == 1:
              return triple[status.index(SPACE)]
      for triple in possible_winning_triples():
          status = status_of_triple(triple)
          if status.count(player) == 1 and status.count(SPACE) == 2:
              return triple[status.index(SPACE)]
      if board[4] == SPACE:
          return 4
      for corner in [0, 2, 6, 8]:
          if board[corner] == SPACE:
              return corner
      for i in range(9):
          if board[i] == SPACE:
              return i
    
        
                   
    return -1




buttons = []
BUTTON_WIDTH = 4
BUTTON_HEIGHT = 2

root = Tk()
s = ttk.Style()
s.theme_use('classic')
s.configure('TFrame', background='pink')
s.configure('TLabel', background='pink', foreground='black', font=("Comic Sans MS", 20))

frm = ttk.Frame(root, padding=20, style='TFrame')
s.configure('TFrame.Win.TFrame', background='lightgreen')
s.configure('TLabel.Win.TLabel', background='lightgreen', foreground='black', font=("Comic Sans MS", 20))

frm.grid()
ttk.Label(frm, text='Tic-Tac-Toe', font=("Ariel", 36)).grid(row=0, column=0, columnspan=3)

message = ttk.Label(frm, text="Player X's turn", font=("Ariel", 16))
message.grid(row=5, column=0, columnspan=3)

def register_click(index: int):
    global player
    original_player = player
    response, player = process_click(index, player)
    if response != "Invalid move":
        if original_player == 0:
            buttons[index].configure(text="X")
        else:
            buttons[index].configure(text="O")
    message.configure(text=response)
    root.update()
    if mode == 1 and player == 1 and response == "Player O's turn":
        move = autoplay(player)
        if move != -1:
            register_click(move)

def reset_game():
    global board
    global player
    player = 0
    board = [-1 for _ in range(9)]
    for button in buttons:
        button.configure(text="")
    message.configure(text="Player X's turn")
    frm.configure(style='TFrame')
    root.update()

for i in range(9):
    b = Button(frm, text=' ', font=("Ariel", 36), width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=partial(register_click, i))
    buttons.append(b)
    b.grid(row=i // 3 + 1, column=i % 3)

ttk.Label(frm, text='', font=("Ariel", 12)).grid(row=4, column=0, columnspan=3)

def set_difficulty(selected_difficulty):
    global difficulty
    difficulty = selected_difficulty
    print(f"Difficulty set to {difficulty}")
def set_easy():
    set_difficulty("easy")

def set_medium():
    set_difficulty("medium")
    
def set_hard():
    set_difficulty("hard")

ttk.Label(frm, text='', font=("Ariel", 12)).grid(row=6, column=0, columnspan=3)
easy_button = ttk.Button(frm, text="Easy", command=set_easy)
medium_button = ttk.Button(frm, text="Medium", command=set_medium)
hard_button = ttk.Button(frm, text="Hard", command=set_hard)


    
    


def toggle_mode():
    global mode
    reset_game()
    mode = (mode + 1) % 2
    if mode == 0:
        mode_button.configure(text="Switch to Single Player")
        easy_button.grid_forget()
        medium_button.grid_forget()
        hard_button.grid_forget()
    else:
        mode_button.configure(text="Switch to Two Player")
        easy_button.grid(row=8, column=0)
        medium_button.grid(row=8, column=1)
        hard_button.grid(row=8, column=2)
    root.update()

mode_button = ttk.Button(frm, text="Switch to Single Player", command=toggle_mode)
mode_button.grid(row=7, column=0, columnspan=2)
ttk.Button(frm, text="Reset", command=reset_game).grid(row=7, column=2)

root.mainloop()