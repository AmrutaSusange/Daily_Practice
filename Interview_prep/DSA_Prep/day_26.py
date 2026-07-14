#remove consecutive duplicates

def consDup(st):
    ans= ''
    for s in range(len(st)-1):
        if st[s] == st[s+1]:
            continue
        else:
            ans +=st[s]

    ans+= st[-1]
    return ans


print(consDup('aabc'))


# merge the strings with alternate charecter

def mergeString(s1, s2):
    new_string = ''
    for i in range(min(len(s1), len(s2))):
        new_string += s1[i] + s2[i]

    new_string += s1[i+1:]
    new_string += s2[i+1:]
    return new_string

        

print(mergeString('Hello', 'Bye'))


