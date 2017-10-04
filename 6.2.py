def div(numb):
    count = 0
    for n in range(1,numb+1):
        if numb % n == 0:
            count +=1
    return count

def isAltComp(numb):
    d1 = div(numb)
    is_AC = True
    for n in range(numb-1, 0, -1):
        d2 = div(n)
        if d2 >= d1:
            is_AC = False
            break
    if is_AC:
        return is_AC
    else:
        return is_AC

def chalkup():
    i = int(input())
    l = []
    for n in range(1, i+1):
        if isAltComp(n):

            l.append(n)
    print(l)


if __name__ == "__main__":
    chalkup()
    
