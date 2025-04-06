# This project isn't finished.

from tkinter import *

# Important Variables
bg = Tk()
clicks = 0
click_counter = 1


# Functions
def increase_clicks(labels):
    global clicks
    clicks += click_counter
    labels.config(text=f"Clicks: {clicks}")


def upgrade_1():
    # This is a click upgrade; click_counter goes up by 1
    global click_counter
    click_counter += 1


# Other Variables

# Labels
label = Label(bg, text=f"Clicks: {clicks}", width=10, height=2)
click_counter_label = Label(bg, text=f"Click Increment per Button Click: {click_counter}", width=23, height=2)

# Buttons
button = Button(bg, text="Click Me!", width=10, height=2, command=lambda: increase_clicks(label))
upgrade_Button = Button(bg, text="Upgrade Clicks", width=10, height=2, command=lambda: upgrade_1())

# GUI Setup
bg.geometry("500x500")
bg.title("Clicker Simulator")
bg.config(background="#70a7ff")

button.pack()
button.config(background="#70a7ff")

upgrade_Button.pack()
upgrade_Button.place(x=375, y=30)
upgrade_Button.config(background="#70a7ff")

label.pack()
label.place(x=45, y=450)
label.config(background="#70a7ff")

click_counter_label.pack()
click_counter_label.place(x=250, y=450)
click_counter_label.config(background="#70a7ff")

bg.mainloop()
