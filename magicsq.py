import math
import random


# This isn't apart of algorithm, only for nice printing of square
def printsquare(square):
    labels = ['['+str(x)+']' for x in range(0,len(square))]
    
    format_row = "{:>6}" * (len(labels) + 1)

    print(format_row.format("", *labels))

    for label, row in zip(labels, square):
        print(format_row.format(label, *row))

n = 7

square = [[float('nan') for i in range(0,n)] for j in range(0,n)]



center_i = math.floor(n/2)
center_j = math.floor(n/2)

# Populating squares
square[center_i][center_j] = int((n**2 + 1)/2)
square[center_i][center_j] = 1
square[center_i][center_j] = n**2
square[center_i][center_j] = n**2 + 1- n
square[center_i][center_j] = n

# upright is indicator of whether we're looking for the entry up and to thr right of x, if not it will default look for the entry to the bottom left of the x
def rule1(x,n,upright):
    return((x + ((-1)**upright) * n)%n**2)
    # if upright is true then it will subtract n instead of adding n which enables us to go in the other direction

# print(rule1(1,3,True))

# Visualisation of Luo Sho square
"""
4   9   2 
3   5   7
8   1   6
"""

# Rule 2 is by default finding the entry below and to the right of x, so it'll find up and to the left when doing the reverse
def rule2(x,n,upleft):
    return((x + ((-1)**upleft))%n**2)

# For exceptions to rule 2 (only followed when crossing the magic square's antidiagonal)
def rule3(x,n,upleft):
    return((x + ((-1)**upleft * (-n+1)))%n**2)


# Filling out the rest of the square
    # One way to fill in the rest of the square is to "walk" randomly through it

# First - determine the indices of our central entry
center_i = math.floor(n/2)
center_j = math.floor(n/2)

# Then - randomly select a direction to "walk"
entry_i = center_i
entry_j = center_j

where_we_can_go = ['up_left','up_right','down_left','down_right']


def fillsquare(square,entry_i,entry_j,howfull):

    while(sum(math.isnan(i) for row in square for i in row) > howfull):

        where_we_can_go = []

        if(entry_i < (n-1) and entry_j < (n-1)):
            where_we_can_go.append('down_right')

        if(entry_i < (n-1) and entry_j > 0):
            where_we_can_go.append('down_left')

        if(entry_i > 0 and entry_j < (n-1)):
            where_we_can_go.append('up_right')
        if(entry_i > 0 and entry_j > 0):
            where_we_can_go.append('up_left')


        where_to_go = random.choice(where_we_can_go)

        if(where_to_go == 'up_right'):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,True)
        if(where_to_go == 'down_left'):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,False)
        if(where_to_go == 'up_left' and (entry_i + entry_j) != (n)):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,True)
        if(where_to_go == 'down_right' and (entry_i + entry_j) != (n-2)):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,False)

        # How to know if in entry that's near an antidiagonal - the entry just above the antidiagonal will have indices that sum to n-2, and entries just below antidiagonal will have indices that sum to n
        if(where_to_go == 'up_left' and (entry_i + entry_j) == (n)):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,True)
        if(where_to_go == 'down_right' and (entry_i + entry_j) == (n-2)):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,False)

        entry_i = new_entry_i
        entry_j = new_entry_j
    
    return(square)

entry_i = math.floor(n/2) +1
entry_j = math.floor(n/2)

square = fillsquare(square, entry_i, entry_j,0)
printsquare(square)
