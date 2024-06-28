import random

def get_random_word(word_list):
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman(word_list):
    word_to_guess = get_random_word(word_list)
    guessed_letters = set()
    attempts_left = 6  # Adjust the number of attempts as needed

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts_left > 0:
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            print(display_word(word_to_guess, guessed_letters))
            if all(letter in guessed_letters for letter in word_to_guess):
                print("Congratulations! You guessed the word correctly.")
                break
        else:
            attempts_left -= 1
            print(f"Wrong guess! You have {attempts_left} attempts left.")
            print(display_word(word_to_guess, guessed_letters))

    if attempts_left == 0:
        print(f"Game over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
    word_list = ['PYTHON', 'DEVELOPER', 'HANGMAN', 'COMPUTER', 'PROGRAMMING', 'JAVA', 'COLLEGE', 'EDUCATION',
    'SCHOOL', 'EMPLOYMENT', 'GAME', 'MOBILE', 'POPULATION', 'SYSTEM', 'TEXTBOOKS', 'LIBRARY', 'LINKEDIN', 'SOCIALMEDIA', ' POLITICS']
    hangman(word_list)