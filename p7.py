#Q.2.2 Write python code to obtain f(-1),f(0)f(1) of f(x)= x^3-4x-9
def f(x):
    return x**3-4*x-9
print(f(-1),"\n",f(0),"\n",f(1))

#Q3a.2 Write Python program to evaluate interpolate value f(3) of the given data.
# X 0 1 2 5   y=f(x)  2 3 12 147

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    
    for i in range(n):
        # Calculate the Lagrange basis polynomial
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Given data points
x_values = [0, 1, 2, 5]
y_values = [2, 3, 12, 147]

# Evaluate f(3)
x_to_interpolate = 3
interpolated_value = lagrange_interpolation(x_values, y_values, x_to_interpolate)

print(f"The interpolated value f(3) is: {interpolated_value:.6f}")


#Q3b 1 Write Python program to estimate the value of the integral 2 to 10 (1/(1 + x)) dx using Trape- zoidal rule (n = 8) .
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

