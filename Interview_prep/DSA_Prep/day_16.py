def subsequence(a,b):
    start = 0
    count = 0
    for char in a:
        if start < len(b):
            for let in range(start,len(b)):
                if char ==  b[let]:
                    count +=1
                    start = let+1
                    break
    if count == len(a):
        return True
    else:
        return False


# print(subsequence('AXY', 'YADXCP'))


# Input:
s1 = 'gacdb'
s2 = 'gafd'
# Output: cogf


def strConcate(s1, s2):
    new= ''
    for s in s1:
        for st in s2:
            if s == st and s in new:
                break
            else:
                new +=s
    return new

# print(strConcate('gacdb', 'gafd'))


set1 = set(s1)
set2 = set(s2)
set3 = set1.difference(set2)
set4 = set2.difference(set1)
set5 = set3.union(set4)
out = ''.join(set5)
# print(set5)
# print(out)


set1 = set(s1)
set2 = set(s2)
result = set1 ^ set2   # symmetric difference
out = ''.join(result)
# print(out)



def recur(n):
    if n == 0:
        return
    recur(n-1)
    print(n, end=' ')

# recur(10) 



# Input: txt = "GeeksForGeeks". pat = "For"
# Output: -1

def patSearch(txt, pat):
    for i in range(len(txt)):
        val1 = txt[i]
        val2 = pat[0]
        if val1 == val2:
            search = txt[i:i+len(pat)]
            if search == pat:
                return i
            else:
                continue
        else:
            continue
    return -1


# print(patSearch("GeeksForGeeks", "For"))

txt = "GeeksForGeeks"
pat = "For"
# for i in range(len(txt)):
    # print(txt[i:i+len(pat)])




S = "bad is good"
# Output: big


def firstChar(S):
    sl = S.split(' ')
    out = ''
    for item in sl:
        out += item[0]
    return out

firstChar("bad is good")


