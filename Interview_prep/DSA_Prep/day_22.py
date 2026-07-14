import string

s = "Bawds jog, flick quartz, vex nymph"
s = s.lower()
ls = s.split(' ')
ls1 = []
char = string.ascii_lowercase
# print(type(char))

for ele in ls:
    for i in ele:
     ls1.append(i)
# print(ls1)

# for i in ls1:
#    if i in char:
# #       print('true')
# # print('false')


# -------------------------------

def checkPangram(s):
#code here
    arr = [0] * 26
    s= s.lower ()
    for char in s:
        if char.isalpha():
         arr[ord(char)-97] += 1

    for count in arr:
        if count ==0:
            return False
        else:
            continue
    return True

print(checkPangram("Bawds jog, flick quartz, vex nymph"))

# Input: s1 = "geeksforgeeks", s2 = "geeksquiz"
# Output: "fioqruz"
# Explanation: The characters 'f', i, 'o', 'a', 'r', 'u', and 'z' are present in either s1
# or s2, but not in both.

s1 = "geeksforgeeks"
s2 = "geeksquiz"
s1 = set(s1)
s2 = set(s2)
s3 = list(s1^s2)
s3 = ''.join(s3)
print(s3)


# Input: s = "testsample"
# Output: 'e'
# Explanation: e is the character which is having the highest frequency.

def highFreq(s):
    store = {}
    for char in s:
        if char in store:
            store[char] +=1
        else:
            store[char] =1

    for key, val in store.items():
        if max(store.values()):
            return key

print(highFreq("testsample"))




