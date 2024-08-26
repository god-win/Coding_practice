def findocc(sttr,char):
    c=0
    for i in sttr:
        if i==char:
            c+=1
    return c
print(findocc("hello","l"))
