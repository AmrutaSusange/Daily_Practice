s = 'amruta'
for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                    print(s[i])
            else:
                   continue

# this solution is o(n^2) which is not at all optomized

def isogram(p):
    d = {}
    for char in p:
              if char in d:
                     return 1
              else:
                     d[char] =1
    return 0

print(isogram('sudhir'))



def duplicate_count(inp):
    out= {}
    for char in inp:
        if char in out:
            out[char] +=1
        else:
            out[char] =1
    
    for key, val in out.items():
        if val > 1:
            return key
            break
    return '#'
        
      
print(duplicate_count('geeksforgeeks'))


def distict_char(inp):
    out= {}
    for char in inp:
        if char in out:
            out[char] +=1
        else:
            out[char] =1
    
    for key, val in out.items():
        if val == 1:
            return key
            break
    return '#'
        
      
print(distict_char('geeksforgeeks'))