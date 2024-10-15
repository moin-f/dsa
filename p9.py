#Q.2.1 using python, find eigenvalues and corresponding eigenvectors of the matrix  
# A=[1 3 3  ;2 2 3  ;4 2 1]

import sympy as sy
sy.init_printing()
A= sy.Matrix([[1,3,3],[2,2,3],[4,2,1]])
print("eigenvalues = ",A.eigenvals())

A.eigenvects()

#Q.2.2 write python code to find product of n natural numbers using while loop
n=int(input("enter number:"))
i=1
num=1
while i<=n:
    num=num*i
    i=i+1
print("product of ",n, "natural number is ",num)

#Q3 Write Python code to find eigenvalues and corresponding eigenvectors of the matrix A=[3 -2  ;6 -4 ] and hence find matrix P with diagonalize to A.
import numpy as np

# Define the matrix A
A = np.array([[3,-2],
              [6,-4]])

# Calculate eigenvalues and eigenvectors
eigenvalues, P = np.linalg.eig(A)

# Create a diagonal matrix D from the eigenvalues
D = np.diag(eigenvalues)

# Print the results
print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nMatrix P (eigenvectors):")
print(P)
print("\nDiagonal Matrix D (eigenvalues):")
print(D)

# Verify the diagonalization: A = P * D * P_inv
P_inv = np.linalg.inv(P)
A_reconstructed = P @ D @ P_inv
print("\nReconstructed Matrix A from P, D:")
print(A_reconstructed)

#Q.3b2  Write a Python program to estimate the value of the integral 1 to 5 (1/ (1+x))  dx using Trape-zoidal rule (n=10).

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

