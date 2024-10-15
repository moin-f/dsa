# 1. Use python code to evaluate each of the following expression.
# a. 20 modulus 2 +7 - (3+7)  * 20 /2
a= 20%2+7-(3+7)*20/2
print('a = ', a)

# b. 30 x 10 floor division 3 +10 modulus 3
b= 30*10//3+10%3
print('b = ',b)

# c. 2^5 -2^4 +4 floor division 4
c = 2**5 - 2**4 + 4//4
print ('c = ', c)


# 2. Write python code to repeat the following string 9 times using the string operator '*'.
# a. python    b. Mathematics 
a= 'python '
b= 'Mathematics '
print(a *9)
print(b*9)

# 3.Write python program to generate the square of numbers from 1 to 10.
n=1
while n<=10:
    print('the square of ',n,'is ',n**2)
    n=n+1


# Q.2) Attempt th following:
# 1. Using python code construct the following matrices.
#  1)An identity matrix od order 10 x 10

import numpy as np
np.array(np.identity(10))


# 2) zero matrix of order 7 x 3

import numpy as np
np.zeros([7,3])


# 3) Ones matrix of order 5 x 4
import numpy as np
np.ones([5,4])

# 2. Write python program to find the 10 term of the sequence of the function f(x)=x^2+x 


# alternate code 
for a in range(1,11):
    b= a**2 +a
    print(b)



# 3. generate all the prime numbers between 1 to 100 using python code.
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if (i%j)==0:
            count=count+1
    if(count==2):
        print(i)
        


# Q.3 a. 1.Write Python program to estimate the value of the integration sin(x)dx of limits 0 to pi using Simpson’s (1/3)rd rule (n=6).
import numpy as np

def f(x):
    """Function to integrate."""
    return np.sin(x)

def simpsons_rule(a, b, n):
    """Estimate the integral of f(x) from a to b using Simpson's (1/3) rule."""
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    
    h = (b - a) / n  # Step size
    integral = f(a) + f(b)  # f(a) + f(b)
    
    # Apply Simpson's rule
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)  # Odd indices
    
    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)  # Even indices
    
    integral *= h / 3  # Final multiplication by h/3
    return integral

# Define the interval and number of subintervals
a = 0
b = np.pi
n = 6

# Estimate the integral
integral_value = simpsons_rule(a, b, n)

print(f"The estimated value of the integral ∫ sin(x) dx from 0 to π is: {integral_value:.6f}")


# Q3.a.2. write the python program to evaluate interpolate value f(3) of given data by lagranges method.
# x 0 1 2 5      y=f(x)  5 13 22 129 
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
y_values = [5, 13, 22, 129]

# Value to interpolate
x_to_interpolate = 3

# Evaluating f(3)
interpolated_value = lagrange_interpolation(x_values, y_values, x_to_interpolate)

print(f"The interpolated value f({x_to_interpolate}) is: {interpolated_value:.6f}")


# Q.3 .b.1. write the python program to obtain the approximate real root of x^3-4X-9=0 by using regula falsi method.
def f(x):
    return x**3 - 4*x - 9

def regula_falsi(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("The function has the same sign at the endpoints a and b.")
        return None

    for i in range(max_iter):
        # Calculate the false position
        c = a - (f(a) * (b - a)) / (f(b) - f(a))
        
        # Check if we found the root or if the interval is small enough
        if f(c) == 0 or abs(f(c)) < tol:
            return c

        # Update the interval
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
    # Return the approximation after the max iterations
    return c

# Initial guesses for the root
a = 2
b = 3

# Tolerance level and maximum iterations
tolerance = 1e-6
max_iterations = 100

# Calculate the root using Regula-Falsi method
root = regula_falsi(a, b, tolerance, max_iterations)

if root is not None:
    print(f"The approximate real root of the equation is: {root:.6f}")
else:
    print("The method did not converge.")


#b.2. Write Python program to estimate the value of the integral 2 to 10 (1/(1 + x)) dx using Trape- zoidal rule (n = 8) .
def f(x):
    return 1 / (1 + x)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Calculate the width of each subinterval
    integral = (f(a) + f(b)) / 2  # Initialize with the first and last term

    # Apply the Trapezoidal rule
    for i in range(1, n):
        x = a + i * h
        integral += f(x)  # Sum the middle terms

    integral *= h  # Multiply by the width of the subintervals
    return integral

# Define the interval [a, b] and number of subintervals n
a = 2
b = 10
n = 8  # Number of subintervals

# Calculate the integral using the Trapezoidal rule
result = trapezoidal_rule(a, b, n)
print(f"The estimated value of the integral is: {result:.6f}")

