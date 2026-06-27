def isAnagram(s: str, t: str) -> bool:
    sd = {}
    td = {}
    for char in s:
        if char in sd:
            sd[char] +=1
        else:
            sd[char] =1
    print(sd)

    for char in t:
        if char in td:
            td[char] +=1
        else:
            td[char] =1 
    print(td)  

    if sd == td:
        return True
    else:
        return False

print(isAnagram(s = 'aab', t = 'abb'))


s = 'rat'
t = 'tar'
sd = {}
for char in s:
    if char in sd:
        sd[char] +=1
    else:
        sd[char] = 1

for char in t:
    if char in sd:
        sd[char] -=1
    else:
        continue

if all(v == 0 for v in sd.values()):
    print(True)