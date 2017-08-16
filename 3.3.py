def exist(point, plane):
    for e in plane:
        if e == point:
            return True
    return False
qnt = input()
for number in range(qnt):
    n = input()
    d = {}
    i = 2
    while n > 1:
        r = n % i
        if r == 0:
            if exist(i, d):
                d[i]+= 1
            else:
                d[i] = 1
            n = n / i
        else:
            if(i>=3):
                i+=2
            else:
                i+=1
    k = d.keys()
    k.sort()
    for e in k:
        print "{} {}".format(e, d[e])
    print "---"

