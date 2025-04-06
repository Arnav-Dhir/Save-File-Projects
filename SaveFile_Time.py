import os
import random
import sys
import time
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

# Absolute Path Is Private.
time_file = "time_file.txt"
log_file = "log_file.txt"

ticktock = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Spent")
        self.setGeometry(0, 0, 0, 1000)

        # Initialize the labels
        self.ticktock_label = QLabel(f"Time Spent: {ticktock} seconds", self)
        self.logout_label = QLabel(f"Last Logout: Not available", self)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.ticktock_label)
        layout.addWidget(self.logout_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def update_ui(self):
        self.ticktock_label.setText(f"Time Spent: {ticktock + 1} seconds")

        # Update the last logout label
        last_logout_time = load_last_logout_time()
        if last_logout_time:
            self.logout_label.setText(f"Last Logout: {last_logout_time}")
        else:
            self.logout_label.setText(f"Last Logout: Not available")

    def closeEvent(self, event):
        # This method is triggered when the window is closed (either by clicking the close button or programmatically).
        print("Window close event triggered.")
        self.save_time_on_exit()
        event.accept()  # Accept the event, allowing the window to close

    def save_time_on_exit(self):
        # Function to save time and handle logout time
        print("Saving Time...")
        time.sleep(random.randint(5, 30) / 10)
        print("Saved Time.")
        print(f"Time Spent: {ticktock} seconds")

        save_logout_time()

        reset = input("Do you want to reset your data? (yes/no): ")

        if reset.lower() == "yes":
            reset_data()
        elif reset.lower() == "no":
            print("Saved Time Stored.")
        else:
            print('Invalid Response.')

        print('Disconnecting from server...')
        sys.exit('Successfully exited from server.')


def load_time():
    if os.path.exists(time_file):
        with open(time_file, 'r') as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0


def save_time(times):
    with open(time_file, "w") as file:
        file.write(str(times))


def reset_data():
    print("Attempting to reset data...")

    try:
        if os.path.exists(time_file):
            os.remove(time_file)

        if os.path.exists(log_file):
            os.remove(log_file)
    except Exception as e:
        print(f"Error removing files: {e}")


def load_last_logout_time():
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            return file.read().strip()
    return None


def save_logout_time():
    current_time = datetime.now().strftime("%H:%M")
    with open(log_file, 'w') as file:
        file.write(current_time)


def main():
    global ticktock

    app = QApplication(sys.argv)
    window = MainWindow()

    # Load previous time if available
    ticktock = load_time()

    # Show last logout time in the GUI
    last_logout_time = load_last_logout_time()
    if last_logout_time:
        print(f"Last logged out at: {last_logout_time}")

    window.update_ui()  # Update the UI with last logout and ticktock

    window.show()

    try:
        while True:
            time.sleep(1)
            ticktock += 1
            print(f"Time: {ticktock} seconds", end='\r')
            save_time(ticktock)

            # Update the GUI to reflect the new time
            window.update_ui()
            app.processEvents()  # Make sure the GUI updates

    except KeyboardInterrupt:
        print("\nSaving Time...")
        time.sleep(random.randint(5, 30) / 10)
        print("Saved Time.")
        print(f"Time Spent: {ticktock} seconds")

        save_logout_time()

        reset = input("Do you want to reset your data? (yes/no): ")

        if reset.lower() == "yes":
            reset_data()
        elif reset.lower() == "no":
            print("Saved Time Stored.")
        else:
            print('Invalid Response.')

        print('Disconnecting from server...')
        sys.exit('Successfully exited from server')


if __name__ == "__main__":
    main()
