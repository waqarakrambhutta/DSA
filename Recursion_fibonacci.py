def fibonacci(n):
    assert n>=0 and n == int(n), 'The number must be a positive integer.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))