import random
import hangman_words
import hangman_art
from replit import clear

# Select a random word from the word list
word = random.choice(hangman_words.word_list)

# Initialize the display with underscores for each letter in the word
display = ["_" for letter in word]

# Set the number of lives to 6
lives = 6

# Set the game over flag to False
game_over = False

# Initialize an empty list to store the guessed letters
guessed_letters = []

# Print the hangman logo and the initial hangman stage
print(hangman_art.logo)
print(hangman_art.stages[lives])

# Start the game loop
while not game_over:
    # Clear the console
    clear()

    # Display the current display to the user
    print(" ".join(display))
    # Get the user's guess
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed this letter
    if guess in display or guess in guessed_letters:
        # If the letter has already been guessed, inform the user and let them try again
        print(f"You already guessed letter: '{guess}'. Try another one.")

    else:
        # If the letter has not been guessed, check if it is in the word
        for position in range(len(word)):
            letter = word[position]

            # If the letter is in the word, update the display
            if letter == guess:
                display[position] = letter

        # If the letter is not in the word, the user loses one life
        if guess not in word:
            lives -= 1
            guessed_letters.append(guess)

            # If the user has no more lives, set the game over flag to True and display the "you lose" ascii art
            if lives == 0:
                game_over = True
                print(hangman_art.you_lose)
            else:
                # If the user still has lives remaining, inform them that their guess was incorrect
                print(f"Letter '{guess}' is not in the word. You lose one life.")
        else:
            # If the letter is in the word, inform the user that their guess was correct
            print(f"Correct! '{guess}' is in the word.")

    # If all the letters in the word have been revealed, set the game over flag to True and display the "you win" ascii art
    if display.count("_") == 0:
        game_over = True
        print(hangman_art.you_win)
    # Display the current hangman stage
    print(hangman_art.stages[lives])
