from math import sqrt

j = input()
i = 0
while i < j:
    
    n = input()
    x = int(sqrt(n))
    y = 0
    c = 'N'
    if (x*x == n):
        c = 'S'
        print("{} {} {}".format(x, y, c))
        break
    else:
        print("{} {} {}".format(x, y, c))
        x += 1
        while x < (n+1)/2:
            y = sqrt(x*x - n)
            if (y - int(y) == 0.0) :
                c = 'S'
                print("{} {} {}".format(x, int(y), c))
                break
            else:
                print("{} {} {}".format(x, int(y), c))
                x += 1
    if (c == 'S'):
        
        a = int(x + y)
        b = int(x - y)
    else:
        a = n
        b = 1
    print("{} {}".format(b, a))
    print("---")
    i+=1

