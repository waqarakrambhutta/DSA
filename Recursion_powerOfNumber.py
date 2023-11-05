
def PowerOfNumber(Base,Exp):
    assert Exp>0 and Exp == int(Exp),'Power must be a positive integer.'
    if Exp==0:
        return 1
    if Exp==1:
        return Base
    return Base * PowerOfNumber(Base , Exp-1)

print(PowerOfNumber(2,4))