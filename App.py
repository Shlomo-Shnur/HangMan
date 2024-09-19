import random
import hangman_words
import hangman_art


def game():
    chosen_word = random.choice(hangman_words.word_list)
    placeholder = ["_" for _ in range(len(chosen_word))]
    display = "".join(placeholder)
    lives = 6
    game_over = False

    print(hangman_art.logo)
    print(f"Word to guess: {display}")
    while not game_over:
        print(f"***********************{lives}/6 LIVES LEFT***********************")
        guess = input("Guess a letter ").lower()
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess} that's not in the word. You lose a life.")
        if guess in placeholder:
            print(f"You have already guessed {guess}")
            print(display)
            continue

        for index, letter in enumerate(chosen_word):
            if guess == letter:
                placeholder[index] = guess

        display = ''.join(placeholder)
        print(f"Word to guess: {display}")
        print(hangman_art.stages[lives])
        if display == chosen_word or lives == 0:
            game_over = True
            if lives == 0:
                print(f"************IT WAS {chosen_word} YOU LOSE!************")
            else:
                print("============YOU WIN!============")


if __name__ == "__main__":
    game()
