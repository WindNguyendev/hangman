"""
Python basics, Problem Set, hangman.py
Name: Nguyen Duc Phong
Collaborators: TODO
Time spent: TODO
"""

# ---------------------------------------------------------------------------- #
#                                 Hangman Game                                 #
# ---------------------------------------------------------------------------- #


# -------------------------------- Helper code ------------------------------- #
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME, "r") as inFile:
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# ---------------------------- end of helper code ---------------------------- #


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far, assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"

    secret_word = secret_word.lower()
    if letters_guessed[len(letters_guessed)-1] in secret_word:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word =  secret_word = secret_word.lower()
    secret_word = list(secret_word)
    for i in range(0,len(secret_word)):

            if secret_word[i] not in letters_guessed:
                secret_word[i] = " _ "


    secret_word = "".join(secret_word)

    return secret_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    a = string.ascii_lowercase
    a = list(a)
    for i in range(0,len(letters_guessed)):
        if letters_guessed[i] in a:
            a.remove(letters_guessed[i])
    a = "".join(a)
    return a


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    l = []

    print("""

        Loading word list from file... 
        55900 words loaded. 
        Welcome to the game Hangman! 
        I am thinking of a word that is {} letters long. 
            ------------- 
        """.format(len(secret_word))
        )
    num = 0
    ascii_lowercase = string.ascii_lowercase
    num_2=3 
    while (num <6) and (num_2>0):
        print("""
            You have {} guesses left. 
            Available letters: {}
            """.format(6-num,get_available_letters(l)))
        print("""Please guess a letter: """,end ="")
        a = input()
        a = str(a)
        l.append(a)
        if (is_word_guessed(secret_word,l) == True) and ("_" in get_guessed_word(secret_word,l)):
            if(l.count(a) >= 2):
                num_2 = num_2 - 1
                print("Oops! You've already guessed that letter. You now have {} warnings".format(num_2))
                print(get_guessed_word(secret_word,l))
            else:

                print("""Good guess: {}""".format(get_guessed_word(secret_word,l)))
   
        elif (is_word_guessed(secret_word,l) == False):
            if a in "aeiou":
                if l.count(a) >=2:
                    num_2 = num_2 - 1
                    num = num +2
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(num_2))
                else:
                    print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word,l)) )
                    num = num + 2
            elif (l.count(a) >= 2) or (a not in ascii_lowercase) :
                num_2 = num_2 - 1
                num = num +1
                print("Oops! You've already guessed that letter. You now have {} warnings".format(num_2))
                
            else:
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word,l)) )
                num = num + 1
        elif (is_word_guessed(secret_word,l) == True) and ("_" not in get_guessed_word(secret_word,l)):
            d = (6-num)*len(set(secret_word))
            print("Congratulations, you won!")
            print("Your total score for this game is: {}".format(d))
            break
        
    if (num>=6) and ("_" in get_guessed_word(secret_word,l)):
        print("""you lose and secret_word: {}""".format(secret_word))
    elif num_2<=0:
        print("""you lose and secret_word: {}""".format(secret_word))
            




        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# ---------------------------------------------------------------------------- #


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    num = 0
    if len(my_word) != len(other_word):
        num = num+1
    else:
        for i in range(0,len(my_word)):
            if (my_word[i] != other_word[i]) and (my_word[i] != "_"):
                num = num+1
    if num!=0:
        return False
    else:
        return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word

    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    l = []
    my_word = my_word.replace(" ","")
    for i in wordlist:
        if match_with_gaps(my_word,i) == True:
            l.append(i)
    l = " ".join(l)
    return l


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"

    l = []

    print("""

        Loading word list from file... 
        55900 words loaded. 
        Welcome to the game Hangman! 
        I am thinking of a word that is {} letters long. 
            ------------- 
        """.format(len(secret_word))
        )
    num = 0
    ascii_lowercase = string.ascii_lowercase
    num_2=3 
    while (num <6) and (num_2>0):
        print("""
            You have {} guesses left. 
            Available letters: {}
            """.format(6-num,get_available_letters(l)))
        print("""Please guess a letter: """,end ="")
        a = input()
        a = str(a)
        if a=="*":
            print(show_possible_matches(get_guessed_word(secret_word,l)))
        else:
            l.append(a)
            if (is_word_guessed(secret_word,l) == True) and ("_" in get_guessed_word(secret_word,l)):
                if(l.count(a) >= 2):
                    num_2 = num_2 - 1
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(num_2))
                    print(get_guessed_word(secret_word,l))
                else:

                    print("""Good guess: {}""".format(get_guessed_word(secret_word,l)))
       
            elif (is_word_guessed(secret_word,l) == False):
                if a in "aeiou":
                    if l.count(a) >=2:
                        num_2 = num_2 - 1
                        num = num +2
                        print("Oops! You've already guessed that letter. You now have {} warnings".format(num_2))
                    else:
                        print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word,l)) )
                        num = num + 2
                elif (l.count(a) >= 2) or (a not in ascii_lowercase) :
                    num_2 = num_2 - 1
                    num = num +1
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(num_2))
                    
                else:
                    print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word,l)) )
                    num = num + 1
            elif (is_word_guessed(secret_word,l) == True) and ("_" not in get_guessed_word(secret_word,l)):
                d = (6-num)*len(set(secret_word))
                print("Congratulations, you won!")
                print("Your total score for this game is: {}".format(d))
                break
            
        if (num>=6) and ("_" in get_guessed_word(secret_word,l)):
            print("""you lose and secret_word: {}""".format(secret_word))
        elif num_2<=0:
            print("""you lose and secret_word: {}""".format(secret_word))
                


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

# ---------------------------------------------------------------------------- #

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
