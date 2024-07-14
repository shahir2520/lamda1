def  febo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return febo(i-2) + febo(i-1)
for x in range(10):
    print(febo(x))







