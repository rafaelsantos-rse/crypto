for n in range(input()):
    a, b, c = input()
    print "{} {} {} {} {}".format(a%c, b%c, (a+b)%c, (a-b)%c, (a*b)%c)
