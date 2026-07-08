# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# element is 34.
# Explanation: The largest element of the array is 35 and the second largest

# def secondGreater(arr):

#     for i in range(len(arr)):
#         for j in range(1, len(arr)):
#             if arr[i] < arr[j]:
#                 continue
#             else:
#                 i, arr[i] = j, arr[j]
#     return arr


def secondGreater(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len (arr)) :
            if arr[max_index] > arr[j]:
                continue
            else:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
        print (arr)
    

print(secondGreater([12, 35, 1, 10, 34, 1]))










# Input: arr] = c
# Output: [3, 4, 5, 2, 1]
# Explanation: Swapping 1 and 3, makes the array [3, 2, 1, 4, 5]. Now, swapping
# 2 and 4, makes the array [3, 4, 1, 2, 5]. Again,swapping 1 and 5, makes the
# array [3, 4, 5, 2, 1]



def swapElements(arr):
    for i in range(len(arr)-2):
        arr[i], arr[i+2] = arr[i+2], arr[i]
    return arr

print(swapElements([1,2,3,4,5]))