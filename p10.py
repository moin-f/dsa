import sympy as sy
sy.init_printing()
A=sy.Matrix([[1,2],[3,5]])
B=sy.Matrix([[1,-7],[2,3]])
C=sy.Matrix([[3,-5],[0,4]])
RHS=A+(B+C)
LHS=(A+B)+C
print("A+(B+C) = ", RHS)
print("(A+B)+C= ",LHS)
print(  RHS==LHS )
if RHS==LHS:
    print("Associativity holds in matrix addition.")

#Q.2.2  Write python code to generate 10 terms of fibonacci sequence using loop
n=10
n1=0
n2=1
for i in range(10):
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    
#Q.2.3 using python, find determinantand inverse of the matrix if exist.
#   A= [ 4 2 2  :  2 4 2 :  2 2 4]
import sympy as sy
sy.init_printing()
A= sy.Matrix([[4,2,2],[2,4,2],[2,2,4]])
A
A.det()
A.inv()

#Q.3a.1 Write Python program to estimate the value of the integral 0 to 1  (1/(1+x2)dx using Simp- son's (1/3)rd rule (n=6).
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

#Q.3b.2  Write Python program to estimate the value of the integral 2 to 4 (2x²-4x+1)dx using Trapezoidal rule (n=5).

def f(x):
    return 2 * x**2 - 4 * x + 1

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
b = 4
n = 5  # Number of subintervals

# Calculate the integral using the Trapezoidal rule
result = trapezoidal_rule(a, b, n)
print(f"The estimated value of the integral is: {result:.6f}")
