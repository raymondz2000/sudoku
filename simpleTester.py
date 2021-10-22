# Simple Tester
# 
# puzzle_to_string, check_rows, check_columns, check_subgrids, (main?)


import sudoku

p1 = "5 3 4 | 6 7 8 | 9 1 2\n" +\
"6 7 2 | 1 9 5 | 3 4 8\n" +\
"1 9 8 | 3 4 2 | 5 6 7\n" +\
"------+-------+------\n" +\
"8 5 9 | 7 6 1 | 4 2 3\n" +\
"4 2 6 | 8 5 3 | 7 9 1\n" +\
"7 1 3 | 9 2 4 | 8 5 6\n" +\
"------+-------+------\n" +\
"9 6 1 | 5 3 7 | 2 8 4\n" +\
"2 8 7 | 4 1 9 | 6 3 5\n" +\
"3 4 5 | 2 8 6 | 1 7 9"

def getPuzzle(n):
    puzzle = [] 
    f = open('puzzle' + str(n) + '.csv', "r")
    for line in f:
        puzzle.append( [int(val) for val in line.split(",")] )
    f.close()
    return puzzle
def compareStrings(s1, s2):
    if len(s1) > len(s2):
        print (s1 + ' has more characters than ' + s2)
        return
    elif len(s1) < len(s2):
        return print(s1 + ' has less characters than ' + s2)
        return


    for index in range(len(s1)):
        c1, c2 = s1[index], s2[index]
        if s1[index] == '\n':
            c1 = '\\n'
        if s2[index] == '\n':
            c2 = '\\n'
        print( '\"' + c1 + '\"',  '\"' + c2 + '\"')
        if c1 != c2:
            print("Yikes! something not right here")

def  main():
    puzzle = getPuzzle(1)

    print('...'*9)
    print('puzzle_to_string')
    print('...'*9)
    
    # call puzzle_to_string
    expected = p1
    actual = sudoku.puzzle_to_string(puzzle)

    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected string is')
        print(expected)
        print('actual string is')
        print(actual)
    

    print("########## puzzle1.csv")
    
    print('...'*9)
    print('check_rows')
    print('...'*9)
    actual = sudoku.check_rows(puzzle)
    expected = []
    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected is ', expected)
        print('actual is   ', actual)

    print('...'*9)
    print('check_columns')
    print('...'*9)
    actual = sudoku.check_columns(puzzle)
    expected = []
    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected is ', expected)
        print('actual is   ', actual)


    print('...'*9)
    print('check_subgrids')
    print('...'*9)
    actual = sudoku.check_subgrids(puzzle)
    expected = []
    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected is ', expected)
        print('actual is   ', actual)


    print("########## puzzle2.csv")

    puzzle = getPuzzle(2)

    print('...'*9)
    print('check_rows')
    print('...'*9)
    actual = sudoku.check_rows(puzzle)
    expected = []
    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected is ', expected)
        print('actual is   ', actual)

    print('...'*9)
    print('check_columns')
    print('...'*9)
    actual = sudoku.check_columns(puzzle)
    actual.sort()
    expected = [0,1,2,3,4,5,6,7,8]
    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected is ', expected)
        print('actual is   ', actual)


    print('...'*9)
    print('check_subgrids')
    print('...'*9)
    actual = sudoku.check_subgrids(puzzle)
    actual.sort()
    expected = [0,1,2,3,4,5,6,7,8]
    if expected == actual:
        print('----> expected output matches your actual output')
    else:
        print('----> something is not quite right')
        print('expected is ', expected)
        print('actual is   ', actual)

if __name__ == "__main__":
    main()