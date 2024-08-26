string=input("Enter String:")
o=[]
for i in string:
    if i not in o:
        o.append(i)
        print(i,end="")
