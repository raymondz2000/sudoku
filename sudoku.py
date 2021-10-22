# COMP 1005/1405
# Summer 2020
#Raymond Zhu
# Assignment 3


#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file filename. 
        Returns a list of lists of integers.  
    '''
    puzzle = [] 
    f = open(filename, "r")
    for line in f:
        puzzle.append( [int(val) for val in line.split(",")] )   
    f.close()
    return puzzle

# your functions go here!
#------------------------------------------------------------------# puzzle to string
'''
to_str = ''
for col_number in range(len(row)):
    if col_number %3 == 0 and col_number != 0:
        to_str += '|'

    to_str += row[col_number]

    if col_number %8 == 0 and col_number != 0:
        to_str += '\n'

'''
#
def puzzle_to_string(puzzle):
    sudoku_data = list(puzzle)
    puzzlestr=""
    for row_number in range(0,9):
        if row_number %3 == 0 and row_number !=0:
            puzzlestr = puzzlestr + ("------+-------+------") +'\n'
        row = sudoku_data[row_number]
        to_str = str(row).strip("[]") # add every element  + \n , it should be use for loops anyways
        to_str2 = to_str.replace(',','')   
        to_str3 = to_str2.replace('0',' ')
        to_str4 = to_str3[0:5]+ ' | ' + to_str3[6:11]+ " | " + to_str3[12:] 
        puzzlestr = puzzlestr + to_str4 +'\n'
    puzzlestr= puzzlestr. rstrip() #remove newline at the bottom
    return puzzlestr
#-------------------------------------------------# check rows

def check_rows(puzzle):
    sudoku_data = list(puzzle)
    checkedrow=[]
    errorrow=[]
    for row in range(9):
        for col in range(9):
            if sudoku_data[row][col]!=0 and sudoku_data[row][col] in checkedrow:
                errorrow.append(row)
            else:
                 checkedrow.append(sudoku_data[row][col])
        checkedrow.clear()
        errorrow = list(set(errorrow))  #remove repeating row number in case of
    errorrow.sort()
    resultrow = errorrow
    return resultrow

# ------------------------------------------------------------------# check_columns
def check_columns(puzzle):
    sudoku_data = list(puzzle)
    checkedcol=[]
    errorcol=[]
    for col in range(9):
        for row in range(9):
            if sudoku_data[row][col]!=0 and sudoku_data[row][col] in checkedcol:
                errorcol.append(col)
            else:
                checkedcol.append(sudoku_data[row][col])
        checkedcol.clear()
        errorcol= list(set(errorcol)) #remove repeating col number in case of
    errorcol.sort()
    resultcol = errorcol
    return resultcol

#------------------------------------------------------------------# helper function to check subgrid
def find_subgrid(x,y):
    if x in range(0,3):
        if y in range(0,3):
            subgrid = 0
        elif y in range(3,6):
            subgrid = 1
        elif y in range(6,9):
            subgrid = 2
    if x in range(3,6):
        if y in range(0,3):
            subgrid = 3
        elif y in range(3,6):
            subgrid = 4
        elif y in range(6,9):
            subgrid = 5
    if x in range(6,9):
        if y in range(0,3):
            subgrid = 6 
        elif y in range(3,6):
            subgrid = 7
        elif y in range(6,9):
            subgrid = 8
    return subgrid

#------------------------------------------------------------------# subgrids function
def check_subgrids(puzzle):
    sudoku_data = list(puzzle)
    checkedsubgrids=[]
    errorsubgrids=[]
    for row in range(0,9,3):
        for col in [0,3,6]:
            for subrow in range (row,row+3):
                for subcol in range (col, col+3):
                    if sudoku_data[subrow][subcol] != 0 and sudoku_data[subrow][subcol] in checkedsubgrids:
                        errorsubgrids.append(find_subgrid(subrow,subcol))
                    else:
                        checkedsubgrids.append(sudoku_data[subrow][subcol])
            checkedsubgrids.clear()
            errorsubgrids= list(set(errorsubgrids))
    resultsubgrids = errorsubgrids
    return resultsubgrids


#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed
def main():
    filename = input('Please enter your sudoku puzzle file:')
    puzzle = load_puzzle(filename)   
    print(puzzle_to_string(puzzle))

    #puzzle_to_string(puzzle)
    print("checking puzzle")
    if check_rows(puzzle) == []:
        print ("...Rows OK")
    else: 
        print("...Rows",check_rows(puzzle),"failed")

    if check_columns(puzzle) == []:
        print ("...Columns OK")
    else: 
        print("...Columns",check_columns(puzzle),"failed")

    if check_subgrids(puzzle) == []:
        print ("...Subgrids OK")
    else: 
        print("...Subgrids",check_columns(puzzle),"failed")   
    
    
    partial = False
    for row in puzzle:
        if 0 in row:
            partial = True
            str = 'partial'
            break 
        else:
            str= 'complete'
    

    '''
    i = 0
    while partial == False and i < len(puzzle):
        if 0 in puzzle[i]:
            partial = True
        i += 1 
    '''

    if  check_columns(puzzle) == [] and check_rows(puzzle) == [] and check_subgrids(puzzle) == []:
        print( str + " puzzle solution is correct!")
    else:
        print( str +" puzzle solution is NOT correct!")

#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()