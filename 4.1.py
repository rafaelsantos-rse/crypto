from math import sqrt
j = input()
i = 0
while i < j:
    
    n = input()
    x = int(sqrt(n))
    y = 0
    if (x*x == n):
        print("{} {} {}".format(x, y, 'S'))
        break
    else:
        print("{} {} {}".format(x, y, 'N'))
        while x <= (n+1)/2:
            x += 1
            y = sqrt(x*x - n)
            if (y - int(y) == 0.0) :
                print("{} {} {}".format(x, int(y), 'S'))
                break
            else:
                print("{} {} {}".format(x, int(y), 'N'))
                
    a = int(x + y)
    b = int(x - y)
    print("{} {}".format(b, a))
    print("---")
    i+=1
    
