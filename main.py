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

def check_winner():
    global turns, game_over
    turns += 1
    if turns > 4:
        if (check_horizontal_win() or check_vertical_win()):
            game_over = True
            return
    else:
        pass


def check_vertical_win():
    for column in range(3):
        if (board[0][column]["text"] != ""):
            if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]):
                print('Voittooooo')                




# Check if horizontal row contains three of the same symbols
def check_horizontal_win():
    # Iterate over all gameboard rows
    for row in range(3):
        # Ensure that the first cell is not empty
        if board[row][0]["text"] != "":
            # Check if the whole row is the same symbol
            if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]):
                print('voitto')
                label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
                # Change row color if win
                for column in range(3):
                    board[row][column].config(foreground=color_yellow, background=color_light_gray)    
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