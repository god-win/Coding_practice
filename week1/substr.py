string=input("Enter String:")
for i in range(len(string)+1):
    for j in range(i+1,len(string)+1):
        print(string[i:j])
