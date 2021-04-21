import math



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


