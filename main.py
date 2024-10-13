import tkinter

# Create main menu window
def create_main_menu():
    # Player options for dropdown
    player_options = ["Human player", "MiniMax"]

    # Label for the title
    label_hi = tkinter.Label(window, text="Welcome to Tic Tac Toe", font=("Arial", 15))
    label_hi.grid(row=0, column=0, columnspan=2, pady=20)

    # Label and OptionMenu for Player 1
    label_p1 = tkinter.Label(window, text="Player 1:", font=("Arial", 12))
    label_p1.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    # StringVar to hold the selected player option
    player1_var = tkinter.StringVar()
    player1_var.set(player_options[0])

    # Create styled OptionMenu for Player 1
    player1_selection = tkinter.OptionMenu(window, player1_var, *player_options)
    player1_selection.grid(row=1, column=1, padx=10, pady=10)

    # Label and OptionMenu for Player 2
    label_p2 = tkinter.Label(window, text="Player 2:", font=("Arial", 12))
    label_p2.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    player2_var = tkinter.StringVar()
    player2_var.set(player_options[0])

    # Create styled OptionMenu for Player 2
    player2_selection = tkinter.OptionMenu(window, player2_var, *player_options)
    player2_selection.grid(row=2, column=1, padx=10, pady=10)

    # Start game button
    start_button = tkinter.Button(window, text="Start New Game", command=start_game, font=("Arial", 15))
    start_button.grid(row=3, column=0, columnspan=2, pady=20)

# Bring out the main menu from game board
def back_to_menu():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()
    # return to the menu
    create_main_menu()

# Bring out the game board
def start_game():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()
    # Open the game board
    create_game_board()

def create_game_board():
    global board, current_player, label, player_x, player_o, turns, game_over

    player_x = "X"
    player_o = "O"
    current_player = player_x
    turns = 0
    game_over = False

    # Create a label to display the current player's turn
    label = tkinter.Label(window, text=current_player + "'s turn", font=("Helvetica", 15))
    label.grid(row=0, column=0, columnspan=3)

    # Create the 3x3 grid
    board = [[0,0,0], [0,0,0], [0,0,0]]
    for row in range(3):
        for column in range(3):
            board[row][column] = tkinter.Button(window, text="", font=("arial", 40, "bold"), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=column: set_title(row, column))
            board[row][column].grid(row=row+1, column=column)

    back_to_menu_btn = tkinter.Button(window, text="Back to menu", font=("arial", 20), background=color_gray, foreground="white", command=back_to_menu)
    back_to_menu_btn.grid(row=4, column=0, columnspan=3, sticky="we")


            
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


# Initialize colors
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#434343"
color_light_gray = "#646464"

# Main window
window = tkinter.Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x_coordinate = int((screen_width/2) - (window_width/2))
window_y_coordinate = int((screen_height/2.2) - (window_height/2))

window.geometry(f"+{window_x_coordinate}+{window_y_coordinate}")

create_main_menu()

window.mainloop()