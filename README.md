# Rock, Paper, Scissors Game

This Python program is an interactive **Rock, Paper, Scissors** game where a user competes against a randomly selected choice made by the bot. The program accepts user input, validates it, and determines the winner based on standard game rules.

## How It Works

1. The user is prompted to choose between:
   - **0** for Rock  
   - **1** for Paper  
   - **2** for Scissors  

2. The bot randomly selects its choice from the same options.

3. Both choices are displayed using ASCII art for clarity and fun.

4. The program compares the user's choice with the bot's choice:
   - If both choose the same option, the result is a **tie**.
   - If the user's choice beats the bot's, it prints **"You win"**.
   - Otherwise, it prints **"You lose"**.

5. If the user inputs anything other than `0`, `1`, or `2`, the program exits with an error message.


## Requirements

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python rock_paper_scissors.py
