# Input: arr = [15, 2, 45, 4 , 7]
# Output: [2, 4]


def indexDigit(arr):
    out= []
    for i in range(len(arr)):
        if i+1 == arr[i]:
           out.append(arr[i])
        else:
            continue
    return out
print(indexDigit([15, 2, 45, 4 , 7]))


# Input: x = 9, arr = [10, 1, 2, 8, 4, 5]
# Output: 5

def smallElements(x, arr):
    count = 0
    for ele in arr:
        if ele <= x:
            count += 1
        else: 
            continue
    return count

print(smallElements(9, [10, 1, 2, 8, 4, 5]))


# Input: s = "what is your name ?"
# Output: wht s yr nm ?


def notVowel(s):
    vov = 'aeiou'
    result = ''
    for i in s:
        if i not in vov:
            result+= i
        else:
            continue
    return result

print(notVowel("what is your name ?"))
