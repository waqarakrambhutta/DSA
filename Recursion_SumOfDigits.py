def SumOfDigits(n):
    assert n>=0 and n == int(n),'The number must be a positive integer.'
    if n==0:
        return n
    else:
        return int(n%10) + SumOfDigits(int(n/10))


print(SumOfDigits(12234))