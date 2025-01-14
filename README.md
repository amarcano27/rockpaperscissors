# rockpaperscissors
Rock, Paper, Scissors Game
This Python program is an interactive Rock, Paper, Scissors game where a user competes against a randomly selected choice made by the bot. The program accepts user input, validates it, and determines the winner based on standard game rules.

How It Works
The user is prompted to choose between:

0 for Rock
1 for Paper
2 for Scissors
The bot randomly selects its choice from the same options.

Both choices are displayed using ASCII art for clarity and fun.

The program compares the user's choice with the bot's choice:

If both choose the same option, the result is a tie.
If the user's choice beats the bot's, it prints "You win".
Otherwise, it prints "You lose".
If the user inputs anything other than 0, 1, or 2, the program exits with an error message.


Requirements
Python 3.x
How to Run
Clone or download the repository.

Open a terminal or command prompt.

Navigate to the directory containing the script.

Run the script using the following command:
python rock_paper_scissors.py

Features
User-friendly prompts.
ASCII art for visual representation of the choices.
Input validation to handle incorrect inputs gracefully.
Randomized bot behavior for an unpredictable game experience.
Future Improvements
Add a loop to allow replaying the game without restarting the program.
Keep track of the score (wins, losses, ties).
Add more features like "best of 3" mode.
