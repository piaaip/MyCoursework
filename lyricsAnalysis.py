# -*- coding: utf-8 -*-

# This script contains a collection of simple functions for text analysis
# designed as a learning aid for the course "Computational Methods in Ethnomusicology"
# (Kunstuniversität Graz, WS 2019/2020)
# Author: Rafael Caro Repetto


########################################################################################################################


# Definition of global variables

vowels_lowercase = 'aeiou'
vowels_uppercase = 'AEIOU'
punctuation = '.,;:!?\'"'


########################################################################################################################


# Definition of functions

def countWords(line):
    '''
    Counts the words contained in a line. A word is understood as the string between blank spaces (" ").
    
    Args:
        line (str): the line whose words are to be counted
    
    Returns:
        word count (int): the number of words contained in line
        
    >>> countWords("What a wonderful world!\\n")
    4
    >>> countWords("\\n")
    0
    '''
    
    # Remove the escape sequence for new line ("\n") from the end of the line using the method .rstrip()
    clean_line = line.rstrip()
    
    # Check if the line is NOT an empty line("")
    if clean_line != "":
        # Divide the clean line in segments using blank space (" ") as separator with the .split() method
        # The output is a list of strings, and is assigned to the variable words
        words = clean_line.split(" ")
        # Count the number of words using len()
        words_count = len(words)
        # Return the number of words
        return words_count
    # If the line is an empty line
    else:
        # Return 0 as the number of words
        return 0

#-----------------------------------------------------------------------------------------------------------------------

def countVowels(line):
    '''
    Counts how many vowels are contained in a line.
    
    Args:
        line (str): the line whose vowels are to be counted
    
    Returns:
        vowels count (int): the number of vowels contained in line
    
    >>> countVowels("What a wonderful world!\\n")
    6
    >>> countVowels("\\n")
    0
    '''
    
    # Start a vowel counter 
    vowel_counter = 0
    
    # Remove the escape sequence for new line ("\n") from the end of the line using the method .rstrip()
    clean_line = line.rstrip()
    
    # Iterate over the letters in line
    for letter in clean_line:
        # Check if the current letter is contained EITHER in the vowels_lowercase variable OR the vowels_uppercase variable
        if letter in vowels_lowercase or letter in vowels_uppercase:
            # If so, update the vowel counter by 1
            vowel_counter += 1
            
    # Return the vowel counter
    return vowel_counter

#-----------------------------------------------------------------------------------------------------------------------

def countConsonants(line):
    '''
    Counts how many consonants are contained in a line.
    
    Args:
        line (str): the line whose consonants are to be counted
    
    Returns:
        consonants count (int): the number of consonants contained in line
    
    >>> countVowels("What a wonderful world!\\n")
    13
    >>> countVowels("\\n")
    0
    '''
    
    # Start a consonants counter 
    consonant_counter = 0
    
    # Remove the escape sequence for new line ("\n") from the end of the line using the method .rstrip()
    clean_line = line.rstrip()
    
    # Iterate over the letters in line
    for letter in clean_line:
        # A consonant is defined by a character that
        ## is contained NEITHER in the vowels_lowercase NOR in the vowels_uppercase variables
        ## is NOT contained in the punctuation variable
        ## it is NOT a blank space (" ")
        if letter not in vowels_lowercase and letter not in vowels_uppercase and letter not in punctuation and letter != " ":
            # Update the consonant counter by 1
            consonant_counter += 1
    
    # Return the vowel counter
    return consonant_counter

#-----------------------------------------------------------------------------------------------------------------------

def revowelizer(line, vowel='aA'):
    '''
    Change all the vowels of the given line to the given target vowel
    
    Args:
        line (str): the string whose vowels will be changed to to the target vowel
        vowel (str): a string with lowercase and uppercase version of the target vowel (in that order)
        
    Returns:
        new line (str): a new version of line, with the vowels changed
        
    >>> revowelizer("I see trees of green,\\n")
    'A saa traas af graan,'
    >>> revowelizer("I see trees of green,\\n", vowel="uU")
    'U suu truus uf gruun,'
    '''
    
    # Create an empty line ("").
    # All the letters of the given line will be copied here, but when a vowel is found, it would be changed to the target vowel
    new_line = ""
    
    # Remove the escape sequence for new line ("\n") from the end of the line using the method .rstrip()
    clean_line = line.rstrip()
    
    # Iterate over the letters in line
    for letter in clean_line:
        # Check if the current letter is a lowercase vowel by checking if it is contained in the vowels_lowercase variable
        if letter in vowels_lowercase:
            # If so, append the lowercase target vowel (vowel[0]) to the new line instead of the original vowel
            new_line += vowel[0]
        # Check if the current letter is an uppercase vowel by checking if it is contained in the vowels_uppercase variable
        elif letter in vowels_uppercase:
            # If so, append the uppercase target vowel (vowel[1]) to the new line instead of the original vowel
            new_line += vowel[1]
        # If the current letter is NEITHER a lowercase NOR an uppercase version of the target vowel...
        else:
            # ...append it to the new line without changes
            new_line += letter
            
    # Return the new line
    return new_line
