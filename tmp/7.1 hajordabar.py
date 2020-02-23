import math

n = int(input("Enter n : "))
myu = float(input("Enter myu : "))
lmd = float(input("Enter lmd : "))
#n-brigadi tiv: n=m+1
#m- pahustayin tarreri tiv
x = myu/lmd
P1 = x**n/(math.factorial(n)*sum(x**j/math.factorial(j) for j in range(n+1)))  # n entahamakarg u 1 brigad
#P1=Kph1
# P1 = myu**n/(lmd+myu)**n # n entahamakarg u n brigad

print('P1 : %.20f' % P1)
