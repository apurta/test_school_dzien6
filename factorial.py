


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is defined only for nonnegativ numbers")
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

print(factorial(1))
print(factorial(-1)) # zwróci chociaż nie powinna wiec robimy wyjatek -_-


