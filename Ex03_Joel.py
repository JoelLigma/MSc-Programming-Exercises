# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:11:38 2020

@author: Joel
"""
# initialize useful variables
size = 8 # grid size
#count = 0 # just for keeping track of the number of solutions

def mk_empty_grid() :
    """
    This function creates an empty size by size grid containing 0s, depending on the 
    predetermined variable: size. 
    """
    global grid
    grid = []
    for i in range(size) :
        row = []
        for j in range(size) :
            row = row + [0]
        grid = grid + [row]
    return grid

def print_grid() :
    """
    This function prints a grid, predefined in mk_empty_grid(), with "." for 0 and "Q" for 1.
    """   
    for row in range(size) :
        for col in range(size) :
            if grid[row][col] == 0 : 
                print(".",end=" ") # print "." when grid shows 0
            elif grid[row][col] == 1 :
                print("Q",end=" ") # print "Q" when grid shows 1
            else :
                print(grid[row][col],end=" ")
        print()

def is_possible(Q,x) :
    """
    This function checks for conflicts in row y, column x as well as diagonally and 
    returns True or False whether it is possible to place a queen or not.
    """
    for i in range(size) : # check if queen in col
        if grid[i][x] == 1 : 
            return False # return False if it does 
    for i in range(size) : # check for diagonal conflict
        for j in range(size) :
            if ((i+j == Q+x) or (i-j == Q-x)) and grid[i][j] == 1: 
                return False # return False if it does 
    return True # if no conflicts return True

def solve(Q = 0) :
    """
    This function solves the Queen's Puzzle using recursion as well as making
    use of possible() to check for conflicts and print_grid() to print the solution(s).
    """
    #global count
    if Q == size: # stopping condition
     #   count += 1
        print_grid() # print solution
      #  print(f"\nSolution count: {count}") # keeping track of total solutions
        input("More? ")
        return 
    for x in range(size) : # x == column
        if is_possible(Q, x) : # Q == row, if no conflicts and not a queen placed yet...
            grid[Q][x] = 1 # place queen
            # recursively solve the remaining grid
            solve(Q+1)
            # failed hence lets look for other options
            grid[Q][x] = 0
            
# run functions
mk_empty_grid()
solve()

# diagonal equation source: https://stackoverflow.com/questions/19524155/how-do-you-test-for-diagonal-in-n-queens/48101807