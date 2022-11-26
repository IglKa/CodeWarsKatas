def even_fib(m):
    fib = [0, 1]
    while fib[-1] < m:
        fib.append(fib[-2] + fib[-1])
    fib.pop()
    return sum([i for i in fib if i % 2 == 0])


print(even_fib(3382))