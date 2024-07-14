def  febo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return febo(i-2) + febo(i-1)
for i in range (13):
    print(febo(i))
