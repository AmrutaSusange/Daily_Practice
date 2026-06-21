arr =[1,2,4,5,7,8,3]

arr.insert(0,float('-inf'))
arr.append(float('-inf'))
print(arr)

for i in range((len(arr)-2)):
    val = arr[i+1] > arr[i] and arr[i+1] > arr[i+2]
    if val == True:
        print(True)


def peakElement(arr):
    for i in range(1,(len(arr)-1)):
        val = arr[i] > arr[i-1] and arr[i] > arr[i+1]
        if val == True:
            return True
    return False



print(peakElement(arr))


# Input: arr[] = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.

def getMinMax(elements):
    min_val = elements[0]
    max_val = elements[0]
    for i in elements:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val, max_val

print(getMinMax([3, 2, 1, 56, 10000, 167]))