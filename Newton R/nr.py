# Newton-Raphson method, a simple implementation
import math
from random import randint
#f(x) - the function of the polynomial
def f(x):
    function = (x*x) - (2*x) - 1
    return function

def derivative(x): #function to find the derivative of the polynomial
    h = 0.000001
    derivative = (f(x + h) - f(x)) / h
    return derivative

def newton_raphson(x):
    return (x - (f(x) / derivative(x)))

# p - the initial point i.e. a value closer to the root
# n - number of iterations 
def iterate(p, n): #
    x = 0
    for i in range(n):
        if i == 0: #calculate first approximation
            x = newton_raphson(p)
        else:
            x = newton_raphson(iterate(x, n)) #iterate the first and subsequent approximations
        n=n-1
    return x
g = 2
resultados = []

for res in range(0,g):
    print randint(-1, 1)
    if res ==0:
        resultados.append(iterate(1, 5)) #print the root of the polynomial x^3 - 2x - 1 using 3 iterations and taking initial point as 1
    else:
        if randint(1, 100)%2 == 0:
            sign = -1
        else: 
            sign = 1
            
        resultados.append(iterate(resultados[(res-1)]+(sign*randint(-10, 10)), 5)) #print the root of the polynomial x^3 - 2x - 1 using 3 iterations and taking initial point as 1

print resultados    
    

