# 1.Write Python code to calculate the volume of a sphere with radius r=7 (V=(4/3)pi r^3)
from math import pi 
r=7
result=(4/3)*math.pi *(r**3)
print("volume of sphere is ", result)


# 2. use the python code to construct string operation "+" below string.
 # a. string1= Hello, string2= World!      b. string1=Good ,string2= Morning
a1= "Hello "
a2= "World!"
print(a1+a2)
b1="Good "
b2="Morning"
print(b1+b2)



# 3. write python code to generate the square of numbers from 20 to 30.
n=20
while n<=30:
    print('the square of ',n,'is ',n**2)
    n=n+1



# Q.2.1 use python code find value of f(-2),f(0),f(2)where f(x)=x^2-5x+6
def f(x):
    return x**2-5*x+6
print(f(-2))
print(f(0))
print(f(2))


#Q.2.2 write python program to find the 10 term of sequence of function f(x)=x^3+5x
i=1
while i<=10:
    f=i**3+5*i
    print(f)
    i=i+1


#Q2.3. find the eigen value and corresponding eigen vectors of the matrix A=[4 2 2;

import numpy as np
A= np.array([[4,2,2],
             [2,4,2],
            [2,2,4]])
eigenvalues,p=np.linalg.eig(A)
print("eigen values: ", eigenvalues)
print('eigen vectors: ', p)


#Q.3a.1. Write Python program to estimate the value of the integral 0 to 1  (1/(1+x2)dx using Simp- son's (1/3)rd rule (n=6).
def f(x):
    return 1 / (1 + x**2)

def simpsons_rule(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even number for Simpson's (1/3) rule.")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    # Apply Simpson's (1/3) rule formula
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    integral *= h / 3
    return integral

# Define the interval [a, b] and number of subintervals n
a = 0
b = 1
n = 6  # Number of subintervals (must be even)

# Calculate the integral using Simpson's (1/3)rd rule
result = simpsons_rule(a, b, n)
print(f"The estimated value of the integral is: {result:.6f}")


#Q.3a.2. write python program to obtain a real root of f(x)=x^3-8x-4 by using newton-raphson method.

def f(x):
    return x**3 - 8*x - 4

def f_prime(x):
    return 3*x**2 - 8  # Derivative of f(x)

def newton_raphson(initial_guess, tolerance=1e-7, max_iterations=100):
    x_n = initial_guess
    
    for i in range(max_iterations):
        f_x_n = f(x_n)
        f_prime_x_n = f_prime(x_n)
        
        # Check if derivative is zero to avoid division by zero
        if f_prime_x_n == 0:
            print("Derivative is zero. No solution found.")
            return None
        
        # Update the root estimate
        x_n1 = x_n - f_x_n / f_prime_x_n
        
        # Check for convergence
        if abs(x_n1 - x_n) < tolerance:
            return x_n1
        
        x_n = x_n1
    
    print("Maximum iterations reached. No solution found.")
    return None

# Initial guess for the root
initial_guess = 4

# Finding the root
root = newton_raphson(initial_guess)

if root is not None:
    print(f"The estimated real root of the equation is: {root:.6f}")


#Q.3b.1. write python program to obtain the approximate real root of x^3-2x-5=0 in[2,3] using regula falsi method. 

def f(x):
    return x**3 - 2*x - 5

def regula_falsi(x0, x1, tolerance=1e-7, max_iterations=100):
    if f(x0) * f(x1) >= 0:
        print("The function has the same signs at the endpoints. No root found.")
        return None

    for i in range(max_iterations):
        # Calculate the point where the line crosses the x-axis
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        # Check if the root is found or if it is within the tolerance
        if abs(f(x2)) < tolerance:
            return x2

        # Update the points based on the sign of the function
        if f(x2) * f(x0) < 0:
            x1 = x2  # Root is in the left subinterval
        else:
            x0 = x2  # Root is in the right subinterval

    print("Maximum iterations reached. No root found.")
    return None

# Set the interval [2, 3]
x0 = 2
x1 = 3

# Finding the root
root = regula_falsi(x0, x1)

if root is not None:
    print(f"The approximate real root of the equation in [{x0}, {x1}] is: {root:.6f}")


# Q.3.b.2. write python program to evaluate interpolate value f(3.5)of the given data by lagranges method.
# x  0 1 2 5     y=f(x)  2 3 12 147

def lagrange_interpolation(x_values, y_values, x):
    """Perform Lagrange interpolation to find the value of f(x)."""
    n = len(x_values)
    result = 0.0
    
    for i in range(n):
        # Calculate the Lagrange basis polynomial L_i(x)
        L_i = 1.0
        for j in range(n):
            if j != i:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += y_values[i] * L_i
        
    return result

# Given data points
x_values = [0, 1, 2, 5]
y_values = [2, 3, 12, 147]

# Value to interpolate
x_to_interpolate = 3.5

# Evaluating f(3.5)
interpolated_value = lagrange_interpolation(x_values, y_values, x_to_interpolate)

print(f"The interpolated value f({x_to_interpolate}) is: {interpolated_value:.6f}")

