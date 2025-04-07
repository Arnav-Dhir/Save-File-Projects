import os
import random
import time

save_file = 'High_Score.txt'

rarity = 1
score = 0
best_score = 0

try:
    def load_high_score():
        """Load the high score from a file, if it exists."""
        if os.path.exists(save_file):
            with open(save_file, "r") as file:
                try:
                    return int(file.read().strip())
                except ValueError:
                    return 0
        return 0

    def save_high_score(high_scorez):
        """Save the high score to a file."""
        with open(save_file, "w") as file:
            file.write(str(high_scorez))

    def random_choice(rarityz):
        """Make a random choice based on current rarity."""
        return random.randint(1, rarityz) == 1

    def play_game():
        """Run the main game loop."""
        global rarity, score, high_score, best_score
        while True:
            if random_choice(rarity):
                print('Success!')
                nums = random.randint(1, random.randint(1, 5))
                if nums != 1:
                    rarity += 1
                score += 1
                time.sleep(0.001)
            else:
                print('Fail!')
                print(f"Score: {score}")
                if score > high_score:
                    print("New High Score!")
                    high_score = score  # Update the high score for current session
                    save_high_score(high_score)
                if score > best_score:
                    best_score = score
                # Reset score and rarity for the next attempt
                score = 0
                rarity = 1
                print("Game Over. Try Again!")
                time.sleep(0.001)  # Pause before the next round
                print("-----------------------------------------------")


    high_score = load_high_score()

    if __name__ == "__main__":
        play_game()
except KeyboardInterrupt:

    print(f'High Score: {high_score}')
    print(f"Best Score This Run: {best_score}")