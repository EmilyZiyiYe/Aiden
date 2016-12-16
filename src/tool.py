#!/usr/bin/python
import sys


def solution1(inputt, target):
    """
    Given an array with numbers and a value, the function
    returns a 1 or 0 indicating whether the numbers in the
    array can be used to reach the targeted value. ('1' is yes;
    '0' is no; numbers in the array can be used more than once.
    """
    # Recursive algorithm is used for this function
    
    result = 0 # Initialize "result"(the variable of the final output) as 0

    # Following 11 lines of code are base cases

    for ele in inputt:  # Iterate over the array to check whether there is
                        # a number equal to the target value or whether the
                        # target value is the multiple of a number. If either of the
                        # situation is true, then directly return 1 since the target value can
                        # be reached by its factors.
        
        if (target == ele)or (target % ele == 0): 
            return 1
        
    
    if (len(inputt) == 0): # If the array contains no number, then the target value
                           # cannot be reached. Return 0.
        return 0
    
    
    if (len(inputt) == 1) : # If there is only one number in the array and
                            # the number isn't equal to the target value,
                            # then the target value cannot be reached. Rreturn 0.
        if inputt[0] != target:
            return 0
    
    
    for ele in inputt: # Iterate over the array and remove numbers that are larger
                       # than the target value because they cannot be used to reach the target value.
        if ele > target:
            inputt.remove(ele)

    # a&b below are recursive cases
    
    a = solution1(inputt[:-1], target) # the first scenario that may happen to the last
                    # number in the array is that it is not used for reaching the value.
                    # Then the issue becomes whether the target value can be reached with
                    # rest of numbers in the array
    b = solution1(inputt, (target-inputt[-1])) # the second scenario that may happen to the
                    # the last number in the array is that it is used for reaching the value.
                    # then the issue becomes whether (the target value - the last number) can
                    # be reached by the given array of numbers.
    
    
    if a > b: # see which scenario works by cmparing their values(a&b can only be one or zero
              # since those are the only output in base cases) The scenario with '1' means it
              # eventually reach the value, then we update variable "result"
        result += a
    else:
        result += b

    return result 



if __name__ == "__main__": # used for turning into command line tool
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	argv_converted = [int(k) for k in sys.argv[1:]]
	argv1 = argv_converted[:-1]
	argv2 = argv_converted[-1]
	print solution1(argv1, argv2)

        


