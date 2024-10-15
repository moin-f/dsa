#Q.1.3 using python find the area of triangle whose base is 10 and height is15
b=10
h=15
A =(1/2)*h*b
print('area of triangle is ', A)

#Q.2.2 Write python code to find value the function f(x)=x^2+x (-5<=x<=5)
for x in range (-5,5):
    f=x**2+x
    print(f)

#Q.2.3write python program to find determinant of matrix 
# A=[ 1 0 5 ;2 1 6  ;3 4 0] and B=[ 2 5  ; -1 4]
import sympy as sy
sy.init_printing()
A=sy.Matrix([[1,0,5],[2,1,6],[3,4,0]])
B=sy.Matrix([[2,5],[-1,4]])
print('det(A)= ',A.det())
print("det(B) = ",B.det())

#Q.3a.1 Write Python program to estimate the value of the integral  integral 1 to 3 (1/x) dx using Simpson's (1/3)rd rule (n=8).

def f(x):
    return 1 / x

def simpsons_rule(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    
    h = (b - a) / n
    sum_odd = sum(f(a + (2 * i + 1) * h) for i in range(n // 2))
    sum_even = sum(f(a + 2 * i * h) for i in range(1, n // 2))
    
    integral = (h / 3) * (f(a) + f(b) + 4 * sum_odd + 2 * sum_even)
    return integral

# Define the interval and number of subintervals
a = 1
b = 3
n = 8

# Calculate the integral using Simpson's (1/3)rd rule
result = simpsons_rule(a, b, n)
print(f"The estimated value of the integral is: {result}")

#Q.3b.2 Write Python program to estimate the value of the integral 0 to 1 cos(x)dx using Trape- zoidal rule (n=5).

import math

# Define the function to integrate
def f(x):
    return math.cos(x)

# Function to calculate the integral using Trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2  # Initial value with the first and last terms
    
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    
    integral *= h
    return integral

# Define the interval [a, b] and number of subintervals n
a = 0
b = 1
n = 5

# Calculate the integral
result = trapezoidal_rule(a, b, n)
print(f"The estimated value of the integral is: {result:.6f}")


