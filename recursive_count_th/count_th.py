'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base-case: length of the word has been traversed
    # if length is 0 or 1, not enough characters for count of th to increment
    if len(word) <= 1:
        return 0
    
    if word[0:2] == 'th':
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])

    # recurse until length of string is done

word = 'ththsafszdfnth'
print(count_th(word))