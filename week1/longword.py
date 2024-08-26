string=input("Enter String:").split()
m=max(len(w) for w in string)
print([w for w in string if len(w)==m])
