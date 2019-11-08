'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

cache = {}


def count_th(word):
    n = 0
    amount = 0
    global cache
    # TBC
    if word == "" or len(word) == 1:
        print('first base')
        return 0
    if word[n] == "t" and word[n+1] == "h":  # word[n] and word[n+1]
        amount = amount + 1
        print(f'amount after increment: {amount}')
    if word[n] not in cache:
        cache[word[n]] = count_th(word[:n])
        n = n + 1
    print(f'letter at index: {word[n]}')
    print(f'word length: {len(word)}')
    if n == len(word)-1:
        return amount


'''
Your function should take in a signle parameter (a string word)
Your function should return a count of how many occurences of "th" occur within word. Case matters.
Your function must utilize recursion.
It cannot contain any loops.

# Understand

-I need to go through the string and look for instances of the lower case letter t
-I need to check if following letter is an h
-I need to check for case but that should be easy since their not equal

# Planning

-I need a base case for if the sting is empty
-I need to declare n = 0 
-I need to declare an amount = 0
-I need a base case for checking if base case of n is a t and if it is if the following letter is an h then amount = 1
-I need an empty dict (cache) to store the 'n' value which will be each 'index' in a string.  for example word[1] should print first letter 
    -I should have an if statement checking if n is in the cache
    -it should then be incremented by 1
        -count_th(word[:n+1])
        -it should cycle through and hit the base cases at every lowercase t
'''
