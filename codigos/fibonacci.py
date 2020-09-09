def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Pon mes a analizar: '))
print(f'Los conejos del mes: {n} son :{fibonacci(n)}')