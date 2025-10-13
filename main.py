print("""
main.py: druhý projekt do Engeto Online Python Akademie
author: Lenka Trachtová
email: lenkatrachtova@email.cz
""")

import random
import time

def colored_text(text, color_code) -> str:
      '''Returns text formatted with ANSI color code.'''
      return f"\033[38;5;{color_code}m{text}\033[0m"

def generate_number() -> list[int]:
    """ 
    Generates a random number with unique digits. The number does not start with zero. The length of the
    number is defined by the global constant DIGIT_COUNT.
    Returns: list[int]: Int representing the secret number with unique digits.
    """
    digits = random.sample(range(0, 10), DIGIT_COUNT)
    if digits[0] == 0:
        for i in range(1, DIGIT_COUNT):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
    return digits

def is_valid_input(user_input) -> bool:
    """
    Checks if the player's input is a valid number with unique digits.
    The required length is defined by the global constant DIGIT_COUNT.
        Parameters:
        user_input (str): The input entered by the player.
        Returns:
        bool: True if the input is valid, False otherwise.
    """
    return (
        user_input.isdigit() and
        len(user_input) == DIGIT_COUNT and
        len(set(user_input)) == DIGIT_COUNT and 
        user_input[0] != "0"
    )

def pluralize(count: int, singular: str, suffix: str = "s") -> str:
    """
    Returns the word in singular or plural form based on count.
        Parameters:
        count (int): The number to determine singular/plural.
        singular (str): The base word in singular form.
        suffix (str): Optional suffix for plural form (default is 's').
        Returns:
        str: Formatted string with count and correct word form.
    """
    word = singular if count == 1 else singular + suffix
    return f"{count} {word}"

def evaluate_guess(secret: list[int], guess: list[int]) -> tuple[int, int]:
    '''
    Compares the player's guess with the secret number and returns the number of bulls and cows.
    Bulls = correct digit in correct position.
    Cows = correct digit in wrong position.
        Parameters:
        secret_number (list[int]): The secret number as a list of digits.
        player_guess (list[int]): The player's guess as a list of digits.
        Returns:
        tuple[int, int]: Number of bulls and cows.
    ''' 
    bulls = 0
    cows = 0

    unmatched_secret = []
    unmatched_guess = []

    for position_index, (secret_digit, guess_digit) in enumerate(zip(secret, guess)):
        if secret_digit == guess_digit:
            bulls += 1
        else:
            unmatched_secret.append(secret_digit)
            unmatched_guess.append(guess_digit)

    for digit in unmatched_guess:
        if digit in unmatched_secret:
            cows += 1
            unmatched_secret.remove(digit)

    return bulls, cows

def play_game() -> None:
    '''
    Starts the Bulls and Cows game.
    Generates a secret number with unique digits, handles user input, evaluates guesses,
    tracks the number of attempts and measures the time taken to solve the game.
    Returns:
    none
    '''
    secret = generate_number()
    attempts = 0
    start_time = time.time()

    while True:
        try:
            user_input = input("Enter a number: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Goodbye!")
            break
        
        if not is_valid_input(user_input):
            print(f"Please enter a valid {DIGIT_COUNT}-digit number.")
            print(line)
            continue

        guess = [int(d) for d in user_input]
        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)
        print(f"{darts} {user_input}")
        print(f"{pluralize(bulls, "bull")}, {pluralize(cows, "cow")}")
        print(line)

        if bulls == DIGIT_COUNT:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(colored_text("Congratulations!", 125))
            print(line)
            print(f"Secret number is: {''.join(map(str, secret))}")
            print(f"Your {pluralize(attempts, "attempt")}: {attempts}")
            print(f"Your time: {round(elapsed_time, 2)} sec.")
            print(line)
            print(f"{name} that's amazing!")
            print(line)
            break

DIGIT_COUNT = 4
line = colored_text("-", 125) * 50
darts = colored_text(">", 125) * 3
name = input("enter your name: ")
print(line)
print(f"Hi {name}!")
print(line)
print(f'''I've generated a random {DIGIT_COUNT} digit number for you.
Let's play a bulls and cows game.''')
print(line)

if __name__ == "__main__":
    play_game()
