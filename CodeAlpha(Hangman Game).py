import random

words = ["mango", "python", "university", "sparrow", "computer","parrot","peacock"]

play_again = "yes"

while play_again == "yes":

    word = random.choice(words)
    guessed_letters = ""
    life_line = 6

    total_attempts = 0
    correct_count = 0
    wrong_count = 0

    print("\nWelcome to Hangman Game")
    print(f"You have {life_line} chances.")

    while life_line > 0:

        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        if "_" not in display:
            print("\n🎉 Congratulations! You Win!")
            break

        guess = input("Enter a letter: ").lower()

        total_attempts += 1

        if guess in word and guess not in guessed_letters:
            guessed_letters += guess
            correct_count += 1
            print(" 😎Correct Guess")
        else:
            life_line -= 1
            wrong_count += 1
            print(" 😇Wrong Guess")
            print("Remaining Chances:", life_line)

    if life_line == 0:
        print("\n 🥹Game Over!")
        print("Correct Word Was:", word)

    print("\n----- Game Summary -----")
    print("Total Attempts :", total_attempts)
    print("Correct Guesses:", correct_count)
    print("Wrong Guesses  :", wrong_count)

    play_again = input("\nPlay Again? (😃 yes/😔 no): ").lower()

print("Thanks for playing Hangman Game!")
