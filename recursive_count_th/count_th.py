'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word_length = len(word)
    print('word length', word_length)
    # TBC
    if len(word) < 2:
        return 0
    def helper_function(amount, countdown, index):
        if countdown + 1 == word_length:
            return amount
        elif word[index] == 't' and word[index+1] == 'h': 
            return helper_function(amount+1, countdown+1, index+1)
        else:
            return helper_function(amount, countdown+1, index+1)
        return amount
    return(helper_function(0, 0, 0))



'''
Im going to need a variable to count the number of occurances

Im going to need a base case for len(word)<2

the recursive part of the function will be checking if n == t and n+1 == h
    the helper function will take in an index and increment by 1
    if word[n] == 't' and word[n+1] == 'h':
        occurances = occurances + 1

it will go through the recursive part until it has reached the len(word)

'''

'''
****works...kinda****

def count_th(word):
    # ammount = 0
    # index = 0
    word_length = len(word)
    # TBC
    if len(word) < 2:
        return 0
    def helper_function(amount, countdown, index):
        # print('countdown', countdown)
        # print('index', index)
        # amount = 0
        # print('amount', amount)
        if countdown == word_length:
            return amount
        elif word[index] == 't' and word[index+1] == 'h':
            # amount = amount +1
            # print('occurence in helper', amount) 
            return helper_function(amount+1, countdown+1, index+1)
        else:
            return helper_function(amount, countdown+1, index+1)
        return amount
    return(helper_function(0, 0, 0))
    # print('amount', amount)
    # return ammount

'''