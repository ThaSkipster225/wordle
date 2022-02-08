# Group HAL
# Due: February 9th, 2022

# ai_smarty.py 
# Smart AI for playing Wordle.
#
# The "strategy" of this AI player is simply to pick a winning word.
# This file exists primarily to test the AI capabilities of the main program,
# and perhaps to set the lowest possible benchmark for AI players? :)

from cgitb import grey
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
    # bestwords = ['adieu','roate','audio','stare','teary','cheat','story','tread','poopy'] # poopy is just for Eicholtz
    
    # Use random.choice(bestwords) here if we have not made a single guess yet.
    # This list of words is the best set of starting words to use.


    
    # Create lists and variables to keep track of feedback
    yellow_letters = []     # Keeps track of the letters that have been yellow
    character_counter = 0   # Counts the character we are on - Iterator
    green_letters = ['','','','','']    # Keeps track of the location of the green letters
    grey_letters = []       # Keeps track of all the letters not in the word
    

    list_counter = 0 # Counts the list we are on - Iterator

    # go through each list in feedback
    for list in feedback:
        
        character_counter = -1

        # go through each character in the list
        for element in list:
            character_counter += 1
            
            # if it is a 2, add the letter to the green letter list
            if element == 2:
                green_letters[character_counter] = guesses[list_counter][character_counter] # adds green letters to the right spot in green_letters list

            # if it is a 1, add the letter to the yellow letter list UNLESS it is in green or already in yellow
            elif element == 1:
                if (guesses[list_counter][character_counter]) in green_letters:
                    continue # Skips over letter if the letter is in list already
                elif (guesses[list_counter][character_counter]) in yellow_letters:
                    continue # Skips over letter if the letter is in yellow list already
                else:
                    yellow_letters.append(guesses[list_counter][character_counter])  # Adds yellow letters to yellow_letters list
            
            # if it is a 0, add the letter to the grey letter list UNLESS it is already in green OR is in green or yellow
            elif element == 0:
                if (guesses[list_counter][character_counter]) in grey_letters:
                    continue # Skips over letter if the letter is in list already
                elif (guesses[list_counter][character_counter]) in green_letters:
                    continue # Skips over letter if the letter is in green list already
                elif (guesses[list_counter][character_counter]) in yellow_letters:
                    continue #  Skips over letter if the letter is in yellow list already
                else:
                    grey_letters.append(guesses[list_counter][character_counter]) # Adds grey letters to grey_letters list

 
        # Iterates the counter       
        list_counter += 1

    # Checks that there are no elements in yellow_letters that are also in green_letters. Used for filtering later on
    # for i in range (0, len(yellow_letters)-1):
    #     if yellow_letters[i] in green_letters:
    #         yellow_letters.remove(i) # Removes i element from yellow_letters if it is a green letter as well

                
    
    # We would get rid of the print statements, these are just to see if the iteration was working
    print(f"the letters in the word are {yellow_letters}")
    print(f"the grey letters in the word are {grey_letters}")
    print(f"Green Letters: {green_letters}")

    revised_grey_letters = []
    # Cleaning of the grey gooses
    for i in range (0,len(grey_letters)):
        if grey_letters[i] not in green_letters:
            revised_grey_letters.append(grey_letters[i])



    # USE FILTERS TO DETERMINE THE NEXT WORD GUESS

    # Finding the starting value for the filter
    
    if len(guesses) == 0: # if it is the first guess, return a random word
        return random.choice(wordlist)
    elif (len(guesses) == 1): # if it is the second guess, start the list from the beginning
        start_index = 0
    else: # otherwise, start the list from where we last guessed      
        start_index = wordlist.index(guesses[-1])+1
    
    
    # Check if green_letters list is empty
    green_empty = True # assume the list is empty
    for i in range (0, len(green_letters)): # go through each index of green_letters
        if green_letters[i] != '': # if the index is not empty
            green_empty = False # empty condtion is false
            break # break out of the loop

    # Loop for whole of wordlist
    for i in range (start_index, len(wordlist)): # go through each word in the list, i represents the index of that word in the list
        
        # Create flags that are checked for each word in the list, they all start as true
        green_flag = True
        yellow_flag = True
        grey_flag = True
        
        # if the green_letters list is empty, the word automtically passes the green letter check
        if green_empty == True:
            green_flag = True

        else: # else if there are green letters, the word must be checked against them
            for x in range (0,5): # go through each character of green letters, x is the character
                if green_letters[x] == '': # if there is no green letter there, skip to the next character
                    continue
                else: # else, check the word in wordlist with the green letter
                    if wordlist[i][x] != green_letters[x]: # if the wordlist word at that index does not equal the green_letter at that index
                        green_flag = False # set the green_flag to false and break out of the green letter check loop
                        break
        
        # if the green letter check does not pass, continue to the next word in the list
        if green_flag == False:
            continue

        # Check that all yellow letters are in the word
        for y in range (0, len(yellow_letters)): # go through each yellow letter in the list
            if yellow_letters[y] not in wordlist[i]: # if the letter is not in the word
                yellow_flag = False # the word does not pass the yellow letter check
                break

        # if the yellow letter check does not pass, continue to the next word in the list
        if yellow_flag == False:
            continue

        # Check that all grey letters are not in the word
        for z in range (0, len(grey_letters)): # go through each grey letter in the list
            if grey_letters[z] in wordlist[i]: # if the letter is in the word
                grey_flag = False # the word does not pass the grey letter check
                break

        # if the grey letter check does not pass, continue to the next word in the list
        if grey_flag == False:
            continue

        # if all checks have been passed, return the word
        if (green_flag == True and yellow_flag == True and grey_flag == True):
            return wordlist[i]
        else:
            continue
        
    
    # print(f"the length of wordlist is {len(wordlist)}")

    # # Check for yellow letters
    # for i in range(0, len(wordlist)-1): # go through each word in the list, i represents the index of that word in the list
    #     for x in range(0, len(yellow_letters)-1): # go through each letter in yellow letter, x is the character
    #         if str(yellow_letters[x]) in wordlist[i]: # if the character in yellow letters is in the word, go to next character
    #             continue
    #         else: 
    #             wordlist.remove(wordlist[i]) # else, remove the word from the list
    #             break # break out of for loop to go to the next word in the list


    # FIRST WORD
    # If it is the first guess, pick a random word
    # if len(guesses) == 0:
    #     return random.choice(wordlist) 

    # elif len(guesses) >= 1:
    #     # utilize feedback
    #     return random.choice(wordlist)
        
        


    # BASED ON FEEDBACK
    # else if it is guesses 5-6 and there is some sort of feedback or there is enough feedback...
    # enough feedback : at least 2 green letters or 1 green and at least 2 yellow or at least 3 yellow
    # elif (len(guesses) >= 5 and feedback != 0) or (num_of_green) >= 2 or (num_of_green == 1 and num_of_yellow >= 2) or (num_of_yellow >= 3):
    #     # return based on the feedback
    #     return random.choice(wordlist)


    # "LETTER FARMING"/GOOD FOLLOWUP WORD
    # else pick a "good" word
    # good word : commonly used letters, no letter overlap with previous guesses
    # else:
    #     return random.choice(wordlist)

    # Use feedback to determine the location of the letters within the word, if it's 2, it stays there.
    # If it's a 1, then it is in the word, but needs to be moved elsewhere in the word. Make the AI guess where it would be.


if __name__ == "__main__":
    wordlist = utils.readwords("allwords5.txt")
    print(f"AI: 'My next choice would be {makeguess(wordlist)}'")
