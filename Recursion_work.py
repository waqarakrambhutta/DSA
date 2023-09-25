# this is how the recursion works in stack mamory.

def firstMethod():
    secondMethod()
    print('this is first method')
    
def secondMethod():
    thirdMethod()
    print('this is second method')
    
def thirdMethod():
    forthMethod()
    print('this is third method')
    
def forthMethod():
    fifthMethod()
    print('this is forth method')
    
def fifthMethod():
    print('this is fifth method')
    
# firstMethod()

def recursionMethod(n):
    if n<1:
        print('n is less than 1')
    else:
        recursionMethod(n-1)
        print(n)
        
recursionMethod(5)