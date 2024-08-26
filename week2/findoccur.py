def findoccur(targ):
    l=[1,2,3,4,2,5]
    c=0
    for i in l:
        if i==targ:
            c+=1
    return c
print(findoccur(3))
