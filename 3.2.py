n = input()
for number in range(n):
    a, b, c = input()
    r = [a,b]
    q = ['-','-']
    x = [1,0]
    y = [0,1]
    print "{} {} {} {}".format(r[0], q[0], x[0], y[0])
    print "{} {} {} {}".format(r[1], q[1], x[1], y[1])
    i = 0
    while r[len(r)-1] > 0:
        q.append( ( r[i] - (r[i]%r[i+1]) ) / r[i+1] )
        r.append(r[i]%r[i+1])
        if r[len(r)-1] == 0:
            x.append("-")
            y.append("-")
        else:
            x.append(x[i] - q[i+2]*x[i+1])
            y.append(y[i] - q[i+2]*y[i+1])
        print "{} {} {} {}".format(r[len(r)-1], q[len(q)-1], x[len(x)-1], y[len(y)-1])
        i+=1
    if(c%r[len(r) -2] == 0):
        k = c/r[len(r)-2]
        print "{} {}".format(k*x[len(x)-2], k*y[len(y)-2])
    else:
        print "0"
    print "---"
