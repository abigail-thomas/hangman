import random
import io
import time

print(" o         o           o           o          o        o__ __o       o          o           o           o          o\n<|>       <|>         <|>         <|\        <|>      /v     v\     <|\        /|>         <|>         <|\        <|>\n< >       < >         / \\         / \\\o      / \\     />       <\\    / \\\o    o// \\         / \\         / \\\o      / \\\n |         |        o/   \o       \o/ v\     \o/   o/               \o/ v\  /v \o/       o/   \o       \o/ v\     \o/\n o__/_ _\__o       <|__ __|>       |   <\     |   <|       _\__o__   |   <\/>   |       <|__ __|>       |   <\     | \n |         |       /       \\      / \\    \\o  / \\   \\\          |    / \\        / \\      /       \\      / \\    \\o  / \\\n<o>       <o>    o/         \o    \o/     v\ \o/     \         /    \o/        \o/    o/         \o    \o/     v\ \o/\n |         |    /v           v\    |       <\ |       o       o      |          |    /v           v\    |       <\ | \n/ \       / \  />             <\  / \        < \      <\__ __/>     / \        / \  />             <\  / \        < \\\n\n\n ")

while True:

    # list of words to choose from
    with io.open("C:\\Users\\agtho\\Downloads\\download-random-word\\list-of-words.txt", 'r', encoding='utf-8') as f:
        dictionary = f.read().split(',')
    
    # computer chooses a random word from list
    word_to_guess = random.choice(dictionary)
    length_of_word = len(word_to_guess)

    # print the empty hangman
    print("_______\n|     |\n|     |\n|     \n|     \n|     \n|     \n|     \n-----")

    # print the letters to choose from
    print("\nLetters to choose from: \n")
    alphabet = ("a b c d e f g h i j k l m n o p q r s t u v w x y z\n")
    print(alphabet)

    # print the blank spaces of the word to guess
    print("*** The word is {} letters long...Good luck! ***\n".format(length_of_word))
    spaces = ["_ "] * length_of_word
    print("".join(spaces))
  
    # user guesses a letter
    user_guess = input("\nPlease guess a letter: ")

    # incorrect guesses start at 0
    guesses = []
    incorrect_guesses = 0
    
    # replacing underscores with correct guesses 
    def filling_in(): 
        for i, letter in enumerate(word_to_guess):
            if letter != "_" and user_guess == letter:
                spaces[i] = letter        
        print("")
        time.sleep(1)
        print("".join(spaces))
        
    filling_in()

    # loop until user guesses correct word or runs of ouf guesses
    while ("".join(spaces)) != word_to_guess:
            
        # if guessed incorrectly
        if user_guess not in word_to_guess:
            incorrect_guesses += 1 
            print("\n{} is not in the word :(".format(user_guess))
            if incorrect_guesses < 5:
                print("\nYou have {} guesses left.".format(6 - incorrect_guesses))
            elif incorrect_guesses == 1:
                print("\n You have {} guess left.".format(6 - incorrect_guesses))

        # if guessed correctly
        else:
            guesses.append(user_guess)
            print("\n")
            
        # add to the hangman depending on number of incorrect guesses
        if incorrect_guesses == 0:
            print("_______\n|     |\n|     |\n|     \n|     \n|     \n|     \n|     \n-----")
        elif incorrect_guesses == 1:
            print("_______\n|     |\n|     |\n|   ﻿(._.)﻿﻿﻿﻿ ﻿﻿﻿﻿\n|     \n|     \n|     \n|     \n-----")
        elif incorrect_guesses == 2:
            print("_______\n|     |\n|     |\n|   ﻿(._.)﻿﻿﻿﻿ ﻿﻿﻿﻿\n|     |\n|     \n|     \n|     \n-----")
        elif incorrect_guesses == 3:
            print("_______\n|     |\n|     |\n|   ﻿(._.)﻿﻿﻿﻿ ﻿﻿﻿﻿\n|    /|\n|     \n|     \n|     \n-----")
        elif incorrect_guesses == 4:
            print("_______\n|     |\n|     |\n|   ﻿(._.)﻿﻿﻿﻿ ﻿﻿﻿﻿\n|    /|\\\n|     \n|     \n|     \n-----")
        elif incorrect_guesses == 5:
            print("_______\n|     |\n|     |\n|   ﻿(._.)﻿﻿﻿﻿ ﻿﻿﻿﻿\n|    /|\\\n|    / \n|     \n|     \n-----") 
        else:
            print("_______\n|     |\n|     |\n|   ﻿(._.)﻿﻿﻿﻿ ﻿﻿﻿﻿\n|    /|\\\n|    / \\\n|     \n|     \n-----")
            break

        
               
        # replace user guess with blank space in alphabet
        if user_guess in alphabet:
            print("\n*** Letters to left choose from: ***\n")
            alphabet = (alphabet.replace(user_guess, '_'))
            print(alphabet)
            
        # if a non letter or already guessed letter is guessed, print invalid
        else:
            print("\nInvalid guess")
        
        # ask for another guess until word is guessed
        user_guess = input("\nPlease guess a letter: ") 
        
        # go back to replacing blank spaces with correct guesses
        filling_in()
               
    # if the user guesses the word in less than 6 guess, VICTORY
    if incorrect_guesses < 6 and ("".join(spaces)) == word_to_guess:
        print(" _  _  __   _  _    ____  _  _  ____  _  _  __  _  _  ____  ____    _ \n( \\/ )/  \\ / )( \\  / ___)/ )( \\(  _ \\/ )( \\(  )/ )( \\(  __)(    \\  / \\\n )  /(  O )) \/ (  \___ \) \/ ( )   /\ \/ / )( \ \/ / ) _)  ) D (  \_/\n(__/  \__/ \____/  (____/\____/(__\_) \__/ (__) \__/ (____)(____/  (_)\n\n  ")
    
    # once the user has 6 incorrect guesses, LOSS    
    if incorrect_guesses == 6:
        print(" _  _  __   _  _    ____  __  ____  ____    _ \n( \\/ )/  \\ / )( \\  (    \\(  )(  __)(    \\  / \\\n )  /(  O )) \\/ (   ) D ( )(  ) _)  ) D (  \\_/\n(__/  \\__/ \\____/  (____/(__)(____)(____/  (_)\n")
        print("\nThe word was {}\n".format(word_to_guess))
        
    # ask if user wants to play again    
    play = input("If you wish to play again, type \"yes\". If not, type \"no\": ")
    # do not repeat game if user says no
    if play == "no":
        print("\nLame choice, but ok...")
        break




