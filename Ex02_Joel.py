# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:08:23 2020
@author: Joel
"""
# initialize useful variables
MIN = 1
MAX = 100
count = 0
# inform the player about the range
print(f"Think of a number between {MIN} and {MAX}!")
# start the game
while True :
    MID = int(MIN + (MAX - MIN) / 2) # use binary search algorithm to half the solution space for each iteration
    answer = input(f"Is your number greater (>), equal (=), or less (<) than {MID}? Please answer <, =, or >! ")
    count += 1
    if answer == "=" :
        print("\nI have guessed it!")
        break # the program won the game so we end it
    elif answer == "<" :
        MAX = MID - 1 # update MAX since player answered "less" 
        if MID == MIN : # detecting a contradiction in user input
            print("\nYou are lying!")
            break # contradiction detected so end the game
    elif answer == ">" :
        MIN = MID + 1 # update MIN since player answered "greater" 
        if MID == MAX : # detecting a contradiction in user input
            print("\nYou are lying!")
            break # contradiction detected so end the game
    else : 
        print("Please only answer <, =, or >!") # error handling without try and except
        count -= 1 # avoid counting incorrect inputs as steps
print(f"\nI needed {count} steps!")

# binary search algorithm source:
# https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.html