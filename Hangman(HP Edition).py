#HarryPotterHangman
import random
easy_words = [
    "lumos", "nox", "accio", "reparo", "silencio", "stupefy", "avadakedavra", "expelliarmus", "wingardiumleviosa", "expectopatronum"
]

medium_words = [
    "sectumsempra", "obliviate", "incendio", "aguamenti", "diffindo", 
    "protego", "muffliato", "sonorus", "riddikulus"
]

hard_words = [
      "petrificustotalus", "priorincantato", 
    "finiteincantatem", "locomotorwibbly", 
    "arrestomomentum", "impervius", "colloportus", "episkey", "tarantallegra"
]

from hangman_art import logo,stages,hp
print(logo)
print(hp)
while True:
    lives = 6
    difficulty = input("Choose your difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        word_list = easy_words
    elif difficulty == "medium":
        word_list = medium_words
    elif difficulty == "hard":
        word_list = hard_words
    else:
        print("Invalid difficulty. Defaulting to 'medium'.")
        word_list = medium_words
        
    chosen_word = random.choice(word_list)
    #print(chosen_word)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += " _"
    print(f"Word to guess({word_length}): " + placeholder)

    game_over = False
    correct_letters = []

    while not game_over:
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        guess = input("Guess a letter: ").lower()

        if guess in correct_letters:
            print(f"You've already guessed {guess}")
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += " _"

        print("Word to guess: " + display)


        if guess not in chosen_word:
            lives=lives-1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            if lives == 0:
                game_over = True

                
                print(f"***********************YOU LOSE**********************")
                print(f"IT WAS {chosen_word}! YOU LOSE!")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")
        print(stages[lives])
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing Hangman HP Edition!")
        break

