import re

"""
- Write a function that accepts a lengthy string parameter.
- Without utilizing any of the built-in library methods available to your language, 
return the first word to occur more than once in that provided string.
- Modify your function to return a count of each of the words in the provided string
- Modify your function to return a list of the words most frequently used in the provided string
- Python: a folder named repeated_word which contains a file called repeated_word.py
"""

def repeated_word(string):
    '''
    Takes a string and returns first word to occur more
    than once in that provided string.
    '''
    unique = set()
    phrase = string.lower().split(' ')

    for word in phrase:
        word = re.sub(r'\W', '', word)
        if word in unique:
            return word
        unique.add(word)

    return None

if __name__ == "__main__":
    test_word = 'asd f8u3! ASD, ksu12 34 @$!!'
    output = repeated_word(test_word)
    print(output)