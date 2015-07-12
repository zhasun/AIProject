# SUDOKU SOLVER

import sys
import string
import copy
from time import time
from sudokuUtil import *

# Please implement function solve_puzzle
# input puzzle: 2D list, for example:
# [ [0,9,5,0,3,2,0,6,4]
#   [0,0,0,0,6,0,1,0,0]
#   [6,0,0,0,0,0,0,0,0]
#   [2,0,0,9,0,3,0,0,6]
#   [0,7,6,0,0,0,0,0,3]
#   [3,0,0,0,0,0,0,0,0]
#   [9,0,0,5,0,4,7,0,1]
#   [0,5,0,0,2,1,0,9,0]
#   [0,0,8,0,0,6,3,0,5] ]
# Return a 2D list with all 0s replaced by 1 to 9.
# You can utilize argv to distinguish between algorithms
# (basic backtracking or with MRV and forward checking).
# For example: python sudokuSolver.py backtracking
def solve_puzzle(puzzle, argv):
    """Solve the sudoku puzzle."""

    def constraints_Satisfy(puzzle, count):
        row = count / 9
        col = count % 9

        for k in range(9):
            if puzzle[row][k] == puzzle[row][col] and k != col:
                return False
                break

        for k in range(9):
            if puzzle[k][col] == puzzle[row][col] and k != row:
                return False
                break

        tempRow = (row/3)*3
        tempCol = (col/3)*3
        for i in range(tempRow, tempRow+3):
            for j in range(tempCol, tempCol+3):
                if puzzle[i][j] == puzzle[row][col] and i != row and j != col:
                    return False
                    break
        return True


    def backtracking(puzzle, count):

        if count ==81:
            save_sudoku('solution.txt', puzzle)
            return True

        row = count / 9
        col = count % 9
        if puzzle[row][col]==0:
            for i in range(1,10):
                puzzle[row][col] = i
                if constraints_Satisfy(puzzle, count) and backtracking(puzzle, count+1):
                    return True
                puzzle[row][col] = 0
        else:
            return backtracking(puzzle, count+1)


#def mrv_fc_ac(puzzle):
    #MRV
    def mrv(puzzle):
    	temp = 0
    	min_value = 10
        for c in range(81):
            row = c / 9
            col = c % 9
            if puzzle[row][col] == 0:
                min_value = len(Domain[c])
                temp = c
                break
            else:
                return -1
        for c_min_value in range(temp+1, 81):
            row = c_min_value / 9
            col = c_min_value % 9
            if puzzle[row][col] == 0 and len(Domain[c_min_value]) < min_value:
                min_value = len(Domain[c_min_value])
        for c_min in range(81):
            row = c_min / 9
            col = c_min % 9
            if puzzle[row][col] == 0 and min_value == len(Domain[c_min]):
                return c_min
    #forward checking
    def forwardchecking(puzzle):
        count = mrv(puzzle)
        if count < 0:
            save_sudoku('solution.txt', puzzle)
            return True

        removed = list()
        row = count / 9
        col = count % 9
        for i in Domain[count]:
            puzzle[row][col] = i
            if constraints_Satisfy(puzzle, count):
                for k in range(9):
                    if puzzle[row][k] == 0 and k != col:
                        tempCount = row*9 + k
                        if exist(Domain[tempCount], i):
                       	    Domain[tempCount].remove(i)
                       	    removed.append(tempCount)
                        if len(Domain[tempCount]) == 1:
                            puzzle[row][k] = Domain[tempCount]

                    if puzzle[k][col] == 0 and k != row:
                       	tempCount = k*9 + col
                    	if exist(Domain[tempCount], i):
                       	    Domain[tempCount].remove(i)
                            removed.append(tempCount)
                        if len(Domain[tempCount]) == 1:
                            puzzle[k][col] = Domain[tempCount]
                tempRow = (row/3)*3
                tempCol = (col/3)*3
                for m in range(tempRow, tempRow+3):
                    for j in range(tempCol, tempCol+3):
                        if puzzle[m][j] == 0 and m != row and j != col:
                            tempCount = m*9 + j
                            if exist(Domain[tempCount], i):
                        	    Domain[tempCount].remove(i)
                        	    removed.append(tempCount)
                            if len(Domain[tempCount]) == 1:
                                puzzle[m][j] = Domain[tempCount]
                if forwardchecking(puzzle) == True:
                	return True
            puzzle[row][col] = 0
            for r in removed :
                Domain[r].append(i)

    #to determine whether Elist contains n or not
    def exist(Elist, n):
        for i in range(len(Elist)):
            if Elist[i] == n:
                return True
            else:
                return False


    count = 0

    # initialization
    Domain = dict()
    for c in range(81):
        row = c / 9
        col = c % 9
        EachDomain = list()
        if puzzle[row][col] == 0:
            for i in range(1, 10):
                puzzle[row][col] = i
                if constraints_Satisfy(puzzle, c):
                    EachDomain.append(i)
            puzzle[row][col] = 0
            Domain[c] = EachDomain

    if cmp(argv[0],'backtracking'):
        return backtracking(puzzle, count)
    else :
        return forwardchecking(puzzle)

#===================================================#
puzzle = load_sudoku('puzzle.txt')
print puzzle


print "solving ..."
t0 = time()

solution = solve_puzzle(puzzle,sys.argv)

t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."



