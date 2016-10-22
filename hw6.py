# File: hw6.py
# Author: Uzoma Uwanamodo
# Date: 10/21/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# A simple math helper program
# Collaboration:
# I did not collaborate with anyone on this assignment




# summation() Return sum of list of integers
# Input: a list; the integer list
#Output: The sum of the integers in the list
def summation(*ints): 

    # Variable that will calculate the sum
    total = 0
    
    # Add all the numbers
    for i in ints:
        total += i 
    return total


# multiply() Return product of list of integers
# Input: a list; the integer list
#Output: The sum of the integers in the list (or 0, if the list is empty)
def multiply(*ints):
    #Variable that will calculate the product
    total = 1
    
    # Multiply all the numbers
    for i in ints:
        total *= i
    
# If the list has elements, return the product, otherwise, return 0
    return total if len(ints) else 0





# createIntList() Create a list of integer from user input
# Input: an integer, the sentinel
# Output: a list, a list of integers created with the users input
def createIntList(SENTINEL):

    # List of integers
    intList = []
    
    # Prompt user for integers
    promptInt =int( input("Please enter a number, %s to stop: " % SENTINEL))
    
    # Continue to prompt user for integers until they input SENTINEL value
    while promptInt != SENTINEL:
        intList.append(promptInt)
        promptInt =int( input("Please enter a number, %s to stop: " % SENTINEL))
    
    return intList




def main():
    
    # Welcome user
    print("Welcome to the Simple Math Helper")
    
    # Prompt user for number of lists
    numLists = int(input("How many lists would you like to create? "))
    
    # Create the lists (start indexing from 1 instead of 0)
    for i in range(1,numLists+1):
        
        # Display List #
        print("\nYou are creating list #%s" % i)
        
        # Prompt user for SENTINEL value
        SENTINEL = int(input("What do you want the sentinel to be? "))
        
        # Create the list
        currentList = createIntList(SENTINEL)
        
        # Print the list, the sum, and the product
        print("For the list",currentList,"\nThe summation is",summation(*currentList),"\nThe product is",multiply(*currentList))
        
    # Thank user after all the lists have been operated on
    print("Thank you for using the Simple Math Helper")


main()