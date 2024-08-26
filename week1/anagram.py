def anagram(sttr1,sttr2):
    if len(sttr1)==len(sttr2):
        if sorted(sttr1)==sorted(sttr2):
            return True
    else:
        return False
print(anagram("silent","listen"))
