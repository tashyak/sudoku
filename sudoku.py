
#global variable set to 0
backtracks = 0


def findNextCellToFill(grid):
    for x in range(9):
         for y in range(9):
             if grid[x][y] == 0:
                 return x, y
    return -1, -1

#check if setting the (i, j) square to 'e' is valid
def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            #find the first x,y position in the 3*3 square
            topX, topY = 3*(i//3), 3*(j//3)
            for x in range(topX, topX+3):
                for y in range(topY, topY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

def solveSudoku(grid, i=0, j=0):
    global backtracks

    #find next cell to fill
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True
    
    for e in range(1,10):
        #trying different values in i,j location
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i , j):
                return True
            
            #undo the current cell for backtracking
            backtracks += 1
            grid[i][j] = 0
    return False

def printSudoku(grid):
    numrow = 0
    for row in grid:
        if numrow % 3 == 0  and numrow != 0:
            print(' ')
        print (row[0:3], row[3:6], row[6:9])
        numrow += 1
    return

hard = [[8,5,0,0,0,2,4,0,0],
        [8,0,0,0,0,0,0,2,0],
        [0,7,0,0,1,0,5,0,0],
        [4,0,0,0,0,5,3,0,0],
        [0,1,0,0,7,0,0,0,6],
        [0,0,3,2,0,0,0,8,0],
        [0,6,0,5,0,0,0,0,9],
        [0,0,4,0,0,0,0,3,0],
        [0,0,0,0,0,9,7,0,0]]

inp2 = [[5,1,7,6,0,0,0,3,4],
        [0,8,9,0,0,4,0,0,0],
        [3,0,6,2,0,5,0,9,0],
        [6,0,0,0,0,0,0,1,0],
        [0,3,0,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]]

printSudoku(inp2)
print(solveSudoku(inp2))
printSudoku(inp2)
print(backtracks)

