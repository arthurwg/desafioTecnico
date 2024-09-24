def is_fibonacci(n):
    
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


num = int(input("Informe um número: "))


if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
