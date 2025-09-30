import random

# 📝 Sign Up Ritual
print("Sign Up to Continue")
input("Press Enter to continue...")

# 🔤 Name Validation
while True:
    name = input("Enter your name: ").strip()
    if name.replace(" ", "").isalpha() and name:
        print("✅ Name accepted.")
        break
    else:
        print("⚠️ Invalid name. Use letters only, no digits, symbols, or empty fields.")

# 📧 Email Validation
while True:
    email = input("Enter your email: ").strip()
    if email.endswith("@gmail.com"):
        print("✅ Email accepted.")
        break
    else:
        print("⚠️ Please use a Gmail address ending with '@gmail.com'.")

# 📱 Phone Validation
print("Proceeding to the next step...")
while True:
    phone = input("Enter your phone number: ").strip()
    if phone.isdigit() and 8 <= len(phone) <= 15:
        print("✅ Phone number accepted.")
        break
    else:
        print("⚠️ Invalid phone number. Must be 8–15 digits with no letters or symbols.")

print("All inputs are valid. Thank you!")
print("Operation Successful!")

# 🎮 Game Launcher
def number_guessing_game():
    print("\n🎯 Number Guessing Game Activated!")
    secret = random.randint(1, 10)
    while True:
        guess = input("Guess a number between 1 and 10: ").strip()
        if not guess.isdigit():
            print("⚠️ Invalid input. Enter digits only.")
            continue
        guess = int(guess)
        if guess == secret:
            print("🔥 Legacy unlocked! You guessed it.")
            break
        elif guess < secret:
            print("📈 Too low. Try a higher number.")
        else:
            print("📉 Too high. Try a lower number.")

def tic_tac_toe_game():
    print("\n❌ Tic Tac Toe Activated!")
    board = [" "]*9
    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def check_win(player):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

    current = "X"
    for turn in range(9):
        print_board()
        move = input(f"Player {current}, choose position (1-9): ").strip()
        if not move.isdigit() or not (1 <= int(move) <= 9) or board[int(move)-1] != " ":
            print("⚠️ Invalid move. Try again.")
            continue
        board[int(move)-1] = current
        if check_win(current):
            print_board()
            print(f"🏆 Player {current} wins!")
            return
        current = "O" if current == "X" else "X"
    print_board()
    print("🤝 It's a draw!")

def tech_quiz_game():
    print("\n🧠 Tech Quiz Activated!")
    question = "What does CPU stand for?"
    options = ["Central Processing Unit", "Computer Power Unit", "Core Performance Utility", "Control Panel Unit"]
    answer = 0
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt}")
    choice = input("Choose the correct option (1-4): ").strip()
    if choice == str(answer + 1):
        print("✅ Correct! Legacy knowledge confirmed.")
    else:
        print("❌ Incorrect. Ritual failed.")

def math_speed_game():
    print("\n🧮 Math Speed Test Activated!")
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    answer = a + b
    guess = input(f"What is {a} + {b}? ").strip()
    if guess.isdigit() and int(guess) == answer:
        print("✅ Correct! Mental audit passed.")
    else:
        print(f"❌ Incorrect. The answer was {answer}.")

def even_odd_game():
    print("\n🔢 Even or Odd Game Activated!")
    number = random.randint(1, 100)
    guess = input(f"Is {number} even or odd? ").strip().lower()
    correct = "even" if number % 2 == 0 else "odd"
    if guess == correct:
        print("✅ Correct! You read the pattern.")
    else:
        print(f"❌ Incorrect. It was {correct}.")

# 🔀 Random Game Selector
games = [number_guessing_game, tic_tac_toe_game, tech_quiz_game, math_speed_game, even_odd_game]
selected_game = random.choice(games)
selected_game()
# 🎉 End of Program