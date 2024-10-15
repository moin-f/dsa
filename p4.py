#Q.1.1 using python code sort the tuple in ascending and descending order 5,-3,0,1,6,-6,2
numbers =(5,-3,0,1,6,-6,2)
ascending_order=tuple(sorted(numbers))
descending_order=tuple(sorted(numbers,reverse=True))
print(ascending_order)
print(descending_order)

#Q.1.2 write python program which deals with concatenation and repeatition of lists 
#list1=[15,20,25,30,35,40]   list2=[7,14,21,28,35,42]
#a) find list1 +list2
#b) find 9*list1
#c) find 7*list2

list1=[15,20,25,30,35,40]
list2=[7,14,21,28,35,42]
a= list1+list2
b=9*list1
c=7*list2
print(a)
print(b)
print(c)

#Q.2.2 find the data type of the following daya by using python code:
# a. number  b. 31.25  c. 8+4j  d. Mathematics e. 49
a="number"
b= 31.25
c=8+4j
d= "Mathematics"
e=49
print("data type of ",a, "is ", type(a),"\ndata type of ",b,"is ",type(b),"\ndata type of ",c, "is ", type(c),"\ndata type of ", d, "is ",type(d),"\ndata type of ",e, "is ",type(e))

#Q.2.3 write python program to find the determinant of matrices A=[1 0 5 ; 2 1 6 : 3 4 0] and B=[2 5 : -1 4]
import numpy as np
# define a matrix
A= np.array([[1,0,5],[2,1,6],[3,4,0]])
B=np.array([[2,5],[-1,4]])
# calculate the determinant
detA =np.linalg.det(A)
detB =np.linalg.det(B)
print("A=",A)
print("B=",B)
print("Determinant of matrix A is ", detA,"\nDeterminant of matrix B is ",detB)

#Q3.a.1 write python program to estimate the value of the integral xsin(x) dx from 0 to pi using simpson's (1/3)rd rule (n=6)

import numpy as np

def f(x):
    """Define the function to be integrated."""
    return x * np.sin(x)

def simpsons_rule(a, b, n):
    """Estimate the integral of f(x) from a to b using Simpson's (1/3) rule."""
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    
    h = (b - a) / n  # Step size
    integral = f(a) + f(b)  # f(a) + f(b)
    
    # Sum the odd indices
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    
    # Sum the even indices
    for i in range(2, n, 2):
        integral += 2 * f(a + i * h)
    
    integral *= h / 3  # Final result
    return integral

# Set the limits and number of intervals
a = 0
b = np.pi
n = 6

# Estimate the integral
result = simpsons_rule(a, b, n)
print(f"The estimated value of the integral from {a} to {b} is: {result:.6f}")

#Q.3.b.1 write the python program to find all positive prime numbers less than givan number n.

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    """Find all prime numbers less than n."""
    primes = []
    for num in range(2, n):  # Start from 2 since 1 is not prime
        if is_prime(num):
            primes.append(num)
    return primes

# Input: Get a number from the user
n = int(input("Enter a positive integer n: "))

# Find and print all prime numbers less than n
primes = find_primes(n)
print(f"Prime numbers less than {n}: {primes}")

