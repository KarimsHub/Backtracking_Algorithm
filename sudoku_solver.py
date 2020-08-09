# Sudoku solver with backtracking algorithm


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)): # creates a list which is as long as the amount of rows on the board and than loops over each item in list
        if i % 3 == 0 and i != 0: # after every three rows we want to draw a line
            print('- - - - - - - - - - - - -')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0: # have to check if its not zero because of the first colum in the row we would print sth we wont
                print(" | ", end="")
            if j == 8: # checking if we are at the last position
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def solve(bo): # if we cant get to the solution we reset that value and repeat that process recursevily
    # print(bo) # to see the actual process of finding the solution
    find = find_empty(bo)
    if not find:
        return True # found the final solution
    else:
        row, col = find # if it's not the case that we got the solution find has to give us a col and row value

    for i in range(1,10):
        if valid(bo, i, (row, col)): # if the value is valid we insert i
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0 # the last added value can#t be correct so we reset the value

    return False


# function to check if the insertion is valid or not
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # we ignore the position we inserted the value right before, because it would be the same number of course
            return False # we found a duplicate

    # Check column
    for i in range(len(bo)): # looping through every single row (0-9)
        if bo[i][pos[1]] == num and pos[0] != i: # check if the current clounm value is equal to the number we inserted
            return False # we found a duplicate

    # Check box (have to check in which box we´re in)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False # found a duplicate

    return True


# function to pick empty squares
def find_empty(bo):
    for i in range(len(bo)): 
        for j in range(len(bo[0])): # length of each row
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None # need to return none if we want to solve finally

print_board(board)

solve(board)
print('__________________________')
print_board(board)