def issort():
    l=[1,2,3,4,5]
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
print(issort())        
