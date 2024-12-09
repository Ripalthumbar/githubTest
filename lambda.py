addition = lambda num : num + 12
print(addition(13))


mul = lambda m1,m2 : m1 * m2
print(mul(2,3))

addition2 = lambda a1,a2,a3 : a1 + a2 + a3
print(addition2(2,3,6))


def demolambda(q):
    return lambda e : e / q 

opr = demolambda(5)

print(opr(60))