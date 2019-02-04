# Just a miniature set of functions to automatically solve any
# humanly-solveable 9x9 sudoku puzzle.
#
# Just serves a small, quick-to-read example to demonstrate my
# intermediate Python proficieny, as well as my current coding
# style.
# May be expanded on as I learn or require more things to
# demonstrate.
#
# Logic:
# Uses a simple backtracking algorithm, which works by:
#   1) Generating a list of solutions for a given puzzle
#   2) Incorporating those solutions into a reference puzzle
#   3) Generating a list of solutions for this reference puzzle,
#      and repeating the proceses
#
# Further Steps:
#   1) Some puzzles go beyond 9x9. This can be adapted
#   2) The squareNeighbours(x, y, table) function can probably be
#      simplified a little bit
#   3) Develop an AR app around this logic (Much larger project)


import copy

def horizontalNeighbours(x, y, table):
    return table[x];

def verticalNeighbours(x, y, table):
    return [x[y] for x in table] 

def squareNeighbours(x, y, table):
    if(0 <= x <= 2):
        if(0 <= y <= 2):
            return table[0][:3] + table[1][:3] + table[2][:3]
        elif(3 <= y <= 5):
            return table[0][3:6] + table[1][3:6] + table[2][3:6]
        else:
            return table[0][6:9] + table[1][6:9] + table[2][6:9]
    elif(3 <= x <= 5):
        if(0 <= y <= 2):
            return table[3][:3] + table[4][:3] + table[5][:3]
        elif(3 <= y <= 5):
            return table[3][3:6] + table[4][3:6] + table[5][3:6]
        else:
            return table[3][6:9] + table[4][6:9] + table[5][6:9]
    else:
        if(0 <= y <= 2):
            return table[6][:3] + table[7][:3] + table[8][:3]
        elif(3 <= y <= 5):
            return table[6][3:6] + table[7][3:6] + table[8][3:6]
        else:
            return table[6][6:9] + table[7][6:9] + table[8][6:9]
        
        
#Generates a list of possible solutions to any
#X Y position of a given TABLE
def possibleSolutions(x, y, table):
    val = table[x][y];
    hn = horizontalNeighbours(x, y, table)
    vn = verticalNeighbours(x, y, table)
    sn = squareNeighbours(x, y, table)
    possibleValues = range(1,10)
    
    if(val == 0):
        taken = set(hn).union(set(vn), set(sn))
        possibleValues = set(possibleValues) - taken
    else:
        return [val]
    return list(possibleValues)


def generateSolutionList(table):
    """Generates a list of solutions for a particular table"""
    solutionList = [[] for i in range(9)]
    
    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            solutionList[i].append(possibleSolutions(i, j, table))
    
    return solutionList

def checkSolved(table):
    """Just looks for 0s to see if a table is fully solved"""
    for row in table:
        for item in row:
            if (item == 0):
                return False
            
    return True

#Generate a list of potential solutions for each element
#Go through the entire table. If it'z zero, look for possible solutions
#If it's a number, that's the solution

#While not solved, generate a list of solutions
#From the solutions, copy them over to the reference table
#if they are singular items
def solvePuzzle(referenceTable):
    #Old table is preserved for sake of immutability
    table = copy.deepcopy(referenceTable)
    solved = checkSolved(table)

    
    while(not solved):

        solutionList = generateSolutionList(table)
        
        for i in range(len(solutionList)):
            for j in range(len(solutionList[0])):
                if(len(solutionList[i][j]) == 1):
                    table[i][j] = solutionList[i][j][0]

        solved = checkSolved(table)


    return table
                
def printPuzzle(table):
    for row in table:
        print(row)

#Example
a =  [[0,0,0,0,8,5,4,2,1],
      [0,2,0,0,0,0,0,5,0],
      [5,1,0,0,0,6,0,0,0],
      [7,0,0,0,5,9,0,0,0],
      [1,0,0,8,7,3,0,0,2],
      [0,0,0,4,6,0,0,0,7],
      [0,0,0,5,0,0,0,4,6],
      [0,8,0,0,0,0,0,7,0],
      [2,9,6,7,1,0,0,0,0]]

solution = solvePuzzle(a)
printPuzzle(solution)
