for e in range(int(input())):
    c, a = input()
    r = 1
    e = c - 1
    while e!=0:
        if e%2 == 0:
            print r,a,e,'N'
            e /= 2
        else:
            print r,a,e,'S'
            r = (r*a)%c
            e = (e-1)/2
        a = (a**2)%c
    print r, a, e, 'N'
    if r == 1:
        print 'inconclusivo'.upper()
    else:
        print 'conclusivo'.upper()
    print '---'
    
        
