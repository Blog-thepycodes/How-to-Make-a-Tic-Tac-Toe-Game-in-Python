from tkinter import *
import random
 
 
def mark_cell(row, col):
   global current_player
   if board[row][col]['text'] == "" and not check_winner():
       board[row][col]['text'] = current_player
       if check_winner():
           highlight_winner()
           label.config(text=(current_player + " wins!"))
           update_score(current_player)
       elif check_tie():
           label.config(text="It's a tie!")
       else:
           current_player = next_player(current_player)
           label.config(text=(current_player + "'s turn"))
 
 
def highlight_winner():
   for i in range(3):
       if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != "":
           highlight_buttons([(i, 0), (i, 1), (i, 2)])
           return
       if board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != "":
           highlight_buttons([(0, i), (1, i), (2, i)])
           return
   if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
       highlight_buttons([(0, 0), (1, 1), (2, 2)])
       return
   if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
       highlight_buttons([(0, 2), (1, 1), (2, 0)])
       return
 
 
def highlight_buttons(coords):
   for coord in coords:
       row, col = coord
       board[row][col].config(bg='green')  # Change the color here
 
 
def check_winner():
   for i in range(3):
       if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != "":
           return True
       if board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != "":
           return True
   if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
       return True
   if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
       return True
   return False
 
 
def check_tie():
   for row in board:
       for button in row:
           if button['text'] == "":
               return False
   return True
 
 
def next_player(player):
   return players[(players.index(player) + 1) % 2]
 
 
 
def restart_game():
   global current_player
   for row in range(3):
       for col in range(3):
           board[row][col]['text'] = ""
           board[row][col].config(bg='SystemButtonFace')  # Reset button colors
   current_player = random.choice(players)
   label.config(text=(current_player + "'s turn"))
 
 
 
 
def update_score(player):
   if player == "X":
       x_score.set(x_score.get() + 1)
   else:
       o_score.set(o_score.get() + 1)
   score_label.config(text="Score - X: {}  O: {}".format(x_score.get(), o_score.get()))
 
 
 
 
root = Tk()
root.title("Simple Tic-Tac-Toe - The Pycodes")
 
 
players = ["X", "O"]
current_player = random.choice(players)
 
 
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
 
label = Label(text=(current_player + "'s turn"), font=('consolas', 40))
label.pack(side="top")
 
 
x_score = IntVar()
o_score = IntVar()
 
 
x_score.set(0)
o_score.set(0)
 
 
score_label = Label(text="Score - X: {}  O: {}".format(x_score.get(), o_score.get()), font=('consolas', 20))
score_label.pack(side="top")
 
 
restart_button = Button(text="Restart", font=('consolas', 20), command=restart_game)
restart_button.pack(side="top")
 
 
buttons_frame = Frame(root)
buttons_frame.pack()
 
 
for row in range(3):
   for col in range(3):
       board[row][col] = Button(buttons_frame, text="", font=('consolas', 50), width=4, height=1,
                                command=lambda row=row, col=col: mark_cell(row, col))
       board[row][col].grid(row=row, column=col)
 
root.mainloop()
