#Q.1.2 use print command on python to find
#a. sin30   b. pi   c.e   cos30
import math
print(math.sin(30))
print(math.pi)
print(math.e)
print(math.cos(30))

#Q.1.3 write python code to generate modulus value of -10,10,-1,1,0
import math
print(math.fabs(-10))
print(math.fabs(10))
print(math.fabs(-1))
print(math.fabs(1))
print(math.fabs(0))

#Q.2.1 use python to generate second , fifth, eightcharacters from thr string 'MATHEMATICS'
s="MATHEMATICS"
print("second character of ",s, "is ", s[1])
print("fifth character of ",s,"is ",s[4],"\n eighth character of ",s,'is',s[7])

#Q.2.2 using python find eigenvalues and corresponding eigen vectorsof the matrix 
# A=[ 3 -2  ; 6 -4]
import sympy as sy
sy.init_printing()
A=sy.Matrix([[3,-2],[6,-4]])
A
A.eigenvals()
A.eigenvects()

#Q.3a.1 Write Python program to estimate the value of the integral 1 to 10 (x² + 5x)dx using Simpson's (1/3)rd rule (n=5).

def f(x):
    return x**2 + 5*x

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
a = 1
b = 10
n = 6  # Changed to an even number

# Calculate the integral using Simpson's (1/3)rd rule
result = simpsons_rule(a, b, n)
print(f"The estimated value of the integral is: {result:.6f}")

#Q.3b2 Write Python program to evaluate fourth order forward difference of the given data.
# x  1 2 3 4 5  y=f(x) 40 60 65 50 18
def forward_difference_table(x_values, y_values):
    n = len(y_values)
    difference_table = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize first column with y_values
    for i in range(n):
        difference_table[i][0] = y_values[i]

    # Calculate forward differences
    for j in range(1, n):
        for i in range(n - j):
            difference_table[i][j] = difference_table[i + 1][j - 1] - difference_table[i][j - 1]

    return difference_table

# Given data points
x_values = [1, 2, 3, 4, 5]
y_values = [40, 60, 65, 50, 18]

# Construct forward difference table
difference_table = forward_difference_table(x_values, y_values)

# Display the forward difference table
print("Forward Difference Table:")
for row in difference_table:
    print(row)

# Extract the fourth order forward difference
fourth_order_forward_difference = difference_table[0][4]
print(f"\nThe fourth order forward difference is: {fourth_order_forward_difference}")

