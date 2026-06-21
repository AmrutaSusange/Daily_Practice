# Input: s = "i love programming"
# Output: "I Love Programming"

s = "i love programming"

a = s.split(' ')
print(a)

def convert(st):
    arr = st.split(' ')
    arr2 = []
    for char in arr:
        val = char[0].upper() + char[1:]
        arr2.append(val)
        out = ' '.join(arr2)

    return out

print(convert(s))


# Input:
# N = 13
# Char array = geeksforgeeks
# Output: geeksforgeeks b
# Explanation: combined all the characters
# to form a single string.

ar = 'geeksforgeeks'.split(' ')
print(ar)
output = ''.join(ar)
print(output)