#Q.1.1 Evaluate following expression on python 
#a) M=[1,2,3,4,5,6,7]. Find length of M
M=[1,2,3,4,5,6,7]
print(len(M))

#b) L="XY"+"pqr". find L
L="XY"+"pqr"
print(L)

#c) s='Make In India', find (s[:5])& (s[:9])
s="Make In India"
print(s[:5])
print(s[:9])

#Q.1.3 Write pythone pragram to reverse the string S= [3,4,5,6,7,8,9,10,11,12,13]
S=[3,4,5,6,7,8,9,10,11,12,13]
rev= S[::-1]
print(rev)

#Q2 generate all prime numbers between 51 to 100 using python
for i in range(51,101):
    count=0
    for j in range(1,i+1):
        if (i%j)==0:
            count=count+1
    if(count==2):
        print(i)
    
#Q.3# Write Python program to estimate a root of an equation f(x) = x^5+3x+1 using Newton-Raphson method correct up to four decimal places.
def f(x):
    """Define the function for which we want to find the root."""
    return  x**5 + 3 * x + 1

def f_prime(x):
    """Define the derivative of the function."""
    return 5 * x**4 + 3

def newton_raphson(initial_guess, tolerance=1e-4, max_iterations=100):
    """Approximate the root of the function using the Newton-Raphson method."""
    x_n = initial_guess

    for iteration in range(max_iterations):
        x_n1 = x_n - f(x_n) / f_prime(x_n)  # Newton-Raphson formula

        # Check for convergence
        if abs(x_n1 - x_n) < tolerance:
            print(f"Root found: x = {x_n1:.4f} in {iteration + 1} iterations")
            return x_n1
        
        x_n = x_n1

    print("Max iterations reached without finding a root.")
    return None

# Initial guess for the root
initial_guess = -1.0

# Call the newton_raphson function to find the root
root = newton_raphson(initial_guess)


#Q.3b2  Write Python program to evaluate interpolate value f(153) of the given data.
# X  150 152 154 155 y=f(x)  12.247  12.329  12.410 12.490

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
x_values = [150,152,154,155]
y_values = [12.247,12.329,12.410,12.490]

# Evaluate f(153)
x_to_interpolate = 153
interpolated_value = lagrange_interpolation(x_values, y_values, x_to_interpolate)

print(f"The interpolated value f(153) is: {interpolated_value:.6f}")
