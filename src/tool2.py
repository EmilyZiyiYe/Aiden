#!/usr/bin/python
import sys
def num_to_letterlist(number):
    """
    Given a multi_digit number, this function returns a list of lists, where each sublist
    contains the letters that the number on oen digit corresponds to in the keypad of the phone
    ('0'&'1' don't have corresponding letters in the keypad).
    """
    result = []
    for num in str(number):
        num = int(num)
        if num == 2:
            result.append(['a','b','c'])
        elif num == 3:
            result.append(['d','e','f'])
        elif num == 4:
            result.append(['g','h','i'])
        elif num == 5:
            result.append(['j','k','l'])
        elif num == 6:
            result.append(['m','n','o'])
        elif num == 7:
            result.append(['p','q','r','s'])
        elif num == 8:
            result.append(['t','u','v'])
        elif num == 9:
            result.append(['w','x','y', 'z'])
    return result

            
def letter_to_num(letter):
    """
    Given a list of letters, this function returns the number that these letters
    correspond to in the keypad of the phone.
    """
    if letter == ['a','b','c']:
        return 2
    elif letter == ['d','e','f']:
        return 3
    elif letter == ['g','h','i']:
        return 4
    elif letter == ['j','k','l']:
        return 5
    elif letter == ['m','n','o']:
        return 6
    elif letter == ['p','q','r','s']:
        return 7
    elif letter == ['t','u','v']:
        return 8
    elif letter == ['w','x','y', 'z']:
        return 9
    

def permutation(llist, _permutation):
    """
    Given a list of n lists where each sublist contains letters, this function
    returns the permutations of letters from each sublist.
    eg. [['a', 'b'], ['c', 'd', 'e']] --> ['ac', 'ad', 'ae, 'bc', 'bd', 'be']
    """
    # recursive algorithm is used for this function
    if str(llist) in _permutation: # variable "_permutation'is mostly an empty dictionary
                                   # that is used to keep track of already computed input and its
                                   # output so that it dosn't spend unnecessary time doing repetitive work
        return _permutation[str(llist)]
    
    if len(llist) == 1: # base case: if there is only one sublist, then the
                        # permutation is the sublist itself
        return llist[0]
    else:
        #recursive case
        result = [] # create an empty list to contain permutations later
        for i in llist[-1]: # obtain the permutation of letter from n sublists
                            # by respectively adding the elements from the last(nth)
                            # list to the permutation result of previous n-1 sublists
            for ele in permutation(llist[:-1], _permutation):
                result.append(ele + i)
                
        _permutation[str(llist)] = result # enter the newly computed result into dictionary _permutation
                                          # for later use
        return result 
    

def findword(inputt):
    """
    Given a multi-digit number that doesn't contain 0 or 1, this function
    returns a mixed string of words and numbers, where words are spelled by
    the same digit number's corresponding letter (find words as much as possible)
    """
    # dynamic programming is used for this function 
    
    file_object = open('usa2.txt', 'r') #read the text file of dictionary words
    data = file_object.read()
    dictionary = data.splitlines()

    letter_list = num_to_letterlist(inputt) # turn the input number into list of lists where each sublist
                                            # represents its corresponding letters in keypad
    num = len(letter_list) 
    _permutation = {} # create an empty dictionary for the permutation function that is used later

    if num == 0:  # special case: when the input is not valid, return an empty string
        return ''
    elif num == 1: # special case: when the input is one digit number, return this number since it can't form word
        return str(inputt)
    else:
        opt_list = [[letter_to_num(letter_list[0])]] # this is a list of lists where the nth sublist is used for recording
                                                     # the optimal combination of words and numbers up until the
                                                     # nth digit of the input number (dynamic programming data structure)

        for n in range(num-1): # occupy the empty list positions with True, will be replaced by real sublist values later
            opt_list.append(True)

        for i in range(1,num): # this tries to find the  the optimal combination of words and numbers up until the
                               # nth digit of the input number. 

            a = len(opt_list[i-1]) + 1 # situation1: if we dont include the ith digit, then the number of
                                       # items in the combination(a single word or a number is considered as an
                                       # item) is (i-1)th digit's number of optimal items plus one

            for previous in range(i): # situation2: if we include the ith digit, then we need to find a word that
                                      # combines the ith digit's letters with the letters of previous digits
                perm = permutation(letter_list[previous:i+1], _permutation)
                word = ''
                for ele in perm: # iterate the permutation to see whether there is a dictionary word. Breaks
                                 # the loop once find a word
                    if ele in dictionary:
                        word = ele
                        break
                if word != '':
                    break
            
            if len(word) == 0: # if the ith digit can't form a word, then situation2 = situation1
                b = a
            elif i+1 == len(word): # if the ith digit can form a word with all digits before it, then there is only one
                                   # item to remember
                b = 1
            else:
                b = len(opt_list[i - len(word)]) + 1 # If the ith digit form a word of length k, then the number of items are the
                                                     # is (i-k)th digit's number of optimal items plus one
            
            # compare which situation generates less items to remember and then update "opt_list" with the list with fewer items
            # at ith index
            if a <= b: 
                opt_list[i] = opt_list[i-1] + [letter_to_num(letter_list[i])]
            else:
                if i+1 == len(word):
                    opt_list[i] = [word]
                else:
                    opt_list[i] = opt_list[i - len(word)] + [word]

        # the final sublist in "opt_list" is the result we want. Turn the list into a strng of numbers and words
        result = ''
        for item in opt_list[-1]:
            result += str(item)
        return result 
    

import re
def converter(number):
    """
    Given a multi-digit number that doesn't contain 0 or 1, this function
    returns a mixed string of words and numbers, where words are spelled by
    the same digit number's corresponding letter. The function favors words over numbers.
    """
    
    number = str(number) # turn number into a string 
    pattern = '1|0'
    zero_one = re.findall(pattern, number) # find all the 0 and 1 in the number string
    words = [] 
    for ele in re.split(pattern,number): # use function findword() to find words in sequences of
                                         # digits between 0's and 1's
        if ele == '':
            words.append(ele)
        else:
            a = findword(int(ele))
            words.append(a)

    if zero_one == []: 
        return words[0]

    if words == ['']:
        return str(number)

    result = words[0]
    for i in range(len(zero_one)): # combine 0's, 1's and the words find between them together. The order
                                   # should remain the same.
        result += zero_one[i]
        result += words[i+1]
    return result 
        
    
if __name__ == "__main__": # used for turning the code into command line tool
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
        inputstring = ''
	for num in sys.argv[1:]:
            inputstring +=  num
        inputt = int(inputstring)
	print converter(inputt)




