import tkinter

def set_title(row, column):
    global current_player
    selected_button = board[row][column]

    if selected_button["text"] != "":
        return
    
    selected_button["text"] = current_player
    if current_player == player_x:
        current_player = player_o
    else:
        current_player = player_x

    label["text"] = current_player + "'s turn"
    check_winner()
    pass

def new_game():
    print("reset pressed")
    pass

# Check if the game has a winner
def check_winner():
    global turns, game_over
    turns += 1
    # Game can not be won with less than 5 total turns
    if turns > 4:
        # Check all possible ways of winning
        if (check_horizontal_win() or check_vertical_win() or check_diagonal_win()):
            game_over = True
            return
    else:
        pass

# Announce winner on the gameboard
def announce_winner(winner):
    # Change label to winner's symbol
    label.config(text=winner["symbol"]+" is the winner!", foreground=color_yellow)
    # Change color to indicate winning cells
    for cell in winner["winning_cells"]:
        cell.config(foreground=color_yellow, background=color_light_gray)
    return


# Check for horizontal wins
def check_vertical_win():
    # Iterate over all columns
    for column in range(3):
        # Check if all column cells contain same symbol and ensure the first cell is not empty
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            # Announce winner if all column cells contained the same symbol
            announce_winner({
                "winning_cells": [board[0][column], board[1][column], board[2][column]],
                "symbol": board[0][column]["text"]
            })
            return           


# Check for diagonal wins
def check_diagonal_win():
    # Initialize function to iterate over diagonal cells
    def check_diagonal(cells):
        # Check if all diagonal cells contain same symbol and ensure the first cell is not empty
        if cells[0]["text"] == cells[1]["text"] == cells[2]["text"] and cells[0]["text"] != "":
            # Announce winner if all diagonal cells contained the same symbol
            announce_winner({
                "winning_cells": cells,
                "symbol": cells[0]["text"]
            })
    # Call function to check diagonals
    check_diagonal([board[0][0], board[1][1], board[2][2]])  # upper left to bottom right
    check_diagonal([board[0][2], board[1][1], board[2][0]])  # bottom left to upper right


# Check for horizontal wins
def check_horizontal_win():
    # Iterate over all rows
    for row in range(3):
        # Check if all row cells contain same symbol and ensure the first cell is not empty
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            # Announce winner if all row cells contained the same symbol
            announce_winner({
                "winning_cells": [board[row][0], board[row][1], board[row][2]],
                "symbol": board[row][0]["text"]
            })
            return


# Initialize new game
player_x = "X"
player_o = "O"
turns = 0
game_over = False

current_player = player_x
board = [[0,0,0], [0,0,0], [0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#434343"
color_light_gray = "#646464"

# Game window
window = tkinter.Tk()
window.title = "Tic Tac Toe"
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = current_player +"'s turn", background=color_gray, font=("arial", 20), foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("arial", 50, "bold"), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart", font=("arial", 20), background=color_gray, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x_coordinate = int((screen_width/2) - (window_width/2))
window_y_coordinate = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x_coordinate}+{window_y_coordinate}")

window.mainloop()