qnt = input()
for n in range(qnt):
    D,d = input()
    q = 0
    r = D
    print q, r
    while r >= d:
        r -= d
        q += 1
        print q, r
    print '--'
