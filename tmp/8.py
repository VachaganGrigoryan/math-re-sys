from functools import reduce

Ft = ["a*b", "a*c*e", "d*e", "d*c*b"]

exc = reduce(lambda a, b: f"({a})+({b})-({a})*({b})", Ft)

a = b = d = e = 0.9
c = 0.8

print( "P : ", eval(exc))
print(eval("c*((a+d-a*d)*(b+e-b*e))+(1-c)*(a*b+d*e-a*b*d*e)"))

# k = c
# c = 1

# st = reduce(lambda a, b: f"({a})+({b})-({a})*({b})", F)

# ex1 = eval(f'k*({st})')

# c = 0

# ex2 = eval(f'(1-k)*({st})')

# print(ex1+ex2)
