import tkinter as tk


def Tetris():
    from Tetris import tetris
    tetris.main_menu(tetris.win)


def PacMan():
    from Pacman import pacman
    pacman.pac()


def DonkeyKong():
    pass


def Snake():
    from Snake import snake
    snake.snek()


root = tk.Tk()
root.title("Retro Library")
root.geometry("1200x900")
root.configure(bg="black")

label = tk.Label(root, text="Retro Library", bg="black", fg="green", font=("Courier", 44))
label.pack(padx=20, pady=20)

button_1 = tk.Button(root, text="Tetris", bg="green", fg="red", font=("Courier", 44), command=Tetris)
button_1.pack(padx=20, pady=50)

button_2 = tk.Button(root, text="Pac Man", bg="green", fg="red", font=("Courier", 44), command=PacMan)
button_2.pack(padx=20, pady=50)

button_3 = tk.Button(root, text="Donkey Kong", bg="green", fg="red", font=("Courier", 44), command=DonkeyKong)
button_3.pack(padx=20, pady=50)

button_4 = tk.Button(root, text="Snake", bg="green", fg="red", font=("Courier", 44), command=Snake)
button_4.pack(padx=20, pady=50)

root.mainloop()
