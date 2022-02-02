# Group HAL
# Due: February 9th, 2022

# ai_smarty.py 
# Smart AI for playing Wordle.
#
# The "strategy" of this AI player is simply to pick a winning word.
# This file exists primarily to test the AI capabilities of the main program,
# and perhaps to set the lowest possible benchmark for AI players? :)

import pdb
import random
import utils



def makeguess(wordlist, guesses=[], feedback=[]):
    """Guess a word from the available wordlist, (optionally) using feedback 
    from previous guesses.
    
    Parameters
    ----------
    wordlist : list of str
        A list of the valid word choices. The output must come from this list.
    guesses : list of str
        A list of the previously guessed words, in the order they were made, 
        e.g. guesses[0] = first guess, guesses[1] = second guess. The length 
        of the list equals the number of guesses made so far. An empty list 
        (default) implies no guesses have been made.
    feedback : list of lists of int
        A list comprising one list per word guess and one integer per letter 
        in that word, to indicate if the letter is correct (2), almost 
        correct (1), or incorrect (0). An empty list (default) implies no 
        guesses have been made.

    Output
    ------
    word : str
        The word chosen by the AI for the next guess.
    """

    # print(wordlist) 

    # List of all the best starting words for wordle.
    bestwords = ['adieu','roate','audio','stare','teary','cheat','story','tread','poopy'] # poopy is just for Eicholtz
    
    # Use random.choice(bestwords) here if we have not made a single guess yet.
    # This list of words is the best set of starting words to use.
    if len(guesses) == 0:
        print (wordlist[1])
        print (wordlist[wordlist.index(random.choice(bestwords))])
        return wordlist[wordlist.index(random.choice(bestwords))] 
        # random.choice( list(set(wordlist) - (set(wordlist)-set(bestwords))))
    elif len(guesses) > 0:
        return random.choice(wordlist)
    else:
        return random.choice(wordlist)

    # Use feedback to determine the location of the letters within the word, if it's 2, it stays there.
    # If it's a 1, then it is in the word, but needs to be moved elsewhere in the word. Make the AI guess where it would be.


if __name__ == "__main__":
    wordlist = utils.readwords("allwords5.txt")
    print(f"AI: 'My next choice would be {makeguess(wordlist)}'")
