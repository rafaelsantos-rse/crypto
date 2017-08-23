from math import sqrt

n = input()
L = [3]
L2 = [3]
m = int(sqrt(n))

a = 3 + 2
while a < n:
    L.append(a)
    L2.append(a)
    a += 2

print L
print m


p = 3
j = 0
crivo = []

while p < m:
    
    i = L.index(p*p)
    
    print "{} {} {}".format(p, p*p, i)

    while i < len(L):

        crivo.append(L[i])
        try:
            L2.remove(L[i])
        except ValueError:
            pass

        i += p

    print crivo

    print L2

    j += 1
    p = L2[j]
    crivo = []
    
L2 = [2] + L2    
print L2

    

