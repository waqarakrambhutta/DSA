def HCF(a,b):
    assert a==int(a) and b==int(b),'Both numbers should be integers only!'
    if a<0:
        a = -1 * a
    if b<0:
        b = -1 * b
    if b==0:
        return a
    return HCF(b,a%b)

print(HCF(48,-18))
