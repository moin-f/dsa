#Q3. generate all the prime numbers between 1 to 100 using python code.
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

#Q.3b.2 write python program to estimate the value of the integral 2 to10 (1/(1+x))dx usiong traprzoidal rule (n=5)
import numpy as np

# Define the function to integrate
def f(x):
    return 1/(1 + x)

# Trapezoidal Rule implementation
def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Step size
    integral_value = 0.5 * (f(a) + f(b))  # Start with the endpoints

    # Calculate the area for each trapezoid
    for i in range(1, n):
        integral_value += f(a + i * h)

    integral_value *= h  # Final result
    return integral_value

# Set the limits of integration and the number of intervals
a = 2
b = 10
n = 5

# Estimate the integral
integral_result = trapezoidal_rule(a, b, n)
print(f"The estimated value of the integral from {a} to {b} for 1/(1 + x)dx using Trapezoidal rule is: {integral_result:.4f}")
