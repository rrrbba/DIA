



def gcd(x,y):
    larger = max(x,y)
    smaller = min(x,y)

    remainder = larger % smaller

    if(remainder == 0):
        return(smaller)

    if(remainder != 0):
        return(gcd(smaller,remainder))

x = 105
y = 33

print(gcd(x,y))