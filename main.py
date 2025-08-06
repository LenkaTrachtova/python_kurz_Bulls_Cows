#knihovny
import random
import time

#obarvení
def colored_text(text, color_code):
      return f"\033[38;5;{color_code}m{text}\033[0m"

link = colored_text('-', 125) * 50
print(link)
darts = colored_text(">", 125) * 3

#hlavička + úvod
print("""
main.py: druhý projekt do Engeto Online Python Akademie

author: Lenka Trachtová
email: lenkatrachtova@email.cz
""")
print(link)
print("Hi there!")
print(link)
print('''I've generated a random 4 digit number for you.
Let's play a bulls and cows game.''')
print(link)

#  náhodné 4-ciferné číslo jako list číslic
def generate_number():
    digits = random.sample(range(0, 10), 4)  # náhodně vybere 4 různé číslice
    if digits[0] == 0:
        # Pokud první číslice je 0, vyměníme ji, aby číslo nezačínalo nulou
        for i in range(1, 4):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
    return digits
# správný výstup hráče
def is_valid_input(user_input):
    return (
        user_input.isdigit() and
        len(user_input) == 4 and
        len(set(user_input)) == 4 and 
        user_input[0] != "0"
    )

#jednotné množné č.
def pluralize(count, singular, plural):
    return f"{count} {singular if count == 1 else plural}"

#  hodnocení pokusů hráče
def evaluate_guess(secret, guess):
    bulls = 0
    cows = 0

    # Pomocné seznamy
    secret_unused = []
    guess_unused = []

    # 1️ hledání bulls
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        else:
            secret_unused.append(secret[i])
            guess_unused.append(guess[i])

    # 2️ hledání cows (správná číslice, špatné místo)
    for digit in guess_unused:
        if digit in secret_unused:
            cows += 1
            secret_unused.remove(digit)  # Odstraň, aby se nezapočítala vícekrát

    return bulls, cows    

#  Hlavní herní smyčka
def play_game():
    secret = generate_number()
    attempts = 0
    #časomíra
    start_time = time.time()

    while True:
        user_input = input("Enter a number: ")
        if not is_valid_input(user_input):
            print("Please enter a valid 4-digit number.")
            print(link)
            continue

        guess = [int(d) for d in user_input]
        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)
        print(f"{darts} {user_input}")
        print(f"{pluralize(bulls, 'bull', 'bulls')}, {pluralize(cows, 'cow', 'cows')}")
        print(link)

# vyhodnocení bulls a cows.
        if bulls == 4:
            end_time = time.time()  #  konec časomíry
            elapsed_time = end_time - start_time
            print("Correct, you've guessed the right number in 4 guesses!")
            print(link)
            print(f"Secret number is: {''.join(map(str, secret))}")
            print(f"Your attempts: {attempts}")
            print(f"Your time: {round(elapsed_time, 2)} sec.")
            print(link)
            print("That's amazing!")
            print(link)
            break

#  Spuštění hry
play_game()