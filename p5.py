#Q.2.2 using linsolve command in python, solve the following system of linear equations:
# x-2y+3z=7  ;  2x+y+z=4  ; -3x+2y-2z=-10
import sympy as sy
x =sy.symbols('x')
y =sy.symbols('y')
z =sy.symbols('z')

EQN1=sy.Eq(x - 2*y +3*z,7)
EQN2=sy.Eq(2*x + y +z ,4)
EQN3=sy.Eq(-3*x +2*y - 2*z,-10)

system = [EQN1,EQN2,EQN3]
solnSet =sy.linsolve(system,x,y,z)
solnSet

#Q.3a.1. write the python code to find eigenvalues and corresponding vectors of the matrix . A=[1 3 3  ;2 2 3  ;4 2 1] and hence find matrix P with diagonalize to A
import numpy as np

# Define the matrix A
A = np.array([[1, 3, 3],
              [2, 2, 3],
              [4, 2, 1]])

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

#Q3.b1.  write python programm to obtain the approximate real root of x^3-4x-9=0 by using regula falsi method.

def f(x):
    """Define the function for which we want to find the root."""
    return x**3 - 4*x - 9

def regula_falsi(x0, x1, tolerance=1e-6, max_iterations=100):
    """Approximate the root of the function using the Regula-Falsi method."""
    if f(x0) * f(x1) >= 0:
        print("The function has the same signs at the endpoints. Choose different points.")
        return None

    for iteration in range(max_iterations):
        # Calculate the root using the Regula-Falsi formula
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        
        # Check if the current approximation is close enough to the root
        if abs(f(x2)) < tolerance:
            print(f"Root found: x = {x2:.6f} in {iteration + 1} iterations")
            return x2
        
        # Update the interval
        if f(x0) * f(x2) < 0:
            x1 = x2  # The root is in the left subinterval
        else:
            x0 = x2  # The root is in the right subinterval

    print("Max iterations reached without finding a root.")
    return None

# Define the initial interval [2, 3]
x0 = 2
x1 = 3

# Call the regula_falsi function to find the root
root = regula_falsi(x0, x1)

