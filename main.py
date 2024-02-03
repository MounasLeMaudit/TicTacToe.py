import tkinter

def check_nul():
    print("Match nul")


def print_winner():
    global win
    if win is False:
        win = True
        print("le joueur", current_player, "a gagné le jeu")


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def win_check(clicked_row, clicked_column):
    count = 0
    for i in range(3):
        current_button = buttons[clicked_column][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
    
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
    
    count = 0
    for i in range(3):
        current_button = buttons[i][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
    
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == 'O':
                    count += 1
        print(count)
        if count == 9:
            print("Match nul")


def x_or_o(j, i):
    print("click", j, i)

    clicked_button = buttons[i][j]
    if clicked_button['text'] == "":
        clicked_button.config(text=current_player)

    win_check(j, i)
    switch_player()


def grille():
    for i in range(3):
        buttons_tmp = []
        for j in range(3):
            button = tkinter.Button(
                window, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=j, c=i: x_or_o(r, c)
                )
            button.grid(row=j, column=i)
            buttons_tmp.append(button)
        buttons.append(buttons_tmp)

buttons = []
current_player = 'X'
win = False

window = tkinter.Tk()
window.title("GAME #001")
window.minsize(500, 500)
window.configure(bg='grey')


grille()
window.mainloop()

