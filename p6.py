#Q.3.1 write python program to find the value of integral (x- sin(x))dx from 0 to pi using simpson's 1/3rd rule.(n=5)

import numpy as np

def f(x):
    return x - np.sin(x)

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
b = np.pi
n = 5  # Number of subintervals (must be even)

# Calculate the integral using Simpson's (1/3)rd rule
# Since n is not even, let's correct it to 6 for the calculation.
n = 6
result = simpsons_rule(a, b, n)
print(f"The estimated value of the integral is: {result:.6f}")

#Q.3.2 write python code to diagonalize matrix A=[3 -2  ; 6 -4] And find matrix P with diagonalise of A and diagonal matrix D
import numpy as np

# Define the matrix A
A = np.array([[3, -2],
              [6, -4]])

# Find the eigenvalues and right eigenvectors of A
eigenvalues, P = np.linalg.eig(A)

# Create the diagonal matrix D from the eigenvalues
D = np.diag(eigenvalues)

# Print the results
print("Matrix A:")
print(A)
print("\nMatrix P (eigenvectors):")
print(P)
print("\nDiagonal Matrix D (eigenvalues):")
print(D)

# Verify the diagonalization: A = P * D * P_inv
P_inv = np.linalg.inv(P)
A_reconstructed = P @ D @ P_inv
print("\nReconstructed Matrix A from P, D:")
print(A_reconstructed)

#Q3b.2 write python code to find the value of integral 1/(1+x) dx from 1 to5 using trapezoidal rule (n=10)

def f(x):
    """Define the function for which we want to integrate."""
    return 1 / (1 + x)

def trapezoidal_rule(a, b, n):
    """Estimate the integral of f from a to b using the Trapezoidal rule."""
    h = (b - a) / n  # Step size
    integral = (f(a) + f(b)) / 2  # Initialize with the first and last terms

    # Sum the function values at the interior points
    for i in range(1, n):
        x = a + i * h
        integral += f(x)

    integral *= h  # Multiply by the step size
    return integral

# Define the interval [1, 5] and number of subintervals n
a = 1
b = 5
n = 10  # Number of subintervals

# Calculate the integral using the trapezoidal rule
result = trapezoidal_rule(a, b, n)
print(f"The estimated value of the integral from {a} to {b} is: {result:.6f}")


