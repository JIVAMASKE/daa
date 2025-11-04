# Assignment No. 1
# Program: Fibonacci Series using Recursive and Non-Recursive Methods

# --- Recursive Function ---
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# --- Non-Recursive (Iterative) Function ---
def fibonacci_iterative(n):
    a, b = 0, 1
    print("Fibonacci Series (Iterative):", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# --- Main Program ---
num = int(input("Enter the number of terms: "))

# Recursive Output
print("Fibonacci Series (Recursive):", end=" ")
for i in range(num):
    print(fibonacci_recursive(i), end=" ")
print()

# Non-Recursive Output
fibonacci_iterative(num)
