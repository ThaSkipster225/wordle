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


    # QUESTIONS FOR SKIPPY:

    # Do we want to have variables for the feedback? Like the number of green/yellow we have figured out
    # We would have to loop through each element of feedback and only count it once 
    # (like the same green letter in guesses 1 and 2 should only count as 1 green)
    num_of_green = 0
    num_of_yellow = 0
    yellow_letters = []
    character_counter = 0

    # This is helpful for totals, but it doesnt take into account similar/repeated yellow letters OR repeated green letters
    # OR letters turning from yellow to green
    for list in feedback:
        character_counter = -1
        for element in list:
            character_counter += 1
            if element == 1:
                if (guesses[-1][character_counter]) in yellow_letters:
                    continue
                else:
                    num_of_yellow +=1
                    yellow_letters.append(guesses[-1][character_counter])
            elif element == 2:
                num_of_green += 1
    
    # We would get rid of the print statements, these are just to see if the iteration was working
    print(f"the number of green is {num_of_green}")
    print(f"the number of yellow is {num_of_yellow}")
    print(f"the letters in the word are {yellow_letters}")

    # I'm having issues with the above code changing between runs...
    # Idk if we can even use the code, but it might be helpful
    

    # OR should we combine the feedback from each guess somehow?

    # Idea for our best words/secondary words...
    # What if our first set of words was all anagrams like "stare", "tears", etc.
    # Our second set would then be the next common words
    # Would we have to create a third set, fourth set? Like all anagrams, but slowly using less common letters?


    # I commented out the logic below to test it with random words
    return random.choice(wordlist)

    # FIRST WORD
    # If it is the first guess, pick a word from bestwords
    if len(guesses) == 0:
        print (wordlist[1])
        print (wordlist[wordlist.index(random.choice(bestwords))])
        return wordlist[wordlist.index(random.choice(bestwords))] 
        # random.choice( list(set(wordlist) - (set(wordlist)-set(bestwords))))


    # BASED ON FEEDBACK
    # else if it is guesses 5-6 and there is some sort of feedback or there is enough feedback...
    # enough feedback : at least 2 green letters or 1 green and at least 2 yellow or at least 3 yellow
    elif (len(guesses) >= 5 and feedback != 0) or (num_of_green) >= 2 or (num_of_green == 1 and num_of_yellow >= 2) or (num_of_yellow >= 3):
        # return based on the feedback
        return random.choice(wordlist)


    # "LETTER FARMING"/GOOD FOLLOWUP WORD
    # else pick a "good" word
    # good word : commonly used letters, no letter overlap with previous guesses
    else:
        return random.choice(wordlist)

    # Use feedback to determine the location of the letters within the word, if it's 2, it stays there.
    # If it's a 1, then it is in the word, but needs to be moved elsewhere in the word. Make the AI guess where it would be.


if __name__ == "__main__":
    wordlist = utils.readwords("allwords5.txt")
    print(f"AI: 'My next choice would be {makeguess(wordlist)}'")
