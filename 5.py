def Eimpar(n):
    if n % 2 == 0:
        return 'N'
    else:
        return 'S'
    
for n in range(input()):
    a, t, n = input()
    r = 1
    print "{} {} {} {}".format(r,a,t,Eimpar(t))
    while t != 0:
        if t % 2 == 0:
            t = t/2
            a = (a*a) % n

        else:
            t = (t-1) / 2
            r = (r*a) % n
            a = (a*a) % n
            
        print "{} {} {} {}".format(r,a,t,Eimpar(t))
    print '---'
