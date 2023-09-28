# import sys
# sys.setrecursionlimit(1000) # to increase stack depth or stack mamory.

def fectorial(n):
    
    # step 3 (unintentional or constraints)
    assert n>=0 and n == int(n), 'The number must be positive integers only!'
    
    # step 2 (condition)
    if n in [0,1]: 
        return 1
    
    # step 1 (expression)
    else:
        return n * fectorial(n-1) 
    

print(fectorial(5))