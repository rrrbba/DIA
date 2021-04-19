import math 
import pandas as pd

n1 = 89
n2 = 18

halving = [n1]
doubling = [n2]

while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))

while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)