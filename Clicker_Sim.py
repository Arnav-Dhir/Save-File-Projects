from tkinter import *
import time
import json
import os

# Important Variables

# GUI Variables
bg = Tk()
clicks = 0
click_counter = 1
auto_clicks = 0  # Variable for automatic clicks per second

# Money Variables
upgrade_1_cost = 20
upgrade_2_cost = 50  # Cost for the automatic upgrade
data_file = 'game_data.json'  # File to save game data


# Functions
def save_data():
    data = {
        'clicks': clicks,
        'click_counter': click_counter,
        'auto_clicks': auto_clicks,
        'upgrade_1_cost': upgrade_1_cost,
        'upgrade_2_cost': upgrade_2_cost,
    }
    with open(data_file, 'w') as f:
        json.dump(data, f)
    message_label.config(text="Game Saved!", background="#70a7ff", font=30)


def load_data():
    global clicks, click_counter, auto_clicks, upgrade_1_cost, upgrade_2_cost
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
            clicks = data.get('clicks', 0)
            click_counter = data.get('click_counter', 1)
            auto_clicks = data.get('auto_clicks', 0)
            upgrade_1_cost = data.get('upgrade_1_cost', 20)
            upgrade_2_cost = data.get('upgrade_2_cost', 50)

            label.config(text=f"Clicks: {clicks}")
            click_counter_label.config(text=f"Click Increment per Button Click: {click_counter}")
            auto_clicks_label.config(text=f"Automatic Clicks per Second: {auto_clicks}")
            upgrade_Button.config(text=f"Upgrade Clicks\nCost: {upgrade_1_cost} Clicks")
            upgrade_2_button.config(text=f"Upgrade Auto Clicks\nCost: {upgrade_2_cost} Clicks")
            message_label.config(text="Game Loaded!", background="#70a7ff", font=30)

def increase_clicks(labels):
    global clicks
    clicks += click_counter
    labels.config(text=f"Clicks: {clicks}")

def upgrade_1(labels):
    global click_counter
    global clicks
    global upgrade_1_cost

    if clicks >= upgrade_1_cost:
        clicks -= upgrade_1_cost
        click_counter += 1
        upgrade_1_cost = round(upgrade_1_cost * 1.5)  # round upgrade cost
        labels.config(text=f"Clicks: {clicks}")
        click_counter_label.config(text=f"Click Increment per Button Click: {click_counter}")
        message_label.config(text="Purchase Successful!", background="#70a7ff", font=30)
        upgrade_Button.config(text=f"Upgrade Clicks\nCost: {upgrade_1_cost} Clicks")
    else:
        message_label.config(text="Not Enough Clicks!", background="#70a7ff", font=30)

def upgrade_2(labels):
    global clicks
    global auto_clicks
    global upgrade_2_cost

    if clicks >= upgrade_2_cost:
        clicks -= upgrade_2_cost
        auto_clicks += 1  # Increase auto clicks by 1
        upgrade_2_cost = round(upgrade_2_cost * 1.5)  # round upgrade cost
        labels.config(text=f"Clicks: {clicks}")
        auto_clicks_label.config(text=f"Automatic Clicks per Second: {auto_clicks}")
        message_label.config(text="Automatic Upgrade Successful!", background="#70a7ff", font=30)
        upgrade_2_button.config(text=f"Upgrade Auto Clicks\nCost: {upgrade_2_cost} Clicks")
    else:
        message_label.config(text="Not Enough Clicks!", background="#70a7ff", font=30)

def auto_increment():
    global clicks
    while True:
        time.sleep(1)  # Wait for one second
        clicks += auto_clicks  # Increment clicks by the number of automatic clicks
        label.config(text=f"Clicks: {clicks}")


# Labels
label = Label(bg, text=f"Clicks: {clicks}", width=20, height=2, background="#70a7ff")
click_counter_label = Label(bg, text=f"Click Increment per Button Click: {click_counter}", width=30, height=2, background="#70a7ff")
auto_clicks_label = Label(bg, text=f"Automatic Clicks per Second: {auto_clicks}", width=30, height=2, background="#70a7ff")
message_label = Label(bg, text="Messages will appear here.", width=30, height=2, background="#70a7ff")

# Buttons
button = Button(bg, text="Click Me!", width=10, height=2, command=lambda: increase_clicks(label), background="#70a7ff")
upgrade_Button = Button(bg, text=f"Upgrade Clicks\nCost: {upgrade_1_cost} Clicks", width=10, height=2, command=lambda: upgrade_1(label), background="#70a7ff")
upgrade_2_button = Button(bg, text=f"Upgrade Auto Clicks\nCost: {upgrade_2_cost} Clicks", width=15, height=2, command=lambda: upgrade_2(label), background="#70a7ff")
save_button = Button(bg, text="Save Game", width=15, height=2, command=save_data, background="#70a7ff")
load_button = Button(bg, text="Load Game", width=15, height=2, command=load_data, background="#70a7ff")

# GUI Setup
bg.geometry("500x600")
bg.title("Clicker Simulator")
bg.config(background="#70a7ff")

# Packing the widgets
button.pack(pady=(200, 10))
upgrade_Button.pack(pady=(10, 0))
upgrade_2_button.pack(pady=(10, 0))
save_button.pack(pady=(10, 0))
load_button.pack(pady=(10, 0))
label.pack()
click_counter_label.pack()
auto_clicks_label.pack()
message_label.pack()

# Load initial data
load_data()

# Start the auto_increment function in a separate thread
import threading
auto_increment_thread = threading.Thread(target=auto_increment, daemon=True)
auto_increment_thread.start()

bg.mainloop()