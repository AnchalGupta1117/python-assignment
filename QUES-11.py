#  Write a python program that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for el in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")
