#Anagram prob using ordinal

def anagram(s,s1):
    ls1 = 26*[0]
    ls2 = 26*[0]
    for st in s:
        ls1[ord(st)-97] += 1
    
    for st1 in s1:
        ls2[ord(st1)-97] += 1

    if ls1 == ls2:
        return True
    else:
        return False
    
print(anagram("geeks", "kseeg"))


        

    

