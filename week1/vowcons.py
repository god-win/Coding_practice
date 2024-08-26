string=input("Enter String:")
l=list("aeiou")
v,c=0,0
for i in string:
    if i in l:
        v+=1
    else:
        c+=1
print("vowels=",v,"Consonents",c)
