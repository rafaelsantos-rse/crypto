qnt = input()
for n in range(qnt):
    a,b = input()
    print a
    print b
    while b > 0:
        c = a%b
        a = b
        b = c
        print c
    print '--'    

    
