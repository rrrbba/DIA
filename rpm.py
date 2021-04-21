import math 
import pandas as pd # enables to work with tables easily

# faster if larger number is the doubling and smaller is halving 
n1 = 18
n2 = 89

halving = [n1]
doubling = [n2]

while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))

while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)

half_double = pd.DataFrame(zip(halving, doubling))
# zip joins halving and doubling together

# keep only the rows of the table whose entry in the halving column is odd
half_double = half_double.loc[half_double[0]%2 == 1, :]
# loc selects only the rows you want - in this case all rows where halving is odd, the colon means we want all the columns

answer = sum(half_double.loc[:,1])

print(answer)
