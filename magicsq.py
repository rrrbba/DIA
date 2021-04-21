
# This isn't apart of algorithm, only for nice printing of square
def printsquare(square):
    labels = ['['+str(x)+']' for x in range(0,len(square))]
    
    format_row = "{:>6}" * (len(labels) + 1)

    print(format_row.format("", *labels))

    for label, row in zip(labels, square):
        print(format_row.format(label, *row))