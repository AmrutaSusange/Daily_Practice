#string char rotation to match the second string

def strRotate(s1,s2):
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            new_str = s1[i:] + s1[:i]
            if new_str == s2:
                return new_str
            else:
                continue
        else:
            continue
    return False


print(strRotate('abcd', 'cdab'))






# remove char from first string of the second string

def strRemove(str, str2):
    new_str = ''
    for i in range(len(str)):
        if str[i] not in str2:
            new_str += str[i]
        else:
            continue
    return new_str


print(strRemove('computer','cat'))