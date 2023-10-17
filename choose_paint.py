import tkinter as tk


# create tkinter window for get Level
def OptionChooser():
    def submit():
        window.destroy()
        result.set(var.get())

    def on_closing():
        result.set("quit")
        window.destroy()

    window = tk.Tk()
    window.title("Level select")
    window.geometry("300x300")
    options = ["Duck", "Monkey", "Super Mario"]

    label = tk.Label(window, text="Choose a Paint:")
    label.pack()
    var = tk.StringVar()
    var.set(options[0])  # Default selection

    # Create radio buttons for each option
    for option in options:
        radio_button = tk.Radiobutton(window, text=option, variable=var, value=option)
        radio_button.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    result = tk.StringVar()

    window.mainloop()

    return result.get()
