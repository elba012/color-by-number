import sys
import tkinter as tk
from grid1 import grid1, colors1
from grid2 import grid2, colors2
from grid3 import grid3, colors3
from choose_paint import OptionChooser
from tkinter import messagebox

# define level

colors = grid = None


def get_level():
    global colors, grid
    level = ""
    while level == "" and level != "quit":
        level = OptionChooser()
    print(level)
    if level == "Duck":
        colors, grid = colors1, grid1
    elif level == "Monkey":
        colors, grid = colors2, grid2
    elif level == "Super Mario":
        colors, grid = colors3, grid3


get_level()

if colors is None:
    sys.exit()


def clear_grid():
    for button in grid_buttons:
        button.config(bg="white", fg="black")


def auto_paint():
    for button in grid_buttons:
        text = button.cget("text")
        rgb_color1 = colors[int(text)]
        hex_color = "#{:02x}{:02x}{:02x}".format(rgb_color1[0], rgb_color1[1], rgb_color1[2])
        button.config(bg=hex_color, fg=hex_color)
    messagebox.showinfo("message", "You are such a lazy person")


def change_color(event):
    # Change the background color of the clicked button
    text = event.widget.cget("text")
    rgb_color1 = colors[int(text)]
    if "#{:02x}{:02x}{:02x}".format(rgb_color1[0], rgb_color1[1], rgb_color1[2]) == color:
        event.widget.config(bg=color, fg=color)
    check = True
    for button in grid_buttons:
        bg_color = button.cget("bg")
        if bg_color == "white":
            check = False
    if check:
        messagebox.showinfo("Congratulation", "Congratulations! You completed the paint successfully")


def print_color(hex_color):
    global color
    color = hex_color
    print(f"Clicked color: {color}")


root = tk.Tk()
root.title("Game")

top_frame = tk.Frame(root)
top_frame.pack()

color = "white"
# define grid
bottom_frame = tk.Frame(root)
bottom_frame.pack()

label = tk.Label(top_frame, text="Good Luck!")
label.pack()

grid_frame = tk.Frame(bottom_frame)
grid_frame.pack()

grid_buttons = []


def restart_program():
    global root, top_frame, bottom_frame, label, grid_frame, grid_buttons
    root.destroy()
    get_level()
    root = tk.Tk()
    root.title("Game")
    top_frame = tk.Frame(root)
    top_frame.pack()

    # define grid
    bottom_frame = tk.Frame(root)
    bottom_frame.pack()

    label = tk.Label(top_frame, text="Good Luck!")
    label.pack()

    grid_frame = tk.Frame(bottom_frame)
    grid_frame.pack()

    grid_buttons = []
    main()


def main():
    # Create a 15x15 grid of buttons
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                button = tk.Button(grid_frame, text=str(grid[i][j]), width=2, height=1)
                button.config(bg="white")
                button.grid(row=i, column=j, padx=0.5, pady=0.5)
                button.bind("<Button-1>", change_color)
                grid_buttons.append(button)

    # Create three buttons in the top frame using pack
    color_buttons = []
    for color_name, rgb_color in colors.items():
        hex_color = "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])
        if rgb_color[0] < 150 and rgb_color[1] < 150 and rgb_color[2] < 150:
            fg_color = "white"
        else:
            fg_color = "black"
        color_buttons.append(tk.Button(top_frame, text=color_name, bg=hex_color, fg=fg_color,
                                       width=2, height=1, command=lambda hex_color=hex_color: print_color(hex_color))
                             )
    for button in color_buttons:
        button.pack(padx=5, pady=5, side=tk.LEFT)
    clear_button = tk.Button(top_frame, text="Clear", bg="red", fg="white", width=5, height=1, command=clear_grid)
    clear_button.pack(padx=(10, 0), pady=5, side=tk.LEFT)
    auto_paint_button = tk.Button(top_frame, text="Auto Paint", bg="green", fg="white", width=9, height=1,
                                  command=auto_paint)
    auto_paint_button.pack(padx=(10, 0), pady=5, side=tk.LEFT)
    restart_button = tk.Button(top_frame, text="Back", bg="blue", fg="white", width=7, height=1,
                               command=restart_program)
    restart_button.pack(padx=5, pady=5, side=tk.LEFT)
    root.mainloop()


if __name__ == '__main__':
    main()
